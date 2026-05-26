# SPDX-FileCopyrightText: Contributors to atlite <https://github.com/pypsa/atlite>
#
# SPDX-License-Identifier: MIT
"""
Module for downloading and curating data from ECMWFs ERA5 dataset (via CDS).

For further reference see
https://confluence.ecmwf.int/display/CKB/ERA5%3A+data+documentation
"""

import logging
import os
import warnings
import weakref
from pathlib import Path
from tempfile import mkstemp

import cdsapi
import numpy as np
import pandas as pd
import xarray as xr
from dask import compute, delayed
from dask.array import arctan2, sqrt
from dask.utils import SerializableLock
from numpy import atleast_1d

from atlite.gis import maybe_swap_spatial_dims
from atlite.pv.solar_position import SolarPosition

# Null context for running a with statements wihout any context
try:
    from contextlib import nullcontext
except ImportError:
    # for Python verions < 3.7:
    import contextlib



logger = logging.getLogger(__name__)

# Model and CRS Settings
crs = 4326

features = {
    "height": ["height"],
    "wind": ["wnd100m", "wnd_shear_exp", "wnd_azimuth", "roughness"],
    "influx": [
        "influx_toa",
        "influx_direct",
        "influx_diffuse",
        "albedo",
        "solar_altitude",
        "solar_azimuth",
    ],
    "temperature": ["temperature", "soil temperature", "dewpoint temperature"],
    "runoff": ["runoff"],
}

static_features = {"height"}


def _add_height(ds):
    """
    Convert geopotential 'z' to geopotential height following [1].

    References
    ----------
    [1] ERA5: surface elevation and orography, retrieved: 10.02.2019
    https://confluence.ecmwf.int/display/CKB/ERA5%3A+surface+elevation+and+orography

    """
    pass


def _rename_and_clean_coords(ds, add_lon_lat=True):
    """
    Rename 'longitude' and 'latitude' columns to 'x' and 'y' and fix roundings.

    Optionally (add_lon_lat, default:True) preserves latitude and
    longitude columns as 'lat' and 'lon'.
    """
    pass


def get_data_wind(retrieval_params):
    """
    Get wind data for given retrieval parameters.
    """
    pass


def sanitize_wind(ds):
    """
    Sanitize retrieved wind data.
    """
    pass


def get_data_influx(retrieval_params):
    """
    Get influx data for given retrieval parameters.
    """
    pass


def sanitize_influx(ds):
    """
    Sanitize retrieved influx data.
    """
    pass


def get_data_temperature(retrieval_params):
    """
    Get wind temperature for given retrieval parameters.
    """
    pass


def get_data_runoff(retrieval_params):
    """
    Get runoff data for given retrieval parameters.
    """
    pass


def sanitize_runoff(ds):
    """
    Sanitize retrieved runoff data.
    """
    pass


def get_data_height(retrieval_params):
    """
    Get height data for given retrieval parameters.
    """
    pass




def retrieval_times(coords, static=False, monthly_requests=False):
    """
    Get list of retrieval cdsapi arguments for time dimension in coordinates.

    If static is False, this function creates a query for each month and year
    in the time axis in coords. This ensures not running into size query limits
    of the cdsapi even with very (spatially) large cutouts.
    If static is True, the function return only one set of parameters
    for the very first time point.

    Parameters
    ----------
    coords : atlite.Cutout.coords
    static : bool, optional
    monthly_requests : bool, optional
        If True, the data is requested on a monthly basis. This is useful for
        large cutouts, where the data is requested in smaller chunks. The
        default is False

    Returns
    -------
    list of dicts witht retrieval arguments

    """
    pass


def noisy_unlink(path):
    """
    Delete file at given path.
    """
    pass






def open_with_grib_conventions(
    grib_file: str | Path, chunks=None, tmpdir: str | Path | None = None
) -> xr.Dataset:
    """
    Convert grib file of ERA5 data from the CDS to netcdf file.

    The function does the same thing as the CDS backend does, but locally.
    This is needed, as the grib file is the recommended download file type for CDS, with conversion to netcdf locally.
    The routine is a reduced version based on the documentation here:
    https://confluence.ecmwf.int/display/CKB/GRIB+to+netCDF+conversion+on+new+CDS+and+ADS+systems#GRIBtonetCDFconversiononnewCDSandADSsystems-jupiternotebook

    Parameters
    ----------
    grib_file : str | Path
        Path to the grib file to be converted.
    chunks
        Chunks
    tmpdir : Path, optional
        If None adds a finalizer to the dataset object

    Returns
    -------
    xr.Dataset
    """
    pass


def retrieve_data(
    product: str,
    chunks: dict[str, int] | None = None,
    tmpdir: str | Path | None = None,
    lock: SerializableLock | None = None,
    **updates,
) -> xr.Dataset:
    """
    Download data like ERA5 from the Climate Data Store (CDS).

    If you want to track the state of your request go to
    https://cds-beta.climate.copernicus.eu/requests?tab=all

    Parameters
    ----------
    product : str
        Product name, e.g. 'reanalysis-era5-single-levels'.
    chunks : dict, optional
        Chunking for xarray dataset, e.g. {'time': 1, 'x': 100, 'y': 100}.
        Default is None.
    tmpdir : str, optional
        Directory where the downloaded data is temporarily stored.
        Default is None, which uses the system's temporary directory.
    lock : dask.utils.SerializableLock, optional
        Lock for thread-safe file writing. Default is None.
    updates : dict
        Additional parameters for the request.
        Must include 'year', 'month', and 'variable'.
        Can include e.g. 'data_format'.

    Returns
    -------
    xarray.Dataset
        Dataset with the retrieved variables.

    Examples
    --------
    >>> ds = retrieve_data(
    ...     product='reanalysis-era5-single-levels',
    ...     chunks={'time': 1, 'x': 100, 'y': 100},
    ...     tmpdir='/tmp',
    ...     lock=None,
    ...     year='2020',
    ...     month='01',
    ...     variable=['10m_u_component_of_wind', '10m_v_component_of_wind'],
    ...     data_format='netcdf'
    ... )
    """
    pass


def get_data(
    cutout,
    feature,
    tmpdir,
    lock=None,
    data_format="grib",
    monthly_requests=False,
    concurrent_requests=False,
    **creation_parameters,
):
    """
    Retrieve data from ECMWFs ERA5 dataset (via CDS).

    This front-end function downloads data for a specific feature and formats
    it to match the given Cutout.

    Parameters
    ----------
    cutout : atlite.Cutout
    feature : str
        Name of the feature data to retrieve. Must be in
        `atlite.datasets.era5.features`
    tmpdir : str/Path
        Directory where the temporary netcdf files are stored.
    monthly_requests : bool, optional
        If True, the data is requested on a monthly basis in ERA5. This is useful for
        large cutouts, where the data is requested in smaller chunks. The
        default is False
    data_format : str, optional
        The format of the data to be downloaded. Can be either 'grib' or 'netcdf',
        'grib' highly recommended because CDSAPI limits request size for netcdf.
    concurrent_requests : bool, optional
        If True, the monthly data requests are posted concurrently.
        Only has an effect if `monthly_requests` is True.
    **creation_parameters :
        Additional keyword arguments. The only effective argument is 'sanitize'
        (default True) which sets sanitization of the data on or off.

    Returns
    -------
    xarray.Dataset
        Dataset of dask arrays of the retrieved variables.

    """
    pass
