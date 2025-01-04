import re

def isValidEmail(email):

    # Regular expression for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

email = input("Enter your email id - ")

if isValidEmail(email):
    username, domain = email.split('@')
    print("Username - ", username)
    print("Domain - ", domain)
else:
    print("Invalid Email!")