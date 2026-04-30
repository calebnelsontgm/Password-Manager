# Fernet encrypt/decrypt + key derivation from master password

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64


 # returns a Fernet-ready key
def derive_key(master_password, salt):
    password_bytes = master_password.encode('utf-8') # encoding the master password to bytes
    kdf = PBKDF2HMAC(   # kdf is now a configured object ready to derive
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000
    )
    raw_key = kdf.derive(password_bytes) # deriving the raw bytes
    key = base64.urlsafe_b64encode(raw_key) #encode it with base64
    return key


# returns a storable string token
def encrypt_password(plaintext, key):
    f = Fernet(key) # create Fernet object with key
    plaintext = plaintext.encode('utf-8') # encode the plaintext to bytes
    token = f.encrypt(plaintext) # encrypt the plaintext, resulting in a token (bytes)
    return token.decode('utf-8') # decode the token to a string for storage



# returns the original plaintext string
def decrypt_password(token, key):
    f = Fernet(key) # create Fernet object with key
    decrypted_bytes = f.decrypt(token) # decrypt the token, resulting in bytes
    plaintext = decrypted_bytes.decode('utf-8') # decode the bytes back to a string
    return plaintext  