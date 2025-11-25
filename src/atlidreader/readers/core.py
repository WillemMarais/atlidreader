import xarray as xr
from pathlib import Path

from typing import Protocol


class ReaderProtocol(Protocol):
    def __init__(self, fileP: str | Path, **kwargs):
        """

        Parameters
        ----------
        fileP: str or Path
            The file path to the EarthCARE
            ATLID 2A file.
        kwargs: dict
            kwargs for the `xr.open_dataset`
            function.
        """

        ...

    @staticmethod
    def match_file_name(fileP: str | Path) -> bool:
        """Returns True if this reader matches
        with the given file name."""

        ...

    @property
    def ds(self) -> xr.Dataset: ...
