import logging
import logging.handlers
from .config import settings
import sys


def setup_logging():
    logger = logging.getLogger(settings.PROJECT_NAME)
    logger.setLevel(logging.getLevelName(settings.LOG_LEVEL))

    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.handlers.RotatingFileHandler(
        "app.log", maxBytes=10240, backupCount=4
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(messages)s"
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


logger = setup_logging()
