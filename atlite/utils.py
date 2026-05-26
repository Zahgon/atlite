# SPDX-FileCopyrightText: Contributors to atlite <https://github.com/pypsa/atlite>
#
# SPDX-License-Identifier: MIT
"""
General utility functions for internal use.
"""

import logging
import re
import textwrap
from pathlib import Path

import pandas as pd
import xarray as xr

from atlite.datasets import modules as datamodules
from atlite.gis import maybe_swap_spatial_dims

logger = logging.getLogger(__name__)


def ensure_coords(index: pd.Index | xr.Coordinates) -> xr.Coordinates:
    """
    Convert an index or multiindex to coordinates
    """
    if isinstance(index, pd.MultiIndex):
        coords = xr.Coordinates.from_pandas_multiindex(index, index.name or "dim_0")
    elif isinstance(index, pd.Index):
        coords = xr.Coordinates({index.name or "dim_0": index})
    elif isinstance(index, xr.Coordinates):
        coords = index
    else:
        raise ValueError(
            f"index must be a pandas index or xarray coordinates, not: {index}"
        )
    return coords


def migrate_from_cutout_directory(old_cutout_dir, path):
    """
    Convert an old style cutout directory to new style netcdf file.
    """
    pass




class arrowdict(dict):
    """
    A subclass of dict, which allows you to get items in the dict using the
    attribute syntax!
    """

    def __getattr__(self, item):
        try:
            return self.__getitem__(item)
        except KeyError as e:
            raise AttributeError(e.args[0])

    _re_pattern = re.compile("[a-zA-Z_][a-zA-Z0-9_]*")

    def __dir__(self):
        dict_keys = []
        for k in self.keys():
            if isinstance(k, str):
                m = self._re_pattern.match(k)
                if m:
                    dict_keys.append(m.string)
        return dict_keys


class CachedAttribute:
    """
    Computes attribute value and caches it in the instance.

    From the Python Cookbook (Denis Otkidach) This decorator allows you
    to create a property which can be computed once and accessed many
    times. Sort of like memoization.
    """

    # For python 3.8 >= use functoolts.cached_property instead.

    def __init__(self, method, name=None, doc=None):
        # record the unbound-method and the name
        self.method = method
        self.name = name or method.__name__
        self.__doc__ = doc or method.__doc__

    def __get__(self, inst, cls):
        if inst is None:
            # instance attribute accessed on class, return self
            # You get here if you write `Foo.bar`
            return self
        # compute, cache and return the instance's attribute value
        result = self.method(inst)
        # setattr redefines the instance's attribute so this doesn't get called
        # again
        setattr(inst, self.name, result)
        return result
