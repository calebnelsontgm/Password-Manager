# CLI that ties everything together

from encryptdecrypt import derive_key, encrypt_password, decrypt_password
from verify import hash_master_password, check_master_password
from storage import init_storage, add_entry, load_storage

import base64

import os

if not os.path.exists("passwords.json"):
    master_password = input("Create a master password: ") # Prompt the user to create a master password
    master_hash = hash_master_password(master_password) # Hash the master password using the function from verify.py
    salt = base64.urlsafe_b64encode(os.urandom(16)).decode('utf-8') # generate a random salt
    init_storage(master_hash, salt) # Initialize the storage with the master hash and salt using the function from storage.py
    key = derive_key(master_password, base64.urlsafe_b64decode(salt))
    print("Master password set and storage initialized.") # Inform the user that the master password has been set and storage initialized
else:
    stored_data = load_storage() # Load the existing storage data using the function from storage.py
    master_password = input("Enter your master password: ") # Prompt the user to enter their master password
    if(not check_master_password(master_password, stored_data["master_hash"])):
        print("Incorrect master password. Exiting.")
        exit(1)
    key = derive_key(master_password, base64.urlsafe_b64decode(stored_data["salt"])) # Derive the encryption key using the master password and salt from storage.py 
    
while True:
    print("\n1. Add a password")
    print("2. Retrieve a password")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        sitename = input("Enter the site name: ")
        username = input("Enter the username: ")
        plaintext_password = input("Enter the password: ")
        encrypted_password = encrypt_password(plaintext_password, key) # Encrypt the password using the function from encryptdecrypt.py
        add_entry(sitename, username, encrypted_password) # Add the entry to storage using the function from storage.py
        print("Password added successfully.")
    elif choice == "2":
        # retrieve
        sitename = input("Enter the site name to retrieve: ")
        entries = load_storage()["entries"] # Load the entries from storage
        for entry in entries:
            if entry["sitename"] == sitename:
                decrypted_password = decrypt_password(entry["encrypted_password"], key) # Decrypt the password using the function from encryptdecrypt.py
                print(f"Username: {entry['username']}, Password: {decrypted_password}")
                break
        else:
            print("Site not found.")
    elif choice == "3":
        break
    else:
        print("Invalid option.")