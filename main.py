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

#texto = input(str("Digite uma string: "))

"""def is_palindrome(string: str) -> bool:
    string = string.strip().lower().isalnum()
    letras = string.split()
    letras_juntas = ''.join(letras)
    if letras_juntas == letras_juntas[::-1]:
        return True
    else:
        return False
    
    Check if string is palindrome."""
    
    #return False





