from pathlib import Path

from atlidreader.readers.core import ReaderProtocol
from atlidreader.readers.atlid2a import AAER2AReader

from typing import Type


class ReaderFactoryNoReader(Exception):
    """Raised if there is no reader matching
    a specific file."""

    def __init__(self, err_str: str):
        super().__init__(err_str)


class ReaderFactory:
    """Covenience class to find a reader
    for a file."""

    def __init__(self):
        self._reader_class_lst: list[Type[ReaderProtocol]] = [AAER2AReader]

    def get_reader(self, fileP: str | Path) -> Type[ReaderProtocol]:
        """Get a reader that matches the given
        file.

        Raises
        ------
        ReaderFactoryNoReader:
            Raised if there is no reader
            matching the given file.
        """

        select_reader_class: Type[ReaderProtocol] | None = None

        for reader_class in self._reader_class_lst:
            if reader_class.match_file_name(fileP) is True:
                select_reader_class = reader_class
                break

        if select_reader_class is None:
            raise ReaderFactoryNoReader(
                "Could not find a matching reader " f"for the file {fileP}"
            )

        return select_reader_class
