'''
Write a program that interprets the Body Mass Index (BMI)
based on a user's weight and height. It should tell them the 
interpretation of their BMI based on the BMI value.
- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.
'''

user_weight: float = float(input('Enter your weight in kg: '))
user_height: float = float(input('Enter your height in m: '))
user_bmi_index: float = user_weight/(user_height*user_height)
user_bmi_index = round(user_bmi_index)
result: str = ""

if user_bmi_index < 18.5:
    result = f"Your BMI is {user_bmi_index}, you are underweight."
elif 18.5 <= user_bmi_index < 25.0:
    result = f"Your BMI is {user_bmi_index}, you have a normal weight."
elif 25.0 <= user_bmi_index < 30.0:
    result = f"Your BMI is {user_bmi_index}, you are slightly overweight."
elif 30.0 <= user_bmi_index < 35.0:
    result = f"Your BMI is {user_bmi_index}, you are obese."
else:
    result = f"Your BMI is {user_bmi_index}, you are clinically obese."

print(result)
