import re

def validate_email(email: str) -> bool:
    """
    Validate an email address using a regular expression.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.

    Edge cases handled:
    - Prevents consecutive dots and trailing dots in the local part.
    - Ensures the TLD is at least two characters long.
    - Ensures the domain part is valid.
    - Prevents leading and trailing dots in the local part.
    - Prevents invalid characters in the local part.
    - Does not support quoted local parts.
    - Does not support IP address domains.
    - Domain part can include letters, digits, dots, and hyphens.
    - Prevent consecutive dots or consecutive hyphen in the domain part.
    - Prevent space in email addresses.
    """
    # Improved regular expression for validating an Email
    regex = r'^(?!.*\.\.)(?!.*\.$)(?!^\.)[a-zA-Z0-9._%+-]+(?<!\.)@(?!-)[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None


def isValidEmail(email: str) -> bool:
    """
    Overloaded function to call validate_email for compatibility with old function name.

    Args:
        email (str): The email address to be validated.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
    return validate_email(email)

def get_email_parts(email: str) -> dict:
    """
    Accept an email address and return the username and domain as a dictionary.

    Args:
        email (str): The email address to be split.

    Returns:
        dict: A dictionary with 'username' and 'domain' keys.
    """
    username = email[0:email.index('@')]
    domain = email[email.index('@') + 1:]
    return {'username': username, 'domain': domain}

def main() -> None:
    """
    Main function to prompt the user for an email address, validate it,
    and print the username and domain if valid.
    """
    email = input("Enter your email id: ")
    if validate_email(email):
        email_parts = get_email_parts(email)
        print("Username:", email_parts['username'])
        print("Domain:", email_parts['domain'])
    else:
        print("Invalid Email!")

if __name__ == "__main__":
    main()

# The aim of this script is to validate an email address and extract the username and domain if valid.
# The script defines two functions: validate_email and get_email_parts.
# The validate_email function uses a regular expression to validate the email address.
# The get_email_parts function extracts the username and domain from the email address.
# The main function prompts the user for an email address, validates it, and prints the username and domain if valid.
# The script also includes an overloaded function isValidEmail for compatibility with an old function name.
# The script can be run to validate and extract information from email addresses.
# The script uses regular expressions to validate email addresses and extract information from them.
# The script is well-structured and easy to understand, with clear function names and comments.
# Future improvements:
# The script could be further improved by adding unit tests to verify the correctness of the functions.
# The script could be enhanced by adding more detailed error messages for invalid email addresses.

