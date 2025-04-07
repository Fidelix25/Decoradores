from loguru import logger

logger.debug("Dev warning")
logger.info("Process important information")
logger.warning("Something will happen in the future")
logger.error("A fail occured")
logger.critical("A fail that stops the app occured")
