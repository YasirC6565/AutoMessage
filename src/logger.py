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
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M")
    # print the time and the message
    print(f"[{timestamp}] '{message}'")




