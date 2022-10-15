'''
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times 
the letters in the word TRUE occurs. Then check for the number 
of times the letters in the word LOVE occurs. Then combine these 
numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
'''

print("Welcome to the Love Calculator!")

name1: str = input("What is your name? \n").lower()
name2: str = input("What is their name? \n").lower()
combined_name: str = name1 + name2

tt: int = combined_name.count('t')
tr: int = combined_name.count('r')
tu: int = combined_name.count('u')
te: int = combined_name.count('e')

ll: int = combined_name.count('l')
lo: int = combined_name.count('o')
lv: int = combined_name.count('v')
le: int = combined_name.count('e')

score: int = int(str(tt + tr + tu + te) + str(ll + lo + lv + le))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
