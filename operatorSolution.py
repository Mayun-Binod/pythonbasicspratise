# Write a Python program to add, subtract, multiply, and divide two numbers given by the user.
number_one=float(input("Enter the first Number:"))
number_two=float(input("Enter the second Number:"))
result_number=number_one+number_two
result_number1=number_one-number_two
result_number2=number_one*number_two
result_number3=number_one/number_two
result_number4=number_one**number_two
result_number5=number_one//number_two
result_number6=number_one%number_two
print(f"the sum of number is {result_number}",round(result_number,2))
print(f"the subtract of number is {result_number1}",round(result_number1,2))
print(f"the multiply of number is {result_number2}",round(result_number2,2))
print(f"the division of number is {result_number3}",round(result_number3,2))
print(f"the exponent of number is {result_number4}",round(result_number4,2))
print(f"the floor division of number is {result_number5}")
print(f"the modulo/remainder of number is {result_number6}",round(result_number6,3))


# 2.Write a program to compare two numbers and print whether the first number is greater than, less than, or equal to the second number.
first_num=45
second_num=33
print(first_num>second_num)
print(first_num<second_num)
print(first_num==second_num)


# 3.Write a Python program to take an integer input and update its value using different assignment operators (+=, -=, *=, /=).
user_number=int(input("enter the assignment operator number:"))
user_number+=2
print(user_number)
user_number-=2
print(user_number)
user_number*=2
print(user_number)
user_number/=2
print(user_number)
user_number**=2
print(user_number)
user_number//=2
print(user_number)
user_number%=2
print(user_number)

# 4.Write a Python program to compare two objects and check if they refer to the same memory location using is and is not./identity operator
object1=[1,2,3,4] # using list so it has different memory location/mutable
object2=[1,2,3,4]
print(id(object1))
print(id(object2))
print(object1 is object2)
print(object1 is not object2)

object1={1,2,3,4} # using set so it has different memory location/mutable
object2={1,2,3,4}
print(id(object1))
print(id(object2))
print(object1 is object2)
print(object1 is not object2)

object1={"key":"value"} # using dictionary so it has different memory location/mutable
object2={"key":"value"}
print(id(object1))
print(id(object2))
print(object1 is object2)
print(object1 is not object2)

# now it has same memory location/immutable

object1=(1,2,3,4) # using tuple so it has same memory location/mutable
object2=(1,2,3,4)
print(id(object1))
print(id(object2))
print(object1 is object2)
print(object1 is not object2)

object1="Binod" # using string so it has same memory location/mutable
object2="Binod"
print(id(object1))
print(id(object2))
print(object1 is object2)
print(object1 is not object2)

object1=33 # using integer number so it has same memory location/mutable
object2=33
print(id(object1))
print(id(object2))
print(object1 is object2)
print(object1 is not object2)

object1=33.44 # using float number so it has same memory location/mutable
object2=33.44
print(id(object1))
print(id(object2))
print(object1 is object2)
print(object1 is not object2)

object1=3j # using complex number so it has same memory location/mutable
object2=3j
print(id(object1))
print(id(object2))
print(object1 is object2)
print(object1 is not object2)

# 5.Write a program to take three integers as inputs, and check if the sum of the first two numbers is greater than or equal to the third number using logical operators.
first_num=int(input("enter the first integer number:"))
second_num=int(input("enter the second integer number:"))
third_num=int(input("enter the third integer number:"))
print((first_num+second_num)>=third_num)

# 6.Write a Python program where you take four inputs and use assignment and logical operators to update a value based on complex conditions, then print the result.
# Take four inputs from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

# Initialize a variable to store the result
result = 0

# Use assignment and logical operators to update the result based on conditions
if a > 10 and b < 20:
    result += a

if c % 2 == 0 or d % 2 == 0:
    result *= 2

if a == b and c != d:
    result -= b

# Print the final result
print("Final result:", result)