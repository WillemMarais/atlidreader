import typer
from pathlib import Path

from atlidreader.readers.factory import ReaderFactory
from atlidreader import create_logger, setup_logging_basic

from typing import Optional

log_obj = create_logger()

app = typer.Typer()


@app.callback()
def cli(
    log_level_str: str = typer.Option(
        "INFO", "--log-level", "-l", help="Python log level."
    )
):
    setup_logging_basic(level_str=log_level_str)


@app.command("convert")
def convert(
    file_path: Path = typer.Argument(help="The ATLID H5 file path."),
    out_file_path: Optional[Path] = typer.Argument(
        None,
        help=(
            "The netcdf4 output file path. If not given then the "
            "netcdf4 file will be written to the same directory as "
            "the given ATLID H5 file."
        ),
    ),
):
    if out_file_path is None:
        out_file_path = file_path.parent / (file_path.stem + ".nc")

    # Create reader factory
    reader_factory = ReaderFactory()

    # Get the reader class
    reader_class = reader_factory.get_reader(file_path)

    # Create the reader
    reader = reader_class(file_path)

    # Write to netcdf4
    out_file_path.parent.mkdir(exist_ok=True, parents=True)
    log_obj.info(f"Writing netcdf4 file to {out_file_path}")
    reader.ds.to_netcdf(out_file_path)
