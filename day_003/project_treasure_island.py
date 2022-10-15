'''
Make your own "Choose Your Own Adventure" game. Use conditionals
such as if, else, and elif statements to lay out the logic and the 
story's path in your program.
'''


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You're at a crossroad. Where do you want to go? Type 'left' or 'right':")
choice: str = input()

if choice == "left":
    print("You've come to a lake. There is an island in the middle of the lake.\n"
          "Type 'wait' to wait for a boat. Type 'swim' to swim across:")
    choice = input()
    if choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.\n"
              "One red, one yellow and one blue. Which colour do you choose?")
        choice = input()
        if choice == "red":
            print("It's a room full of fire. Game Over.")
        elif choice == "yellow":
            print("You found the treasure! You Win!")
        elif choice == "blue":
            print("You enter a room of beasts. Game Over.")
    elif choice == "swim":
        print("You get attacked by an angry trout. Game Over.")
elif choice == "right":
    print("You fell into a hole. Game Over.")
