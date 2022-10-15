'''
Write a program that calculates the Body Mass Index (BMI)
from a user's weight and height.
'''

user_weight: float = float(input('Enter your weight in kg: '))
user_height: float = float(input('Enter your height in m: '))
user_bmi_index: float = user_weight/(user_height*user_height)
print(f"{user_bmi_index:.2f}")
