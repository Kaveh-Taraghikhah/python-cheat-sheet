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

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

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

# Bitwise Operators
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)

# Assignment Operators
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

# Identity Operators
print(a is not b)
print(a is c)

# Membership Operators
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# Ternary Operator
a, b = 10, 20
min = a if a < b else b

print(min)

# Operator Precedence
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# Operator Associativity
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)


# Python Data Types
x = 50  # int
x = 60.5  # float
x = "Hello World"  # string
x = ["geeks", "for", "geeks"]  # list 
x = ("geeks", "for", "geeks")  # tuple

# Numeric Data Types
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

# Sequence Data Types
s = 'Welcome to the Geeks World'
print(s)
print(type(s))
print(s[1])
print(s[2])
print(s[-1])

a = []
a = [1, 2, 3]
print(a)
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])
print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

tup1 = ()
tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

tup1 = (1, 2, 3, 4, 5)
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

# Set Data Type
s1 = set()
s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)
s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

set1 = set(["Geeks", "For", "Geeks"])
print(set1) 
for i in set1:
   print(i, end=" ")
print("Geeks" in set1)

# Dictionary Data Type
d = {}
d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(d['name'])
print(d.get(3))

# For Loop
n = 4
for i in range(0, n):
    print(i)

li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x),

# Iterating by Index of Sequences
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])

# While Loop
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

# Nested Loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

# Loop Control Statements
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)

for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)