import logging
import os
from datetime import datetime
import sys


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE) #logs will be wrt current working directory and log names will start with logs and whatever the lOGFILE name comes
os.makedirs(log_path, exist_ok=True) #keep appending in the files 

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s/ - %(levelname)s - %(message)s",
    level= logging.INFO,

)

# if __name__ == "__main__":
#     try:
#         a= 1/0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e, sys)
#     # logging.info("Logging has started")
     
#%(asctime)s	Timestamp of log	[2024-02-02 14:30:45]
# %(lineno)d	Line number in script	12 (Where the log was created)
# %(name)s	Logger name	root/ (Default unless custom logger is used)
# %(levelname)s	Log level	INFO, ERROR, etc.
# %(message)s	Actual log message	"Something went wrong"