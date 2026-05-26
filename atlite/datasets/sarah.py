# SPDX-FileCopyrightText: Contributors to atlite <https://github.com/pypsa/atlite>
#
# SPDX-License-Identifier: MIT
"""
Module containing specific operations for creating cutouts from the SARAH2
dataset.
"""

import glob
import logging
import os
import warnings
from functools import partial

import numpy as np
import pandas as pd
import xarray as xr
from rasterio.warp import Resampling

from atlite.gis import regrid
from atlite.pv.solar_position import SolarPosition

logger = logging.getLogger(__name__)


# Model, CRS and Resolution Settings
crs = 4326
dx = 0.05
dy = 0.05
dt = "30min"
features = {
    "influx": [
        "influx_direct",
        "influx_diffuse",
        "solar_altitude",
        "solar_azimuth",
    ],
}
static_features = {}


def get_filenames(sarah_dir, coords):
    """
    Get all files in directory `sarah_dir` relevent for coordinates `coords`.

    This function parses all files in the sarah directory which lay in the time
    span of the coordinates.

    Parameters
    ----------
    sarah_dir : str
    coords : atlite.Cutout.coords

    Returns
    -------
    pd.DataFrame with two columns `sis` and `sid` for and timeindex for all
    relevant files.

    """
    pass


def interpolate(ds, dim="time"):
    """
    Interpolate NaNs in a dataset along a chunked dimension.

    This function is similar to xr.Dataset.interpolate_na but can be
    used for interpolating along a chunked dimensions (default 'time'').
    As the sarah data has mulitple NaN's in the areas of dawn and
    nightfall and the data is per default chunked along the time axis,
    use this function to interpolate.
    """
    pass


def as_slice(bounds, pad=True):
    """
    Convert coordinate bounds to slice and pad by 0.01.
    """
    pass


def hourly_mean(ds):
    """
    Resample time data to one hour frequency.

    In contrast to the standard xarray resample function this preserves
    chunks sizes along the time dimension.
    """
    pass


def get_data(
    cutout, feature, tmpdir, lock=None, monthly_requests=False, **creation_parameters
):
    """
    Load stored SARAH data and reformat to matching the given cutout.

    This function loads and resamples the stored SARAH data for a given
    `atlite.Cutout`.

    Parameters
    ----------
    cutout : atlite.Cutout
    feature : str
        Name of the feature data to retrieve. Must be in
        `atlite.datasets.sarah.features`
    monthly_requests : bool
        Takes no effect, only here for consistency with other dataset modules.
    concurrent_requests : bool
        Takes no effect, only here for consistency with other dataset modules.
    **creation_parameters :
        Mandatory arguments are:
            * 'sarah_dir', str. Directory of the stored SARAH data.
        Possible arguments are:
            * 'parallel', bool. Whether to load stored files in parallel
            mode. Default is False.
            * 'sarah_interpolate', bool. Whether to interpolate areas of dawn
            and nightfall. This might slow down the loading process if only
            a few cores are available. Default is True.

    Returns
    -------
    xarray.Dataset
        Dataset of dask arrays of the retrieved variables.

    """
    pass
