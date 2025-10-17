# This is a comment. It will not be executed
print("Hello, World!")

"""
This is a multi-line comment.
It can be used to describe larger sections of code.
"""

# taking input in python . it stops the program and waits for the input . it always returns a string 
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")

# converting the input from string to integer
num = int(input("Enter a number: "))
print(num, "is of type", type(num))

# converting the input from string to float
floatNum = float(input("Enter a decimal number: "))
print(floatNum, "is of type", type(floatNum))

# taking multiple inputs 
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)

# prints the type of a variable
print(type(x))

# taking a list from input
li = input("Enter elements separated by space: ").split()
print("List:", li)

# taking multiple inputs and adding them to a list using a loop
a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    a.append(element)

print("List:", a)

# This code takes a single line of numeric input, splits it and converts all elements to integers
li = list(map(int, input("Enter numbers separated by space: ").split()))
print("List:", li)

# This code uses list comprehension to collect n elements from the user in a single line of code
n = int(input("Enter the number of elements: "))
a = [input(f"Enter element {i+1}: ") for i in range(n)]
print("List:", a)

# This code takes input for a nested list using commas for elements and semicolons for sublists
li = [x.split(",") for x in input("Enter nested list (use commas and semicolons): ").split(";")]
print("Nested List:", li)

# To use variables effectively, we must follow Python’s naming rules:
"""
Variable names can only contain letters, digits and underscores (_).
A variable name cannot start with a digit.
Variable names are case-sensitive (myVar and myvar are different).
Avoid using Python keywords (e.g., if, else, for) as variable names.
"""

# python variables are dynamic 
x = 5
y = 3.14
z = "Hi"

# multiple assignments
a = b = c = 100
print(a, b, c) 

# Casting variables
s = "10"  # Initially a string
n = int(s)  # Cast string to integer
cnt = 5
f = float(cnt)  # Cast integer to float
age = 25
s2 = str(age)  # Cast integer to string

# swapping two variables
a, b = 5, 10
a, b = b, a

# counting characters in a string
word = "Python"
length = len(word)

# Removing the variable using del
del x

# Comparison Operators
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Logical Operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

