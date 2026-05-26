# SPDX-FileCopyrightText: Contributors to atlite <https://github.com/pypsa/atlite>
#
# SPDX-License-Identifier: MIT
"""
Module containing specific operations for creating cutouts from the CORDEX
dataset.

DEPRECATED
----------

The cordex dataset module has not been ported to atlite v0.2, yet. Use atlite v0.0.2 to use it,
for the time being!
"""

import glob
import os
from itertools import groupby
from operator import itemgetter

import pandas as pd
import xarray as xr

# Model and CRS Settings
model = "MPI-M-MPI-ESM-LR"

crs = 4326  # TODO
# something like the following is correct
# crs = pyproj.crs.DerivedGeographicCRS(4326, pcrs.coordinate_operation.RotatedLatitudeLongitudeConversion(??))
# RotProj(dict(proj='ob_tran', o_proj='latlong', lon_0=180, o_lon_p=-162, o_lat_p=39.25))














weather_data_config = {
    "influx": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_data_cordex,
        oldname="rsds",
        newname="influx",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "influx",
            "rsds_*_{year}*.nc",
        ),
    ),
    "outflux": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_data_cordex,
        oldname="rsus",
        newname="outflux",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "outflux",
            "rsus_*_{year}*.nc",
        ),
    ),
    "temperature": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_data_cordex,
        oldname="tas",
        newname="temperature",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "temperature",
            "tas_*_{year}*.nc",
        ),
    ),
    "humidity": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_data_cordex,
        oldname="hurs",
        newname="humidity",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "humidity",
            "hurs_*_{year}*.nc",
        ),
    ),
    "wnd10m": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_data_cordex,
        oldname="sfcWind",
        newname="wnd10m",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "wind",
            "sfcWind_*_{year}*.nc",
        ),
    ),
    "roughness": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_static_data_cordex,
        oldname="rlst",
        newname="roughness",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "roughness",
            "rlst_*.nc",
        ),
    ),
    "runoff": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_data_cordex,
        oldname="mrro",
        newname="runoff",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "runoff",
            "mrro_*_{year}*.nc",
        ),
    ),
    "height": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_static_data_cordex,
        oldname="orog",
        newname="height",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "altitude",
            "orog_*.nc",
        ),
    ),
    "CWT": dict(
        tasks_func=tasks_yearly_cordex,
        prepare_func=prepare_weather_types_cordex,
        oldname="CWT",
        newname="CWT",
        template=os.path.join(
            config.cordex_dir,  # noqa: F821
            "{model}",
            "weather_types",
            "CWT_*_{year}*.nc",
        ),
    ),
}

meta_data_config = dict(
    prepare_func=prepare_meta_cordex,
    template=os.path.join(
        config.cordex_dir,  # noqa: F821
        "{model}",
        "temperature",
        "tas_*_{year}*.nc",
    ),
    height_config=weather_data_config["height"],
)
