import random
import string

# Prompt user for password length
length = int(input("Enter the desired password length: "))

# Character sets for complexity
letters = string.ascii_letters   # a-z, A-Z
digits = string.digits           # 0-949
symbols = string.punctuation     # !@#$%^&*()...

# Combine all character sets
all_chars = letters + digits + symbols

# Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))

# Display the password
print(f"Generated Password: {password}") 