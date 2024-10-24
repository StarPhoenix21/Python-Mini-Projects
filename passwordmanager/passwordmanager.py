from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import csv
import os
import getpass

# Step 1: Derive encryption key from master password
def derive_key_from_password(master_password, salt):
    # PBKDF2 with SHA-256
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

# Step 2: Encrypt the password
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Step 3: Decrypt the password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Step 4: Store encrypted password in CSV file
def store_password(site, username, password, master_password):
    salt = os.urandom(16)  # Random salt for key derivation
    key = derive_key_from_password(master_password, salt)
    encrypted_password = encrypt_password(password, key)

    with open('passwords.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([site, username, encrypted_password.decode(), base64.b64encode(salt).decode()])

# Step 5: Retrieve and decrypt password from CSV file
def retrieve_password(site, username):
    # Ask for master password at the time of retrieval
    master_password = getpass.getpass("Enter your master password: ")

    with open('passwords.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == site and row[1] == username:
                encrypted_password = row[2].encode()
                salt = base64.b64decode(row[3].encode())
                key = derive_key_from_password(master_password, salt)
                try:
                    decrypted_password = decrypt_password(encrypted_password, key)
                    return decrypted_password
                except Exception as e:
                    print(f"Error decrypting password: {e}")
                    return None
    return None

# Step 6: Menu-driven application for user interaction
def menu():
    while True:
        print("\nPassword Manager")
        print("1. Store new password")
        print("2. Retrieve password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # For storing passwords, master password is asked once
            master_password = getpass.getpass("Enter your master password: ")
            site = input("Enter the website or application name: ")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            store_password(site, username, password, master_password)
            print(f"Password for {site} saved.")
        
        elif choice == '2':
            # For retrieving, master password is asked every time
            site = input("Enter the website or application name: ")
            username = input("Enter your username: ")
            password = retrieve_password(site, username)
            if password:
                print(f"Password for {site}: {password}")
            else:
                print(f"No password found for {site} with username {username}.")

        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the password manager
if __name__ == "__main__":
    menu()
