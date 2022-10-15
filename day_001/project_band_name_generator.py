'''
Write a program where you:
- create a greeting for your program,
- ask the user for the city that they grew up in,
- ask the user for the name of a pet,
- combine the name of their city and pet and show them their band name,
- make sure the input cursor shows on a new line.
'''

print("Welcome to the Band Name Generator.")
my_city: str = input("What's name of your city you grew up in?\n").strip()
my_pet: str = input("What's your pet's name?\n").strip()
print(f"Your band name could be {my_city} {my_pet}.")
