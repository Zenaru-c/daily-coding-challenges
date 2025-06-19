
fruits = {'fruit': 'apple', 'color': 'green'}

def longest_value(fruits):
    max_val = max(fruits.values(), key=len)
    return max_val

print(longest_value(fruits))
