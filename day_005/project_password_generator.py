'''
Write a program which automatically generates a password.
'''

import random

numbers: list[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols: list[str] = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Welcome to the PyPassword Generator!")
nr_letters: int = int(input("How many letters would you like in your password?\n"))
nr_symbols: int = int(input(f"How many symbols would you like?\n"))
nr_numbers: int = int(input(f"How many numbers would you like?\n"))

password_list: list[str] = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Randomize this
random.shuffle(password_list)
password: str = ''.join(password_list)

print(f'Your password: {password}')
