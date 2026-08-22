import random
import string

digit_values = string.digits
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
special_chars = string.punctuation

individuals = digit_values + lowercase_letters + uppercase_letters + special_chars
pass_len = 12
password = ""
for i in range(pass_len):
    password += random.choice(individuals)

print(f"Your Random Password is: {password}")
