#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2022 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under the GNU Public Licence, v3 or any higher version
# SPDX-License-Identifier: GPL-3.0-or-later
"""Base class for building Analysis classes."""

import inspect
import logging
from datetime import datetime

import MDAnalysis.analysis.base
import numpy as np
from MDAnalysis.analysis.base import Results
from MDAnalysis.lib.log import ProgressBar
from tqdm.contrib.logging import logging_redirect_tqdm

from .._version import get_versions
from ..lib.math import center_cluster, new_mean, new_variance
from ..lib.util import (
    atomgroup_header,
    correlation_analysis,
    get_cli_input,
    get_compound,
    render_docs,
    )


__version__ = get_versions()['version']
del get_versions

logger = logging.getLogger(__name__)


@render_docs
class AnalysisBase(MDAnalysis.analysis.base.AnalysisBase):
    """Base class derived from MDAnalysis for defining multi-frame analysis.

    The class is designed as a template for creating multi-frame analyses.
    This class will automatically take care of setting up the trajectory
    reader for iterating, and it offers to show a progress meter.
    Computed results are stored inside the :attr:`results` attribute.
    To define a new analysis, `AnalysisBase` needs to be subclassed
    and :meth:`_single_frame` must be defined. It is also possible to define
    :meth:`_prepare` and :meth:`_conclude` for pre- and post-processing.
    All results should be stored as attributes of the
    :class:`MDAnalysis.analysis.base.Results` container.

    Parameters
    ----------
    ${ATOMGROUPS_PARAMETER}
    ${BASE_CLASS_PARAMETERS}
    multi_group : bool
        Analysis is able to work with list of atomgroups

    Attributes
    ----------
    atomgroup : MDAnalysis.core.groups.AtomGroup
        Atomgroup taken for the Analysis (available if `multi_group = False`)
    atomgroups : list[MDAnalysis.core.groups.AtomGroup]
        Atomgroups taken for the Analysis (available if `multi_group = True`)
    n_atomgroups : int
        Number of atomngroups (available if `multi_group = True`)
    _universe : MDAnalysis.core.universe.Universe
        The Universe the atomgroups belong to
    _trajectory : MDAnalysis.coordinates.base.ReaderBase
        The trajectory the atomgroups belong to
    times : numpy.ndarray
        array of Timestep times. Only exists after calling
        :meth:`AnalysisBase.run`
    frames : numpy.ndarray
        array of Timestep frame indices. Only exists after calling
        :meth:`AnalysisBase.run`
    _frame_index : int
        index of the frame currently analysed
    _index : int
        Number of frames already analysed (same as _frame_index + 1)
    results : MDAnalysis.analysis.base.Results
        results of calculation are stored after call
        to :meth:`AnalysisBase.run`
    _obs : MDAnalysis.analysis.base.Results
        Observables of the current frame
    _obs.box_center : numpy.ndarray
        Center of the simulation cell of the current frame
    means : MDAnalysis.analysis.base.Results
        Means of the observables.
        Keys are the same as :attr:`_obs`.
    sems : MDAnalysis.analysis.base.Results
        Standard errors of the mean of the observables.
        Keys are the same as :attr:`_obs`

    Raises
    ------
    ValueError
        If any of the provided AtomGroups (`atomgroups` or `refgroup`) does
        not contain any atoms.
    """

    def __init__(self,
                 atomgroups,
                 multi_group=False,
                 refgroup=None,
                 unwrap=False,
                 jitter=None,
                 concfreq=0):
        if multi_group:
            if type(atomgroups) not in (list, tuple):
                atomgroups = [atomgroups]
            # Check that all atomgroups are from same universe
            if len(set([ag.universe for ag in atomgroups])) != 1:
                raise ValueError("Atomgroups belong to different Universes")

            # Sort the atomgroups,
            # such that molecules are listed one after the other
            self.atomgroups = atomgroups

            for i, ag in enumerate(self.atomgroups):
                if ag.n_atoms == 0:
                    raise ValueError(f"The {i+1}. provided `atomgroup`"
                                     "does not contain any atoms.")

            self.n_atomgroups = len(self.atomgroups)
            self._universe = atomgroups[0].universe
            self._allow_multiple_atomgroups = True
        else:
            self.atomgroup = atomgroups

            if self.atomgroup.n_atoms == 0:
                raise ValueError("The provided `atomgroup` does not contain "
                                 "any atoms.")

            self._universe = atomgroups.universe
            self._allow_multiple_atomgroups = False

        self._trajectory = self._universe.trajectory
        self.refgroup = refgroup
        self.unwrap = unwrap
        self.jitter = jitter
        self.concfreq = concfreq

        if self.refgroup is not None and self.refgroup.n_atoms == 0:
            raise ValueError("The provided `refgroup` does not contain "
                             "any atoms.")

        super(AnalysisBase, self).__init__(trajectory=self._trajectory)

    @property
    def box_center(self):
        """Center of the simulation cell."""
        return self._universe.dimensions[:3] / 2

    def run(self, start=None, stop=None, step=None, verbose=None):
        """Iterate over the trajectory.

        Parameters
        ----------
        start : int
            start frame of analysis
        stop : int
            stop frame of analysis
        step : int
            number of frames to skip between each analysed frame
        verbose : bool
            Turn on verbosity
        """
        logger.info("Choosing frames to analyze")
        # if verbose unchanged, use class default
        verbose = getattr(self, '_verbose',
                          False) if verbose is None else verbose

        self._setup_frames(self._trajectory, start, stop, step)
        logger.info("Starting preparation")

        if self.refgroup is not None:
            if not hasattr(self.refgroup, 'masses') \
               or np.sum(self.refgroup.masses) == 0:
                logger.warning("No masses available in refgroup, falling back "
                               "to center of geometry")
                ref_weights = np.ones_like(self.refgroup.atoms)

            else:
                ref_weights = self.refgroup.masses

        compatible_types = [np.ndarray, float, int, list, np.float_, np.int_]

        self._prepare()

        # Log bin information if a spatial analysis is run.
        if hasattr(self, "n_bins"):
            logger.info(f"Using {self.n_bins} bins.")

        module_has_save = callable(getattr(self.__class__, 'save', None))

        timeseries = np.zeros(self.n_frames)

        for i, ts in enumerate(ProgressBar(
                self._trajectory[self.start:self.stop:self.step],
                verbose=verbose)):
            self._frame_index = i
            self._index = self._frame_index + 1

            self._ts = ts
            self.frames[i] = ts.frame
            self.times[i] = ts.time

            # Before we do any coordinate transformation we first unwrap
            # the system to avoid artifacts of later wrapping.
            if self.unwrap:
                self._universe.atoms.unwrap(
                    compound=get_compound(self._universe.atoms))
            if self.refgroup is not None:
                com_refgroup = center_cluster(self.refgroup, ref_weights)
                t = self.box_center - com_refgroup
                self._universe.atoms.translate(t)
                self._universe.atoms.wrap(
                    compound=get_compound(self._universe.atoms))
            if self.jitter:
                ts.positions += np.random.random(
                    size=(len(ts.positions), 3)) * self.jitter

            self._obs = Results()

            timeseries[i] = self._single_frame()

            # This try/except block is used because it will fail only once and
            # is therefore not a performance issue like a if statement would be.
            try:
                for key in self._obs.keys():
                    if type(self._obs[key]) is list:
                        self._obs[key] = \
                            np.array(self._obs[key])
                    old_mean = self.means[key]
                    old_var = self.sems[key]**2 * (self._index - 1)
                    self.means[key] = \
                        new_mean(self.means[key],
                                 self._obs[key], self._index)
                    self.sems[key] = \
                        np.sqrt(new_variance(old_var, old_mean,
                                             self.means[key],
                                             self._obs[key],
                                             self._index) / self._index)
            except AttributeError:
                with logging_redirect_tqdm():
                    logger.info("Preparing error estimation.")
                # the means and sems are not yet defined.
                # We initialize the means with the data from the first frame
                # and set the sems to zero (with the correct shape).
                self.means = self._obs.copy()
                self.sems = Results()
                for key in self._obs.keys():
                    if type(self._obs[key]) not in compatible_types:
                        raise TypeError(
                            f"Obervable {key} has uncompatible type.")
                    self.sems[key] = \
                        np.zeros(np.shape(self._obs[key]))

            if self.concfreq and self._index % self.concfreq == 0 \
               and self._frame_index > 0:
                self._conclude()
                if module_has_save:
                    self.save()

        logger.info("Finishing up")

        self.corrtime = correlation_analysis(timeseries)

        self._conclude()
        if self.concfreq and module_has_save:
            self.save()
        return self

    def savetxt(self, fname, X, columns=None):
        """Save to text.

        An extension of the numpy savetxt function. Adds the command line
        input to the header and checks for a doubled defined filesuffix.

        Return a header for the text file to save the data to.
        This method builds a generic header that can be used by any MAICoS
        module. It is called by the save method of each module.

        The information it collects is:
          - timestamp of the analysis
          - name of the module
          - version of MAICoS that was used
          - command line arguments that were used to run the module
          - module call including the default arguments
          - number of frames that were analyzed
          - atomgroups that were analyzed
          - output messages from modules and base classes (if they exist)
        """
        # Get the required information first
        current_time = datetime.now().strftime("%a, %b %d %Y at %H:%M:%S ")
        module_name = self.__class__.__name__

        # Here the specific output messages of the modules are collected.
        # We only take into account maicos modules and start at the top of the
        # module tree. Submodules without an own OUTPUT inherit from the parent
        # class, so we want to remove those duplicates.
        messages = []
        for cls in self.__class__.mro()[-3::-1]:
            if hasattr(cls, 'OUTPUT'):
                if cls.OUTPUT not in messages:
                    messages.append(cls.OUTPUT)
        messages = '\n'.join(messages)

        # Get information on the analyzed atomgroup
        atomgroups = ''
        if self._allow_multiple_atomgroups:
            for i, ag in enumerate(self.atomgroups):
                atomgroups += f"  ({i + 1}) {atomgroup_header(ag)}\n"
        else:
            atomgroups += f"  (1) {atomgroup_header(self.atomgroup)}\n"

        header = (
            f"This file was generated by {module_name} on {current_time}\n\n"
            f"{module_name} is part of MAICoS v{__version__}\n\n"
            f"Command line:"
            f"    {get_cli_input()}\n"
            f"Module input:"
            f"    {module_name}{inspect.signature(self.__init__)}"
            f".run({inspect.signature(self.run)})\n\n"
            f"Statistics over {self._index} frames\n\n"
            f"Considered atomgroups:\n"
            f"{atomgroups}\n"
            f"{messages}\n\n"
            )

        if columns is not None:
            header += '|'.join([f"{i:^26}"for i in columns])[2:]

        fname = "{}{}".format(fname, (not fname.endswith('.dat')) * '.dat')
        np.savetxt(fname, X, header=header, fmt='% .18e ', encoding='utf8')


@render_docs
class ProfileBase:
    """Base class for computing profiles.

    Parameters
    ----------
    ${ATOMGROUPS_PARAMETER}
    ${PROFILE_CLASS_PARAMETERS}
    ${PROFILE_CLASS_PARAMETERS_PRIVATE}

    Attributes
    ----------
    ${PROFILE_CLASS_ATTRIBUTES}
    """

    def __init__(self,
                 atomgroups,
                 weighting_function,
                 normalization,
                 grouping,
                 bin_method,
                 output,
                 f_kwargs=None,):
        self.atomgroups = atomgroups
        self.normalization = normalization.lower()
        self.grouping = grouping.lower()
        self.bin_method = bin_method.lower()
        self.output = output

        if f_kwargs is None:
            f_kwargs = {}

        self.weighting_function = lambda ag: weighting_function(ag,
                                                                grouping,
                                                                **f_kwargs)
        # We need to set the following dictionaries here because ProfileBase
        # is not a subclass of AnalysisBase (only needed for tests)
        self.results = Results()
        self._obs = Results()

    def _prepare(self):
        normalizations = ["none", "volume", "number"]
        if self.normalization not in normalizations:
            raise ValueError(f"`{self.normalization}` not supported. "
                             f"Use {', '.join(normalizations)}.")

        groupings = ["atoms", "segments", "residues", "molecules", "fragments"]
        if self.grouping not in groupings:
            raise ValueError(f"`{self.grouping}` is not a valid option for "
                             f"grouping. Use {', '.join(groupings)}.")

        # If unwrap has not been set we define it here
        if not hasattr(self, "unwrap"):
            self.unwrap = True

        if self.unwrap and self.grouping == "atoms":
            logger.warning("Unwrapping in combination with atom grouping "
                           "is superfluous. `unwrap` will be set to `False`.")
            self.unwrap = False

        bin_methods = ["cog", "com", "coc"]
        if self.bin_method not in bin_methods:
            raise ValueError(f"`{self.bin_method}` is an unknown binning "
                             f"method. Use {', '.join(bin_methods)}.")

        if self.normalization == 'number':
            self.tot_bincount = np.zeros((self.n_bins, self.n_atomgroups))

    def _compute_histogram(self, positions, weights=None):
        """Calculate histogram based on positions.

        Parameters
        ----------
        positions : numpy.ndarray
            positions
        weights : numpy.ndarray
            weights for the histogram.

        Returns
        -------
        hist : numpy.ndarray
            histogram
        """
        raise NotImplementedError("Only implemented in child classes")

    def _single_frame(self):
        self._obs.profile = np.zeros((self.n_bins, self.n_atomgroups))
        for index, selection in enumerate(self.atomgroups):
            if self.grouping == 'atoms':
                positions = selection.atoms.positions
            else:
                kwargs = dict(compound=self.grouping)
                if self.bin_method == "cog":
                    positions = selection.atoms.center_of_geometry(**kwargs)
                elif self.bin_method == "com":
                    positions = selection.atoms.center_of_mass(**kwargs)
                elif self.bin_method == "coc":
                    positions = selection.atoms.center_of_charge(**kwargs)

            weights = self.weighting_function(selection)
            profile = self._compute_histogram(positions, weights)

            if self.normalization == 'number':
                bincount = self._compute_histogram(positions, weights=None)

                self.tot_bincount[:, index] += bincount

                # If a bin does not contain any particles we divide by 0.
                with np.errstate(invalid='ignore'):
                    profile /= bincount
                profile = np.nan_to_num(profile)
            elif self.normalization == "volume":
                profile /= self._obs.bin_volume

            self._obs.profile[:, index] = profile

    def _conclude(self):
        self.results.profile = self.means.profile
        self.results.dprofile = self.sems.profile

        if self.normalization == 'number':
            no_occurences_idx = self.tot_bincount == 0
            self.results.profile[no_occurences_idx] = np.nan
            self.results.dprofile[no_occurences_idx] = np.nan

    def save(self):
        """Save results of analysis to file."""
        columns = ["positions [Å]"]

        for i, _ in enumerate(self.atomgroups):
            columns.append(f'({i + 1}) profile')
        for i, _ in enumerate(self.atomgroups):
            columns.append(f'({i + 1}) error')

        # Required attribute to use method from `AnalysisBase`
        self._allow_multiple_atomgroups = True

        AnalysisBase.savetxt(self,
                             self.output,
                             np.hstack((self.results.bin_pos[:, np.newaxis],
                                        self.results.profile,
                                        self.results.dprofile)),
                             columns=columns)
