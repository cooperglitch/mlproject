#Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred. An event is described by a descriptive message which can optionally contain variable data (i.e. data that is potentially different for each occurrence of the event). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
#datetime.now(): This gets the current date and time.
#.strftime('%Y-%m-%d_%H-%M-%S'): This formats the datetime object into a specific string format.

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)
#The primary goal of these two lines is to create a dedicated directory for your log files if it doesn't already exist, and to construct the full, correct path to your new log file within that directory.

LOG_FILE_PATH = logs_path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
#The logging.basicConfig() function is a convenience function provided by Python's logging module. It's designed for simple, quick configurations of the root logger.
#"Root Logger": Python's logging system has a hierarchy. At the very top is the "root logger." By default, all other loggers you create in your application will inherit settings from the root logger unless you explicitly configure them otherwise. basicConfig modifies this root logger.
# When you call basicConfig(), it essentially does two main things:It creates a handler (a component that sends log records to a specific destination, like a file or the console).It creates a formatter (a component that defines the layout of the log records) and attaches it to the handler.It sets the level for the root logger.
