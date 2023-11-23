import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_letters if use_uppercase else string.ascii_lowercase
    characters += string.digits if use_digits else ''
    characters += string.punctuation if use_symbols else ''

    if not characters:
        return "Error: No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    print("Password Generator Preferences:")
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    return length, use_uppercase, use_digits, use_symbols

def save_password_to_file(password, filename='passwords.txt'):
    with open(filename, 'a') as file:
        file.write(password + '\n')

def main():
    length, use_uppercase, use_digits, use_symbols = get_user_preferences()

    num_passwords = int(input("Enter the number of passwords to generate: "))
    save_to_file = input("Save passwords to a file? (y/n): ").lower() == 'y'

    for _ in range(num_passwords):
        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print("Generated Password:", password)

        if save_to_file:
            save_password_to_file(password)

if __name__ == "__main__":
    main()