import logging

logger = logging.getLogger("Application Logs")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger.handlers[0].setFormatter(formatter)
