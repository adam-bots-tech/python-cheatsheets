# This is a comment

#String and Formatted String
#Can Use Quotes and Double Quotes
first = "adam"
last = "white" 
print(f'hello, {first} {last}')
#hello, adam white

#Multiple Variable Assignment
first, last = "adam", "white" 
print(f'hello, {first} {last}')
#hello, adam white

#String functions
print(f'hello, {first} {last}'.title())
#Hello, Adam White
print(f'hello, {first} {last}'.upper())
#HELLO, ADAM WHITE
print(f'hello, {first} {last}'.lower())
#hello, adam white

#White Space Manipulation
print("\tHello\n\tAdam White")
#	Hello
#	Adam White
padded = " padded "
print(padded.rstrip())
# padded
print(padded.lstrip())
#padded
print(padded.strip())
#padded

#Integers
print(2 + 3)
#5
print(2 * 3)
#6
print(3 - 2)
#1
print(4 / 2)
#2
print(3 ** 2)
#Exponent: 9

# Order of Operations supported
print(2 + 3 * 4)
#14
print((2 + 3) * 4)
#20

# Combining Floats and Integers always results in a Float
print(1 + 2.0)
#3.0

#Underscores used as commas in large numbers
print(14_000_000)
#14000000

#Constants not supported. Just use all caps
MAX_CONNECTIONS = 2