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


#Seeing if it works

from input_cleaner import clean_text

# Test 1: Normal messy text
msg1 = "   HELLO   World!!   \nThis is\tan Example "
print("Test 1:", clean_text(msg1))

# Test 2: Input is None
msg2 = None
print("Test 2:", clean_text(msg2))

# Test 3: Input is not a string (number)
msg3 = 12345
print("Test 3:", clean_text(msg3))

# Test 4: Already clean text
msg4 = "python is fun"
print("Test 4:", clean_text(msg4))





