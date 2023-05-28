"""Main functions"""

import re

def is_palindrome(string: str) -> bool:
    """Check if string is palindrome."""
    string = string.lower().replace(" ", "")
    string = re.sub(r'[^\w\s]','',string)
    string_inversa = string[::-1]

    if string == string_inversa:
        return True
    else:
        return False


