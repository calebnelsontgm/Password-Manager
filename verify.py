# This one basically hashes a password and verifies additional inputs only depending on that specific hash
# one way encryption
# Master password hashing + checking

import bcrypt


# 1. Obtain password

def hash_master_password(master_password):
    data = master_password.encode('utf-8')
    # 2. Convert to bytes
    hash = bcrypt.hashpw(data, bcrypt.gensalt(12))
    stringhash = hash.decode('utf-8') # Storing hash as a string
    return stringhash

def check_master_password(master_Password, stored_hash):
    return bcrypt.checkpw(master_Password.encode('utf-8'), stored_hash.encode('utf-8'))
