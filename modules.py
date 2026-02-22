# Basic Arithmetic Operations


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Temperature Conversion


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15


# Area Calculations


def circle_area(radius):
    pi = 3.14
    return pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height


# Basic Banking Operations

def create_account(name, balance):
    return {"name": name, "balance": balance}

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient balance"
    return balance - amount



# Student Academic Results


def calculate_total(marks_list):
    return sum(marks_list)

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"






