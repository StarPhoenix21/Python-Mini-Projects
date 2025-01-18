import re
import dns.resolver  
import idna

# List of disposable email domains
disposable_domains = [
    "mailinator.com",
    "10minutemail.com",
    "guerrillamail.com",
    "throwawaymail.com",
    "getnada.com",
    "maildrop.cc",
    "temp-mail.com",
    "fakemailgenerator.com",
    "yopmail.com",
    "jetable.com"
]

# Regular expression for basic email syntax validation
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    """
    Validates an email address through multiple checks.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Check if the email contains '@'
    if '@' not in email:
        return False
    
    # Split the email into local and domain parts
    try:
        local_part, domain_part = email.split('@')
    except ValueError:
        return False

    # Check length constraints for local and domain parts
    if len(local_part) > 64 or len(domain_part) > 255 or len(email) > 320:
        return False

    # Perform basic syntax validation
    if not re.match(email_regex, email):
        return False

    # Check if the domain is a disposable email domain
    if is_disposable_domain(domain_part):
        return False

    # Validate the domain using DNS MX records
    if not is_valid_domain(domain_part):
        return False

    # Validate if the domain supports internationalized domain names (IDNs)
    if not validate_international_email(domain_part):
        return False

    return True

def is_valid_domain(domain):
    """
    Checks if the domain has valid MX records.
    
    Args:
        domain (str): The domain to check.
    
    Returns:
        bool: True if the domain has valid MX records, False otherwise.
    """
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return len(mx_records) > 0
    except Exception:
        return False

def validate_international_email(domain):
    """
    Validates that the domain supports internationalized domain names (IDNs).
    
    Args:
        domain (str): The domain to validate.
    
    Returns:
        bool: True if the domain supports IDNs, False otherwise.
    """
    try:
        idna.encode(domain).decode('utf-8')
        return True
    except idna.IDNAError:
        return False

def is_disposable_domain(domain):
    """
    Checks if the email domain belongs to a disposable domain.
    
    Args:
        domain (str): The domain to check.
    
    Returns:
        bool: True if the domain is disposable, False otherwise.
    """
    return domain in disposable_domains

if __name__ == "__main__":
    email_input = input("Enter your email address: ")
    if is_valid_email(email_input):
        print("The email address is valid.")
    else:
        print("The email address is invalid.")
