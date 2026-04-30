# Secure Password Manager

A terminal-based password manager built in Python that uses real encryption to store and retrieve passwords securely.

## Features

- Master password authentication using bcrypt one-way hashing
- Stored passwords encrypted with AES-128 via the Fernet symmetric encryption scheme
- Encryption key derived from the master password using PBKDF2-HMAC-SHA256 — the key is never stored anywhere
- Secure password generator using Python's `secrets` module
- JSON-based local storage

## How It Works

The master password is hashed with bcrypt and never stored in plaintext. When you log in, your master password is run through a Key Derivation Function (PBKDF2) along with a stored salt to re-derive the encryption key on the fly. This key is used to encrypt and decrypt your saved passwords via Fernet. Without the correct master password, the stored passwords are unreadable.

## Project Structure

```
main.py            # Entry point and CLI
encryptdecrypt.py  # Key derivation, encryption, decryption
verify.py          # Master password hashing and verification
storage.py         # JSON read/write and entry management
generator.py       # Secure password generation
```

## Setup

1. Clone the repository
2. Install dependencies:
```
pip install cryptography bcrypt
```
3. Run the program:
```
python main.py
```

On first run you will be prompted to create a master password. After that, your master password is required every time you open the manager.

## Security Notes

- The master password is hashed with bcrypt (cost factor 12)
- The encryption key is derived using PBKDF2-HMAC-SHA256 with 480,000 iterations
- A random 16-byte salt is generated on first run and stored alongside the encrypted entries
- The raw encryption key is never written to disk

## Dependencies

- [cryptography](https://pypi.org/project/cryptography/)
- [bcrypt](https://pypi.org/project/bcrypt/)