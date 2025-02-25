import logging 
import os

from from_root import from_root
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" 
LOGS_DIR=os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(LOGS_DIR, exist_ok=True) # create logs directory

LOG_FILE_PATH=os.path.join(LOGS_DIR, LOG_FILE) # create log file

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG # logging.INFO 
) 