# Stores a single password entry in a dictionary
# Read/write JSON, manage entries

import json
import os

filename = "passwords.json"

def init_storage(master_hash, salt): #  creates the JSON file on first run

    someDictionary = {
        "master_hash": master_hash,
        "salt": salt,
        "entries": []
    }

    with open(filename, 'w') as file:
        json.dump(someDictionary, file)

def add_entry(sitename, username, encrypted_password): #  appends to entries

# Call load_storage() to get the existing data

    data = load_storage()

    # Build a dictionary with sitename, username, encrypted_password
    addedDictionary = {
        "sitename": sitename,
        "username": username,
        "encrypted_password": encrypted_password
    }

    # Append it to data["entries"]
    data["entries"].append(addedDictionary)

    # Write the whole thing back to the file
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_storage(): # reads and returns the JSON data
    with open(filename, 'r') as file:
        all_data = json.load(file)
    return all_data

