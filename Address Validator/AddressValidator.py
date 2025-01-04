import re


def addressVal(address: str) -> None:
    address_pattern: str = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(address_pattern, address):
        print("Valid")
    else:
        print("Invalid")


print("This program will decide if your input is a valid email address")
while True:
    print("A valid email address should look like 'example@gmail.com'")
    address = input("Input your email address:")
    addressVal(address)
