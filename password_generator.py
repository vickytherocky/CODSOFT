import random
import string
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    password = [
        random.choice(upper_case),
        random.choice(lower_case),
        random.choice(digits),
        random.choice(special_chars)
    ]

    all_characters = upper_case + lower_case + digits + special_chars
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
