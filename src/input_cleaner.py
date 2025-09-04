"""
input_cleaner.py
----------------
Responsible for cleaning and preprocessing incoming text messages
from WhatsApp or email before passing them to the retriever or tool router.

Functions to implement:
- clean_text(raw_message: str) -> str
    Removes unwanted characters, normalizes whitespace,
    and ensures consistent casing.
"""

# function that is expecting a string, if its none then it returns an empty string
def clean_text(raw_message:str) -> str:
    if raw_message is None:
        return " "

    # Makes the input to a string
    raw_message = str(raw_message)

    #this replaces any new line with a space and replaces any tab with a space

    cleaned = raw_message.replace("\n", " ").replace("\t", " ")


    #so now we have the value of the cleaned from above so raw message again isnt needed again. So now the value of cleaned is override and it is split then joined back together
    cleaned = " ".join(cleaned.split())

    #gets it to lowercase
    cleaned = cleaned.lower()

    return cleaned







