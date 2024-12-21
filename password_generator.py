import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lower + upper + digits + symbols

    if length < 4:
        print("Password length should be at least 4 to ensure trhe complexity.")
        return None

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

while True:
    try:
        length = int(input("Enter the desired password length (or type 0 to exit): "))
        if length == 0:
            print("Exiting the program!")
            break

        generated_password = generate_password(length)

        if generated_password:
            print(f"Generated Password is: {generated_password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
