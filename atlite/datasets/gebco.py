#!/usr/bin/env python3

# SPDX-FileCopyrightText: Contributors to atlite <https://github.com/pypsa/atlite>
#
# SPDX-License-Identifier: MIT
"""
Module for loading gebco data.
"""

import logging

import rasterio as rio
import xarray as xr
from pandas import to_numeric
from rasterio.warp import Resampling

logger = logging.getLogger(__name__)

crs = 4326
features = {"height": ["height"]}




def get_data(
    cutout,
    feature,
    tmpdir,
    monthly_requests=False,
    concurrent_requests=False,
    **creation_parameters,
):
    """
    Get the gebco height data.

    Parameters
    ----------
    cutout : atlite.Cutout
    feature : str
        Takes no effect, only here for consistency with other dataset modules.
    tmpdir : str
        Takes no effect, only here for consistency with other dataset modules.
    monthly_requests : bool
        Takes no effect, only here for consistency with other dataset modules.
    concurrent_requests : bool
        Takes no effect, only here for consistency with other dataset modules.
    **creation_parameters :
        Must include `gebco_path`.

    Returns
    -------
    xr.Dataset

    """
    pass
