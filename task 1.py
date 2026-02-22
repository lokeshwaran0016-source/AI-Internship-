print("Hello World!")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)


num = int(input("Enter a number: "))
sqrt = num ** 0.5
print("Square root is:", sqrt)


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

d = (b**2 - 4*a*c) ** 0.5
x1 = (-b + d) / (2*a)
x2 = (-b - d) / (2*a)

print("The solutions are:", x1, "and", x2)



a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("(a+b)^2 =", (a+b)**2)
print("(a-b)^2 =", (a-b)**2)
print("a^2 - b^2 =", a**2 - b**2)


a = int(input("Enter a: "))
b = int(input("Enter b: "))

temp = a
a = b
b = temp

print("After swap:", a, b)




a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swap:", a, b)



km = float(input("Enter kilometers: "))

miles = km * 0.63

print("Miles:", miles)



c = float(input("Enter Celsius: "))

f = (c * 1.8) + 32

print("Fahrenheit:", f)



num = int(input("Enter a number: "))

last_digit = num % 10

print("Last digit is:", last_digit)




num = int(input("Enter a number: "))

last_two = num % 100

print("Last two digits are:", last_two)


















