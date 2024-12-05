# Error handling in Python is done using the try, except, else, and finally blocks. These blocks help catch and manage exceptions (errors) that occur during the execution of the program.

# 1. try and except Blocks
# The try block is used to wrap code that might raise an exception.
# The except block catches the exception and lets you handle it without crashing the program.

# 2. Catching Multiple Exceptions
# You can handle multiple exceptions by specifying multiple except blocks or by using a tuple in a single except block.


try:
    # Code that might raise an exception
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
# 3. Using else Block
# The else block is executed if no exceptions are raised in the try block. This is useful for code that should only run when no errors occur.

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Can't divide by zero!")
except ValueError:
    print("Please enter a valid number!")
else:
    print(f"Result is: {result}")
# 4. Using finally Block
# The finally block will always run, whether an exception occurs or not. It's typically used for cleanup actions, such as closing files or releasing resources.


try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()  # This ensures that the file is always closed, even if an exception occurs
# 5. Catching All Exceptions
# You can catch all exceptions using the except block without specifying an exception type. However, this is generally not recommended, as it can hide bugs in the code.


try:
    # Some code that might raise any exception
    number = int(input("Enter a number: "))
except:
    print("An error occurred!")
# 6. Accessing Exception Information
# You can access the details of an exception using the as keyword. This gives you more information about the error that occurred.


try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
# 7. Custom Exceptions
# You can define your own exceptions by creating a class that inherits from the built-in Exception class.

class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Caught a custom error: {e}")

# 8. Raising Exceptions
# You can manually raise exceptions using the raise keyword. This is useful when you want to signal an error in your program.


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
# Summary of Key Concepts:
# try block: Code that might raise an exception.
# except block: Catches and handles the exception.
# else block: Executes code if no exception occurs.
# finally block: Executes code no matter what (for cleanup).
# Custom exceptions: Creating your own exceptions using class inheritance.
# Raising exceptions: Manually raising exceptions with raise.