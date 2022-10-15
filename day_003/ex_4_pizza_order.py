'''
Based on a user's order, work out their final bill. 
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''

print("Welcome to Python Pizza Deliveries!")

size: str = input("What size pizza do you want? S, M, or L: ")
add_pepperoni: str = input("Do you want pepperoni? Y or N: ")
extra_cheese: str = input("Do you want extra cheese? Y or N: ")
final_bill: int = 0

if size == 'S':
    final_bill += 15
    if add_pepperoni == 'Y':
        final_bill += 2
elif size == 'M':
    final_bill += 20
    if add_pepperoni == 'Y':
        final_bill += 3
else:
    final_bill += 25
    if add_pepperoni == 'Y':
        final_bill += 3

if extra_cheese == 'Y':
    final_bill += 1

print(f"Your final bill is: ${final_bill}")
