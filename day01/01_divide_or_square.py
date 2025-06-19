import math

def divide_or_square(num):
    if num % 5 == 0:
        return math.sqrt(num)
    else:
        return num % 5

# test cases
print(divide_or_square(25))

print(divide_or_square(7))

print(divide_or_square(10))