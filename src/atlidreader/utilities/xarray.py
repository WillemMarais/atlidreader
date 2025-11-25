import xarray as xr

from typing import Any


def make_coordinate(arr: Any, name_str: str, attrs: dict | None) -> xr.DataArray:
    """Make an xarray coordinate from
    an array.

    Parameters
    ----------
    arr: Any
        The array.
    name_str: str
        The name of the coordinate.
    """

    return xr.DataArray(arr, coords={name_str: arr}, attrs=attrs)
