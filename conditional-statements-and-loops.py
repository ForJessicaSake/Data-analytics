# Module 2: Control Flow Assignments

## Write a program that asks the user to input a number and prints whether the number is positive.

number = float(input('Enter a number: '))
if number>0: 
    print(f'{number} The number is positive')

## Write a program that asks the user to input a number and prints whether the number is positive or negative.
number = float(input('Enter a number: '))
if number>0:
   print(f'{number} is positive')
else:
    print(f'{number} is negative')

## Write a program that asks the user to input a number and prints whether the number is positive, negative, or zero.
number = float(input('Enter a number:'))
if number == 0:
    print(f'{number} is zero')
elif number > 0:
    print(f'{number} is positive')
else:
    print(f'{number} is negative')

## Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.
number = float(input('Enter a number:'))
if number < 0:
    print(f'{number} is negative')
elif number > 0 and number % 2 == 0:
    print(f'{number} is positive and even')
else: 
    print(f'{number} is positive and odd')

## Lesson 2.2: Loops
## Write a program that prints all the numbers from 1 to 10 using a for loop.
for i in range(11):
    print(i)

## Write a program that prints all the numbers from 1 to 10 using a while loop.
n= 10
while n>=n:
    print(n)
    n+=1

## Write a program that prints a 5x5 grid of asterisks (*) using nested loops.
for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print('\n')

## Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.
# total = 0
sum = 0
user_input = float(input('Enter a number: '))
while user_input != 0:
    sum += user_input
    user_input = float(input('Enter a number: '))
print('The sum of all the input numbers is:', sum)

## Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.
for i in range(1,10):
    if i ==5:
        continue
    print(i)

## Write a program that defines an empty function using the pass statement.
def empty_function():
    pass

## Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop.

user_input = float(input('Enter a number: '))
for i in range(1, user_input + 1):
    if i % 2 ==0:
        print(i)

## Write a program that calculates the factorial of a number input by the user using a while loop.
user_input = float(input('Enter a number: '))
factorial = 1
if user_input == 0:
    print('The factorial of 0 is 1')
elif user_input < 0:
    print('Factorial does not exist for negative numbers')
else:
    i = 1
    while i <= user_input:
        factorial *= i
        i += 1
    print('The factorial of', user_input, 'is', factorial)


## Write a program that calculates the sum of the digits of a number input by the user using a while loop.
user_input = int(input('Enter a number: '))
sum_of_digits = 0
while user_input > 0:
    sum_of_digits += user_input % 10
    user_input //= 10
print('The sum of the digits is:', sum_of_digits)

## Write a program that checks if a number input by the user is a prime number using a for loop.
user_input = int(input("Enter a number: "))

if user_input <= 1:
    print(f"{user_input} is not a prime number")
else:
    is_prime = True

    for i in range(2, user_input):
        if user_input % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{user_input} is a prime number")
    else:
        print(f"{user_input} is not a prime number")

## Write a program that prints the first n Fibonacci numbers, where n is input by the user.
user_input = int(input('Enter a number: '))
a, b = 0, 1
for _ in range(user_input):
    print(a, end=' ')
    a, b = b, a + b
print()
