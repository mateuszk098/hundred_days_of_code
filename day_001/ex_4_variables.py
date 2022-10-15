'''
Write a program that switches the values stored in the variables a and b.
'''

a: float = float(input('a: '))
b: float = float(input('b: '))

a = a*b
b = a/b
a = a/b

print(f"a: {a}")
print(f"b: {b}")
