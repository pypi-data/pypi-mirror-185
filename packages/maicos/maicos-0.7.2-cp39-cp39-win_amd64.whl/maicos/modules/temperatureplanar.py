#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2022 Authors and contributors
# (see the AUTHORS.rst file for the full list of names)
#
# Released under the GNU Public Licence, v3 or any higher version
# SPDX-License-Identifier: GPL-3.0-or-later
"""Planar temperature profile."""

import logging

from ..core import ProfilePlanarBase
from ..lib.util import render_docs
from ..lib.weights import temperature_weights


logger = logging.getLogger(__name__)


@render_docs
class TemperaturePlanar(ProfilePlanarBase):
    """Compute temperature profile in a cartesian geometry.

    Currently only atomistic temperature profiles are supported,
    therefore grouping per molecule, segment, residue, or fragment
    is not possible.

    Parameters
    ----------
    ${PROFILE_PLANAR_CLASS_PARAMETERS}

    Attributes
    ----------
    ${PROFILE_PLANAR_CLASS_ATTRIBUTES}
    """

    def __init__(self,
                 atomgroups,
                 dim=2,
                 zmin=None,
                 zmax=None,
                 bin_width=1,
                 refgroup=None,
                 sym=False,
                 grouping="atoms",
                 unwrap=True,
                 bin_method="com",
                 output="temperature.dat",
                 concfreq=0,
                 jitter=None):

        if grouping != "atoms":
            raise ValueError("Invalid choice of grouping, must use atoms")

        super(TemperaturePlanar, self).__init__(
            weighting_function=temperature_weights,
            normalization="number",
            atomgroups=atomgroups,
            dim=dim,
            zmin=zmin,
            zmax=zmax,
            bin_width=bin_width,
            refgroup=refgroup,
            sym=sym,
            grouping=grouping,
            unwrap=unwrap,
            bin_method=bin_method,
            output=output,
            concfreq=concfreq,
            jitter=jitter)
