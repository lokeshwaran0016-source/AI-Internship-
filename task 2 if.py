#Smallest Among Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print("Smallest number is:", a)
else:
    print("Smallest number is:", b)



#Largest Among Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number is:", a)
else:
    print("Largest number is:", b)


#Absolute Value
    
num = int(input("Enter a number: "))

if num < 0:
    print("Absolute value is:", -num)
else:
    print("Absolute value is:", num)


#Even or Odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#Multiple of 5
    
num = int(input("Enter a number: "))

if num % 5 == 0:
    print("Multiple of 5")
else:
    print("Not multiple of 5")



#Multiple of 10
    
num = int(input("Enter a number: "))

if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not multiple of 10")



#Two Digit Number
    
num = int(input("Enter a number: "))

if 10 <= num <= 99:
    print("Two digit number")
else:
    print("Not two digit")



#Three Digit Number
    
num = int(input("Enter a number: "))

if 100 <= num <= 999:
    print("Three digit number")
else:
    print("Not three digit")



#Three Digit Number
    
num = int(input("Enter a number: "))

if 100 <= num <= 999:
    print("Three digit number")
else:
    print("Not three digit")


#Square Above or Below 50
    
num = int(input("Enter a number: "))
square = num * num

if square > 50:
    print("Above 50")
else:
    print("Below or equal to 50")



#Difference is 0 or Not
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a - b == 0:
    print("Difference is 0")
else:
    print("Difference is not 0")


#Pass or Fail
    
marks = int(input("Enter marks: "))

if marks >= 50:
    print("Passed")
else:
    print("Failed")



#Divisible by 10
    
num = int(input("Enter a number: "))

if num % 10 == 0:
    print("Divisible by 10")
else:
    print("Not divisible by 10")


#Biggest Digit of Two Digit Number
    
num = int(input("Enter two digit number: "))

d1 = num // 10
d2 = num % 10

if d1 > d2:
    print("Biggest digit:", d1)
else:
    print("Biggest digit:", d2)



#Multiple of 5 and 3

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 3 == 0:
    print("Multiple of both 5 and 3")
else:
    print("Not multiple of both")



#Three Digit and Multiple of 10

num = int(input("Enter a number: "))

if 100 <= num <= 999 and num % 10 == 0:
    print("Three digit and multiple of 10")
else:
    print("Condition not satisfied")



#Smallest Among Three
    
if a < b and a < c:
    print("Smallest:", a)
elif b < c:
    print("Smallest:", b)
else:
    print("Smallest:", c)




























