#Print First N Natural Numbers

n = int(input("Enter N: "))
for i in range(1, n+1):
    print(i, end=" ")

#Print First N Even Natural Numbers

n = int(input("Enter N: "))
for i in range(1, n+1):
    print(2*i, end=" ")


#Print First N Odd Natural Numbers

n = int(input("Enter N: "))
for i in range(1, n+1):
    print(2*i-1, end=" ")


#Print First N Multiples of 3

n = int(input("Enter N: "))
for i in range(1, n+1):
    print(3*i, end=" ")

#Print First N Multiples of 5

n = int(input("Enter N: "))
for i in range(1, n+1):
    print(5*i, end=" ")


#Print All Multiples of 2 Till N

n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i, end=" ")

#Multiples of 2 or 3 Till N

n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0:
        print(i, end=" ")



#Multiples of 2, 5 or 7 Till N

n = int(input("Enter N: "))
for i in range(1, n+1):
    if i % 2 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")


#First N Multiples of 3, 5 or 7

n = int(input("Enter N: "))
count = 0
num = 1

while count < n:
    if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print(num, end=" ")
        count += 1
    num += 1


#Sum of Digits

num = int(input("Enter number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum:", sum)


#Count Number of Digits

num = int(input("Enter number: "))
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Digits:", count)



#Find Factors

n = int(input("Enter number: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")


#Count Factors

n = int(input("Enter number: "))
count = 0

for i in range(1, n+1):
    if n % i == 0:
        count += 1

print("Total factors:", count)



#Factorial

n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("Factorial:", fact)


#Sum of Even and Odd Numbers

n = int(input("How many numbers: "))

even_sum = 0
odd_sum = 0

for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)


#Palindrome Number

num = int(input("Enter number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")



#Armstrong Number

num = int(input("Enter number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num = num // 10

if original == sum:
    print("Armstrong")
else:
    print("Not Armstrong")


#Star Square

n = int(input("Enter N: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()





















    
