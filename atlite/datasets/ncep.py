# SPDX-FileCopyrightText: Contributors to atlite <https://github.com/pypsa/atlite>
#
# SPDX-License-Identifier: MIT
"""
Module containing specific operations for creating cutouts from the NCEP
dataset.

DEPRECATED
----------

The ncep dataset module has not been ported to atlite v0.2, yet. Use atlite v0.0.2 to use it,
for the time being!
"""

import glob
import os

import numpy as np
import pandas as pd
import xarray as xr

engine = "pynio"
crs = 4326










def convert_clip_lower(ds, variable, a_min, value):
    """
    Set values of `variable` that are below `a_min` to `value`.

    Similar to `numpy.clip`.
    """
    pass
























weather_data_config = {
    "influx": dict(
        tasks_func=tasks_monthly_ncep,
        prepare_func=prepare_influx_ncep,
        template=os.path.join(
            config.ncep_dir,  # noqa: F821
            "{year}{month:0>2}/dswsfc.*.grb2",
        ),
    ),
    "outflux": dict(
        tasks_func=tasks_monthly_ncep,
        prepare_func=prepare_outflux_ncep,
        template=os.path.join(
            config.ncep_dir,  # noqa: F821
            "{year}{month:0>2}/uswsfc.*.grb2",
        ),
    ),
    "temperature": dict(
        tasks_func=tasks_monthly_ncep,
        prepare_func=prepare_temperature_ncep,
        template=os.path.join(
            config.ncep_dir,  # noqa: F821
            "{year}{month:0>2}/tmp2m.*.grb2",
        ),
    ),
    "soil temperature": dict(
        tasks_func=tasks_monthly_ncep,
        prepare_func=prepare_soil_temperature_ncep,
        template=os.path.join(
            config.ncep_dir,  # noqa: F821
            "{year}{month:0>2}/soilt1.*.grb2",
        ),
    ),
    "wnd10m": dict(
        tasks_func=tasks_monthly_ncep,
        prepare_func=prepare_wnd10m_ncep,
        template=os.path.join(
            config.ncep_dir,  # noqa: F821
            "{year}{month:0>2}/wnd10m.*.grb2",
        ),
    ),
    "runoff": dict(
        tasks_func=tasks_monthly_ncep,
        prepare_func=prepare_runoff_ncep,
        template=os.path.join(
            config.ncep_dir,  # noqa: F821
            "{year}{month:0>2}/runoff.*.grb2",
        ),
    ),
    "roughness": dict(
        tasks_func=tasks_monthly_ncep,
        prepare_func=prepare_roughness_ncep,
        template=os.path.join(
            config.ncep_dir,  # noqa: F821
            "{year}{month:0>2}/flxf.gdas.*.grb2",
        ),
    ),
    "height": dict(
        tasks_func=tasks_height_ncep,
        prepare_func=prepare_height_ncep,
        template=os.path.join(
            config.ncep_dir,  # noqa: F821
            "height/cdas1.20130101.splgrbanl.grb2",
        ),
    ),
}

meta_data_config = dict(
    prepare_func=prepare_meta_ncep,
    template=os.path.join(
        config.ncep_dir,  # noqa: F821
        "{year}{month:0>2}/tmp2m.*.grb2",
    ),
    height_config=weather_data_config["height"],
)
