# email has contain atleast one "." and only one "@"
# Email has not contain spaces


def addressVal(address):
    dot = address.find(".")
    at = address.find("@")
    at_count = address.count("@")

    if (
        dot >=1 
        and at > 0
        and at_count == 1 
        and " " not in address 
        and address.endswith("@gmail.com")):
        print("Valid Email")
    else:
        print("invalid Email")    

print("This program will decide if your input is a valid email address")
while(True):
    print("A valid email address needs an '@' symbol and a '.'")
    x = input("Input your email address:")

    addressVal(x)
