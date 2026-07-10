## **Question 1:** Write a Python program to print "Hello, World!".
print("Hello, World!")

## **Question 2:** Write a Python program that takes a user input and prints it.
user_input = input('Enter just anything:')
print(user_input)

## **Question 3:** Write a Python program to check if a number is positive, negative, or zero.
number = float(input('Enter a number:'))
if number > 0:
    print('The number is positive')
elif number < 0:
    print('The number is negative')
else:
    print('The number is zero')

## **Question 4:** Write a Python program to find the largest of three numbers.
num1 = float(input('Enter first number:'))
num2 = float(input('Enter second number:'))
num3 = float(input('Enter third number:'))
max = num1
if(max < num2):
    max = num2
if(max < num3):
    max = num3
print('The largest number is:', max)

## **Question 5:** Write a Python program to calculate the factorial of a number.
number = int(input('Enter a number:'))
factorial = 1
if number < 0:
    print('Factorial does not exist for negative numbers')
elif number == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(1, number + 1):
        factorial *= i
    print('The factorial of', number, 'is', factorial)


## **Question 6:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.
age = 25  # integer
height= 5.11 # float
name = "John Doe"  # string
is_student = True  # boolean
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Name:", name, "Type:", type(name))
print("Is Student:", is_student, "Type:", type(is_student))


## **Question 7:** Write a Python program to swap the values of two variables.
number1 =5
number2 = 10
number1, number2 = number2, number1
print("After swapping: number1 =", number1, "number2 =", number2)

## **Question 8:** Write a Python program to convert Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

## **Question 9:** Write a Python program to concatenate two strings.
greeting = "Hello"
name = "Alice"
concatenated_string = greeting + " " + name
print(concatenated_string)

## **Question 10:** Write a Python program to check if a variable is of a specific data type.
number=10 
data_type_of_number = type(number)
print("The data type of number is:", data_type_of_number)
if isinstance(number, int):
    print("The variable is an integer")
else:
    print("The variable is not an integer")

## **Question 11:** Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.
a = 5
b=10
c=7

addition = a+b+c
subtraction = a-b-c
multiplication = a*b*c
division = a/b
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)    
print("Division:", division)

## **Question 12:** Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.
x=6
y=10
isEqualTo = x==y
isNotEqualTo = x!=y
isGreaterThan = x>y
isLessThan = x<y
print("Is Equal To:", isEqualTo)
print("Is Not Equal To:", isNotEqualTo) 
print("Is Greater Than:", isGreaterThan)
print("Is Less Than:", isLessThan)

## **Question 13:** Write a Python program to demonstrate logical operators: and, or, not.
x = True
y = False
z = False
logical_and_one_true = x and y
logical_and_one_false = x and z
logical_and_both_true = x and x
logical_or_one_true = x or y
logical_or_both_false = y or z
logical_or_both_true = x or x
logical_not_positive = not x
logical_not_negative = not y
print("Logical AND (one true):", logical_and_one_true)
print("Logical AND (one false):", logical_and_one_false)
print("Logical AND (both true):", logical_and_both_true)
print("Logical OR (one true):", logical_or_one_true)
print("Logical OR (both false):", logical_or_both_false)
print("Logical OR (one true):", logical_or_one_true)
print("Logical NOT (positive):", logical_not_positive)
print("Logical NOT (negative):", logical_not_negative)

## **Question 14:** Write a Python program to calculate the square of a number.
number = int(input('Enter a number:'))
square_of_number = number ** 2
print('The square of', number, 'is', square_of_number)

## **Question 15:** Write a Python program to check if a number is even or odd.
number = float(input('Enter a number:'))
if number % 2 == 0:
    print ("The number is even")
else:
    print ("The number is odd")

## **Question 16:** Write a Python program to find the sum of the first n natural numbers.
n = int(input('Enter a number:'))
if n < 0:   
    print('Please enter a positive integer')
else:
    sum_of_natural_numbers = n * (n + 1) // 2
    print('The sum of the first', n, 'natural numbers is', sum_of_natural_numbers)

## **Question 17:** Write a Python program to check if a year is a leap year.
year = int(input('Enter a year:'))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')