#SECTION A: LOOPS

#Sum of Digits

#Definition: Add all digits of a number using loop.

n = int(input("Enter number: "))
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    n = n // 10

print("Sum of digits:", sum_digits)

#Reverse a Number

#Definition: Reverse digits of number without converting to string.

n = int(input("Enter number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reversed number:", reverse)

#Armstrong Number

#Definition: A number equal to sum of its digits power of number of digits.


n = int(input("Enter number: "))
temp = n
digits = len(str(n))
sum_power = 0

while temp > 0:
    digit = temp % 10
    sum_power += digit ** digits
    temp = temp // 10

if sum_power == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")

#Fibonacci Series

#Definition: Series where next number = sum of previous two numbers.

n = int(input("Enter how many numbers: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#Prime Count

#Definition: Count prime numbers from 1 to N.

n = int(input("Enter number: "))
count = 0

for num in range(2, n+1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        count += 1

print("Total prime numbers:", count)

#SECTION B: FUNCTIONS

#Even or Odd Function

#Definition: Function to check even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(5))

#Factorial Function

#Definition: Multiply number by all numbers below it.

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print(factorial(5))

#Largest of Three

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(largest(10, 25, 15))

#Count Vowels

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Python Programming"))

#Simple Calculator (Menu Driven)

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", sub(a, b))
    elif choice == 3:
        print("Result:", mul(a, b))
    elif choice == 4:
        print("Result:", div(a, b))

#SECTION C: MODULES

#Custom Module

#operations.py

def square(n):
    return n * n

def cube(n):
    return n * n * n

#main.py

import operations

print(operations.square(4))
print(operations.cube(3))

#Random Guess Game

import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess number (1-100): "))

    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct Guess!")
        break

#Math Module Usage

import math

print("Square Root:", math.sqrt(16))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))

#BONUS MINI PROJECT

#Student Management System

students = []

def add_student():
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students.append([roll, name, marks])
    print("Student added!")

def view_students():
    for s in students:
        print("Roll:", s[0], "Name:", s[1], "Marks:", s[2])

def search_student():
    roll = int(input("Enter roll to search: "))
    for s in students:
        if s[0] == roll:
            print("Found:", s)
            return
    print("Student not found")

def average_marks():
    total = 0
    for s in students:
        total += s[2]
    if len(students) > 0:
        print("Average Marks:", total / len(students))
    else:
        print("No students available")

while True:
    print("\n1.Add 2.View 3.Search 4.Average 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        average_marks()
    elif choice == 5:
        break
