import random
import string

def generate_password(length, complexity):
    chars = string.ascii_letters
    if complexity > 1:
        chars += string.digits
    if complexity > 2:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

length = int(input("Enter password length: "))
complexity = int(input("Enter complexity (1 - letters, 2 - letters + numbers, 3 - letters + numbers + symbols): "))

print(f"Generated password: {generate_password(length, complexity)}")
