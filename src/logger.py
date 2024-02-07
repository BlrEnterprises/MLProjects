import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    level=logging.INFO
)

if __name__=="++main__":
    try:
        a=1/0

    except Exception as e:
        logging.info("Logging have started for the above.")
        raise CustomException(e,sys)