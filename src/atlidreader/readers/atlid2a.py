import pandas as pd
import xarray as xr
from pathlib import Path

from atlidreader.readers.core import ReaderProtocol
from atlidreader.utilities.xarray import make_coordinate


class AAER2AReader(ReaderProtocol):
    """EarthCARE ATLID aerosol inversion
    2A product reader."""

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

        self._fileP = Path(fileP)
        self._open_dataset_kwargs = kwargs

        # Cache the dataset
        self._ds: xr.Dataset | None = None

    @staticmethod
    def match_file_name(fileP: str | Path) -> bool:
        """Returns True if this reader matches
        with the given file name."""

        file_name_str = Path(fileP).name

        return ("ECA_EXBA_ATL_AER_2A_" in file_name_str) and ("h5" in file_name_str)

    def _open_dataset(self):
        """Open the dataset."""

        if self._ds is None:
            open_dataset_kwargs = {
                "group": "ScienceData",
                "engine": "h5netcdf",
                "phony_dims": "sort",
            } | self._open_dataset_kwargs

            self._ds = xr.open_dataset(
                self._fileP, **open_dataset_kwargs  # type: ignore
            )

    def _embellish_dataset(self):
        """Make the dataset more viable
        for netcdf4."""

        assert self._ds is not None, (
            "The dataset has not "
            "been opened yet via self._open_dataset; "
            "There is probably a bug in the code."
        )

        # Give "along track" an index
        self._ds["along_track"] = make_coordinate(
            arr=pd.RangeIndex(self._ds.along_track.size),
            name_str="along_track",
            attrs={"long_name": "Along track index"},
        )

        # Give "class" an index
        self._ds["class"] = make_coordinate(
            arr=[
                "Dust",
                "Sea_salt",
                "Continental_Pollution",
                "Smoke",
                "Dusty_smoke",
                "Dusty_mix",
                "Thin ice",
            ],
            name_str="class",
            attrs={"long_name": "Aerosol classes"},
        )

        # Give "layer" an index
        self._ds["layer"] = make_coordinate(
            arr=pd.RangeIndex(self._ds.layer.size),
            name_str="layer",
            attrs={"long_name": "Layer index"},
        )

        # Give "JSG_height" an index
        self._ds["JSG_height"] = make_coordinate(
            arr=pd.RangeIndex(self._ds.JSG_height.size),
            name_str="JSG_height",
            attrs={"long_name": "Joint scientific group height"},
        )

        # Create mean height
        self._ds["mean_height"] = self._ds.height.mean(dim="along_track")

        # Swap time with along track, and JSG_height with mean_height
        self._ds = self._ds.swap_dims(
            {"along_track": "time", "JSG_height": "mean_height"}
        )

    @property
    def ds(self) -> xr.Dataset:
        if self._ds is None:
            self._open_dataset()
            self._embellish_dataset()

        assert self._ds is not None

        return self._ds
