#MichaelNyembo, Fri 9 Aug 10:30

import random
import string

print("*********** PASSWORD GENERATOR ******************\n")

print("Rules for creating a good and secure password:")
print("- Length should be between 12 to 16 characters.")
print("- Must include at least one uppercase letter (A-Z).")
print("- Must include at least one lowercase letter (a-z).")
print("- Must include at least one digit (0-9).")
print("- Must include at least one special character (e.g., !, @, #, $, etc.).")
print("- Should not follow common patterns or sequences.\n\n")

quit = ""

def Generator():
    while True:
        length = input("Enter the length of the password to generate (Should be between 12-16): ")
        if not length.isdigit():
            print("Please enter a valid number.")
            continue
        length = int(length)
        if length < 12 or length > 16:
            print("The length should be between 12-16.")
        else:
            UpperCase_pool = string.ascii_uppercase
            LowerCase_pool = string.ascii_lowercase
            Number_pool = string.digits
            Characters_pool = string.punctuation


            Random_password = [
                random.choice(UpperCase_pool),
                random.choice(LowerCase_pool),
                random.choice(Number_pool),
                random.choice(Characters_pool),
            ]

            allCharacters = UpperCase_pool + LowerCase_pool + Number_pool + Characters_pool
            Random_password += random.choices(allCharacters, k=length - len(Random_password))

            random.shuffle(Random_password)

            password = ''.join(Random_password)

            print(f"Generated Password: {password}\n")
            break

while quit != 'q':
    Generator()
    quit = input("Press 'q' to quit or any other key to generate another password: ")
