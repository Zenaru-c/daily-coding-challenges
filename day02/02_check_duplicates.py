
def check_duplicates(str_list):
    seen = set()
    duplicates = set()

    for item in str_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    if duplicates:
        return list(duplicates)
    else:
        return "no duplicates"

# test cases
print(check_duplicates(['apple', 'orange', 'banana', 'apple']))
print(check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark']))
