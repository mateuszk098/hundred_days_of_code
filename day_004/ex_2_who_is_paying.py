'''
You are going to write a program which will select a random
name from a list of names. The person selected will have
to pay for everybody's food bill.
'''

import random

names_string: str = input("Give me everybody's names, separated by a comma:\n")
names: list[str] = names_string.split(", ")
choice: int = random.randint(0, len(names) - 1)
print(names[choice])
