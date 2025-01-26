import time


'''
Fixes:
    - Now checks number of '@' symbols
    - Now checks if characters come before and after the '@' symbol
    - Now checks position of '.'
'''

def addressVal(address):
    """
    Validates an email address.
    Ensures only one '@' is present, the '@' is the not the first char,
    there is atleast one '.' after the '@', and the '.' is not the last
    char in the email.
    
    Args:
        address (str): The email to be validated.
    Returns:
        str: "Valid" if the email is valid, an invalid message otherwise.
    """
    if '@' not in address or address.count('@') != 1:
        return "Invalid: Email must contain exactly one '@' symbol!"
    
    at_pos = address.find('@')
    dot_pos = address.find('.', at_pos)
    
    if at_pos == 0 or at_pos == len(address) - 1:
        return "Invalid: Characters must appear before or after the '@'!"
    
    if dot_pos == -1 or dot_pos == len(address) - 1 or dot_pos < at_pos + 2:
        return "Invalid: Dot must come after the '@'!"
    
    return "Valid"


print("This program will decide if your input is a valid email address")
while(True):
    x = input("Input your email address:")
    result = addressVal(x)
    print(result)
