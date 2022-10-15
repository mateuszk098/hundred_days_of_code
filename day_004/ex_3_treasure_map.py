'''
You are going to write a program which will mark a spot with an X.
'''

row1: list[str] = ["_", "_", "_"]
row2: list[str] = ["_", "_", "_"]
row3: list[str] = ["_", "_", "_"]
my_matrix: list[list[str]] = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position: str = input("Where do you want to put the treasure? ")
pos_row: int = int(position[0])
pos_col: int = int(position[1])
my_matrix[pos_row][pos_col] = 'X'

print(f"{row1}\n{row2}\n{row3}")
