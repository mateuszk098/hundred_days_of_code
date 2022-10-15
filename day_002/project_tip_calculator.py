'''
Write a code which calculate how much should pay
each of person for the bill, including tip.
'''

print('Welcome to the tip calculator!')

bill_amount: float = float(input('What was the total bill? $'))
tip_percent: int = int(input('How much tip would you like to give? 10, 12, or 15? '))
people_number: int = int(input('How many people to split the bill? '))

final_amount: float = (bill_amount/people_number) * (1 + tip_percent/100)
print(f'Each person should pay: ${final_amount:.2f}')
