import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

if length < 1:
    print("Please enter a valid length!")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Your generated password is:", password)