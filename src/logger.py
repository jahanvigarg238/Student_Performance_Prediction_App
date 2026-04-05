import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)# this is the path where the log file will be created and stored. It combines the logs directory, the log file name, and the current working directory to create the full path for the log file.
os.makedirs(logs_path,exist_ok=True)# this line creates the logs directory if it does not exist. The exist_ok=True parameter allows the function to ignore the error if the directory already exists, preventing the program from crashing.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # this is the path where the log file will be created and stored. It combines the logs directory, the log file name, and the current working directory to create the full path for the log file.

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
