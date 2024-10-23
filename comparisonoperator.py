# Write a Python program to check if two numbers, a = 5 and b = 10, are equal.
a=5
b=10
print(a==b)

# Check if a = 8 is greater than b = 3.
a=8
b=3
print(a>b)

# Verify if the number 15 is less than 20.
number=15
print(number<20)

# Write a Python program that takes two variables, x = 12 and y = 25, and prints the larger number.
x = 12
y = 25
if x < y:
    print("y is larger")
elif x > y:
    print("x is larger")
else:
    print("Both are equal")


# Determine if a number n = 18 is both greater than 10 and less than 20.
n = 18
if n > 10 and n < 20:
    print("n is between 10 and 20")
else:
    print("n is not between 10 and 20")
# another way
n=18
print(n>10 and n<20)

# Compare two strings "apple" and "banana" using the > operator.
string1="apple"
string2="banana"
print(string1>string2)

# Compare two floating-point numbers a = 0.1 + 0.2 and b = 0.3. Why does a == b return False?
a = 0.1 + 0.2
b = 0.3
print(a==b)

# Compare three numbers, x = 7, y = 12, and z = 5, and print which one is the greatest.
x = 7
y = 12
z = 5
if x > y and x > z:
    print("x is the greatest")
elif y > x and y > z:
    print("y is the greatest")
else:
    print("z is the greatest")


# Compare two lists list1 = [1, 2, 3] and list2 = [1, 2, 3]. Why does list1 == list2 return True but list1 is list2 return False?
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1))
print(id(list2))
print(list1==list2) # same memory location
print(list1 is list2) # different memory location

# Create a class Person with attributes name and age. Write a program to compare two Person objects based on their age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Binod", 23)
p1 = Person("Saroj", 26)

if p.age > p1.age:
    print(f"{p.name} is older")
elif p.age < p1.age:
    print(f"{p1.name} is older")
else:
    print("They are of the same age")


