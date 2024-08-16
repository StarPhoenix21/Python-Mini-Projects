# AdvanceRandomPasswordGenerator.py

import random
import string

def generatePassword(length: int, include_symbols: bool, min_alpha: int, min_num: int, min_sym: int) -> str:
    """Generate a random password based on user specifications."""
    if length < min_alpha + min_num + min_sym:
        raise ValueError("Password length must be at least the sum of minimum alpha, number, and symbol requirements.")
    
    characters = string.ascii_letters + string.digits
    # symbols = string.punctuation if include_symbols else ''
    # print(f"symbols: {symbols} {type(symbols)}")
    
    symbols = """!#$%&()*+-/:<=>?@[\]^_~""" if include_symbols else ''
    characters += symbols

    password = []
    password.extend(random.choices(string.ascii_letters, k=min_alpha))
    password.extend(random.choices(string.digits, k=min_num))
    password.extend(random.choices(symbols, k=min_sym))

    remaining_length = length - len(password)
    password.extend(random.choices(characters, k=remaining_length))

    random.shuffle(password)  # Shuffle to ensure random distribution of character types

    return ''.join(password)

def main():
    """Run the password generator application."""
    try:
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        length = int(input("Enter the password length: ").strip())
        min_alpha = int(input("Enter minimum number of alphabets: ").strip())
        min_num = int(input("Enter minimum number of numbers: ").strip())
        min_sym = int(input("Enter minimum number of symbols: ").strip())

        password = generatePassword(length, include_symbols, min_alpha, min_num, min_sym)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
