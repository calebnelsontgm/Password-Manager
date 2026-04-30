# password generator that will create strong passwords automatically

import secrets
import string

letters = string.ascii_letters
digits = string.digits
symbols ="!@#$%^&*()_+/|.,`~"

all_chars = letters + digits + symbols

password = ''.join(secrets.choice(all_chars) for i in range(20))
print(password)