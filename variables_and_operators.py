# This is a comment if you didn't already know. It is not interpreted.
''' This is a 
multiline comment '''

#Nothingness assigned to a variable
nothing = None
if nothing == None:
	print('The void')

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

#Type conversaion
print('I am ' + str(29) + ' years old.')
#I am 29 years old
print( 40 + int('9'))
#49
print(100.0 - float(10))
#90.0

#Modifying a global variable from within a function
def spam():
	global eggs
	eggs = 'spam'

eggs = 'global'
print(eggs)
spam()
print(eggs)