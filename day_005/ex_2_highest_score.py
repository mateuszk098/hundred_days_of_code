'''
You are going to write a program that calculates
the highest score from a List of scores.
'''

# Naive
# heights: list[str] = input().split()
# max_height: int = int(heights[0])

# for height in heights:
#     if max_height < int(height):
#         max_height = int(height)

# print(f"Maximal height: {max_height}")

# Another
heights: list[int] = list(map(int, input().split()))
result: int = max(heights)
print(f"Maximal height: {result}")
