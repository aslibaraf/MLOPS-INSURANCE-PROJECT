from src.logger import logging
from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1+'Z'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e