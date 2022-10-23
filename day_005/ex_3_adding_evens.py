'''
You are going to write a program that calculates the sum
of all the even numbers from 1 to 100. Thus, the first even
number would be 2 and the last one is 100.
'''

# Naive
# result: int = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         result += number
# print(result)

# Notice we can use math formula
result: float = 100/2*(100/2+1)
print(result)
