__version__ = "v0.0.2"

import logging


def create_logger():
    return logging.getLogger("atlidreader")


def setup_logging_basic(level_str: str = "INFO"):
    # Setup the logging
    logging.basicConfig(
        level=level_str,
        datefmt="%Y/%m/%d %H:%M",
        format="%(asctime)s: [%(name)s:%(funcName)s:%(lineno)d] %(message)s",
    )
