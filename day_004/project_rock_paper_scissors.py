'''
Make a rock, paper, scissors game. 
Inside the file, you'll find the ASCII art for the hand signals
already saved to a corresponding variable: `rock`, `paper`, and `scissors`.
This will make it easy to print them out to the console. 
'''

import random

rock: str = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper: str = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors: str = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice: int = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choice: int = random.randint(0, 2)
choices: list[str] = [rock, paper, scissors]

print(f'USER:\n{choices[user_choice]}')
print(f'COMPUTER:\n{choices[computer_choice]}')

if user_choice == computer_choice:
    print('IT IS A DRAW!')
elif user_choice == 0 and computer_choice == 2:
    print('YOU WIN!')
elif user_choice == 2 and computer_choice == 0:
    print('YOU LOSE!')
elif user_choice > computer_choice:
    print('YOU WIN!')
elif user_choice < computer_choice:
    print('YOU LOSE!')
