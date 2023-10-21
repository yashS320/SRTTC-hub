import random
import string

#character set by adding or removing characters as needed
custom_characters = string.ascii_letters + string.digits + string.punctuation

#minimum required characters
min_digits = 2
min_letters = 3
length = 12  #length of the password as needed

#2 digits and 3 alphabet characters
password = random.choices(string.ascii_letters, k=min_letters) + random.choices(string.digits, k=min_digits) + random.choices(custom_characters, k=length - (min_digits + min_letters))

#characters to randomize the password
random.shuffle(password)

#string
password = ''.join(password)

print(password)
