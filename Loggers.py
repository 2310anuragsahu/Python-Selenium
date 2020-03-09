import logging

logging.basicConfig(filename="test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug")
logger.info("This is error")
logger.warning("This is warning")
logger.error("This is error")
logger.critical("This is critical")