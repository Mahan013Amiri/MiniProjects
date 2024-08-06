import random, string

lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = "0123456789"
characters = "!@#$%^&*()_+-="
all = lower_letters + upper_letters + numbers + characters
password = ""
for i in range(8):
    password += random.choice(all)
print(password)
