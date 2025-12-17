import random
import string

print("🔐 Password Generator")

# user chooses length
length = int(input("Enter password length: "))

# characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# generate password
password = ""

for i in range(length):
    password += random.choice(characters)

print("✅ Generated Password:", password)
