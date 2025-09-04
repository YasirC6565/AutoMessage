"""
logger.py
---------
Provides simple logging utilities for debugging.

Functions to implement:
- log(message: str) -> None
    Prints timestamped logs to the console (later can be replaced with proper logging).
"""

from datetime import datetime

def log(message: str) -> None:
    # get the current time
    timestamp = datetime.now()

    # print the time and the message
    print(f"[{timestamp}] {message}")


#testing code
from logger import log

# Try logging different messages
log("Program started")
log("Loading input cleaner")
log("Process finished successfully")
