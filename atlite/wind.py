# SPDX-FileCopyrightText: Contributors to atlite <https://github.com/pypsa/atlite>
#
# SPDX-License-Identifier: MIT
"""
Functions for use in conjunction with wind data generation.
"""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING

import numpy as np
import xarray as xr

logger = logging.getLogger(__name__)


if TYPE_CHECKING:
    from typing import Literal


def extrapolate_wind_speed(
    ds: xr.Dataset,
    to_height: int | float,
    from_height: int | None = None,
    method: Literal["logarithmic", "power"] = "logarithmic",
) -> xr.DataArray:
    """
    Extrapolate the wind speed from a given height above ground to another.

    If ds already contains a key refering to wind speeds at the desired to_height,
    no conversion is done and the wind speeds are directly returned.

    Extrapolation of the wind speed can either use the "logarithmic" law as
    described in [1]_ or the "power" law as described in [2]_. See also discussion
    in GH issue: https://github.com/PyPSA/atlite/issues/231 .

    Parameters
    ----------
    ds : xarray.Dataset
        Dataset containing the wind speed time-series at 'from_height' with key
        'wnd{height:d}m' and the surface orography with key 'roughness' at the
        geographic locations of the wind speeds.
    to_height : int|float
        Height (m) to which the wind speeds are extrapolated to.
    from_height : int, optional
        Height (m) from which the wind speeds are interpolated to 'to_height'.
        If not provided, the closest height to 'to_height' is selected.
    method : {"logarithmic", "power"}
        Method to use for extra/interpolating wind speeds

    Returns
    -------
    da : xarray.DataArray
        DataArray containing the extrapolated wind speeds. Name of the DataArray
        is 'wnd{to_height:d}'.

    Raises
    ------
    RuntimeError
        If the cutout is missing the data for the chosen `method`

    References
    ----------
    .. [1] Equation (2) in Andresen, G. et al (2015): 'Validation of Danish
       wind time series from a new global renewable energy atlas for energy
       system analysis'.

    .. [2] Gualtieri, G. (2021): 'Reliability of ERA5 Reanalysis Data for
       Wind Resource Assessment: A Comparison against Tall Towers'
       https://doi.org/10.3390/en14144169 .
    """
    pass
