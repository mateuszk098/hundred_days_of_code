'''
You are going to write a program that calculates
the average student height from a List of heights.
'''

# Naive
# heights: list[str] = input().split()
# heights_sum: int = 0

# for height in heights:
#     heights_sum += int(height)

# result: float = heights_sum/len(heights)
# print(f"Average height: {result:.0f}")

# Another
heights: list[int] = list(map(int, input().split()))
result: float = sum(heights)/len(heights)
print(f"Average height: {result:.0f}")
