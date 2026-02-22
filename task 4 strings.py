#Find Length of a String

s = input("Enter string: ")
print("Length:", len(s))


#Convert String to Uppercase

s = input("Enter string: ")
print(s.upper())


#Convert String to Lowercase

s = input("Enter string: ")
print(s.lower())


#Check if String Starts With Given Substring

s = input("Enter string: ")
sub = input("Enter substring: ")

if s.startswith(sub):
    print("Yes")
else:
    print("No")


#Join List into Single String

words = ["Hello", "World"]
result = " ".join(words)
print(result)


#Slice a Substring

s = input("Enter string: ")
print(s[0:4]) 


#Reverse a String

s = input("Enter string: ")
print(s[::-1])


#Check if String is Alphanumeric

s = input("Enter string: ")

if s.isalnum():
    print("Yes")
else:
    print("No")



#Count Number of Vowels

s = input("Enter string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowels:", count)



#Check if Only Alphabetic Characters

s = input("Enter string: ")

if s.isalpha():
    print("Yes")
else:
    print("No")


#Check if Only Digits

s = input("Enter string: ")

if s.isdigit():
    print("Yes")
else:
    print("No")

#Capitalize First Character

s = input("Enter string: ")
print(s.capitalize())




























































