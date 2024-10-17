def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Calling the function with different numbers of arguments
print(add_numbers(1, 2))         # Output: 3
print(add_numbers(1, 2, 3, 4))   # Output: 10
