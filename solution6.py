# Type casting in Python is the process of converting one data type to another. This can be done using built-in functions like int(), float(), str(), etc.

# Converting integer to string
num = 10
num_str = str(num)
print("Type of num_str:", type(num_str))  # Output: <class 'str'>

# Converting string to integer
num_str = "25"
num_int = int(num_str)
print("Type of num_int:", type(num_int))  # Output: <class 'int'>

# Converting float to integer
num_float = 9.8
num_int_from_float = int(num_float)
print("Value of num_int_from_float:", num_int_from_float)  # Output: 9

# Converting integer to float
num = 7
num_float_from_int = float(num)
print("Value of num_float_from_int:", num_float_from_int)  # Output: 7.0