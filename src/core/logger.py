import logging
from pathlib import Path

from config import LOG_DIR

LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    fh = logging.FileHandler(LOG_DIR / "pipeline.log")

    sh = logging.StreamHandler()

    fh.setFormatter(formatter)

    sh.setFormatter(formatter)

    logger.addHandler(fh)

    logger.addHandler(sh)

    return logger