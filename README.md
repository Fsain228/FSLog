# FSLog - Simple Python Logging Library
This is my first Python logging library that helps you organize log messages with colorful output and log rotation.

Installation:
pip install fslog

How It Works?

Initialization:
from fslog import FSLog

logger = FSLog(
    log_folder_path="/Logs",  # Path to your log folder (default: "/Logs")
    max_logs=5              # Maximum number of log files to keep
)

Basic Usage:
logger.logging("Hello world!")

Output:
[2023-11-15 14:30:00] [LOGGING] Hello world!

Custom Colors (RGB)
logger.logging("Hello world!", (0, 255, 0))  # Green text

Log Levels:

Method	     Default Color	Example
.debug()	Cyan	    logger.debug("Message")
.info()	        Blue	    logger.info("Message")
.logging()	White	    logger.logging("Message")
.server()	White	    logger.server("Message")
.warning()	Yellow	    logger.warning("Message")
.error()	Red	    logger.error("Message")
.custom()	Custom	    See below

Custom Prefixes:
logger.custom("Hello world!", "MY_PREFIX", (255, 0, 255))  # Purple text

Output:
[2023-11-15 14:30:00] [MY_PREFIX] Hello world!

Log Rotation
When the number of log files exceeds max_logs, the oldest files are automatically deleted.

Advanced Features
# Enable debug mode to see internal calls
logger.lib_debug("on")

# Get logging statistics
logger.logging_stats()  # Shows: current log file, file count, size

Requirements
Python 3.8+
No external dependencies