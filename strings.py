#String and Formatted String
#Can Use Quotes and Double Quotes
first = "adam"
last = "white" 
print(f'hello, {first} {last}')
#hello, adam white

#Escape characters
print('\'') #Single quote
print('\"') #Double quote
print('\t') #Tab
print('\n') #New Line
print('\\') #Backslash

#Raw Strings
#Ignores all escape scharacters
print(r'This is Carol\'s cat')

#Multiline string with triple quotes
print('''This
	is
	a
	multiline
	string''')

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

#In and not in with strings
print('Hello' in 'Hello World')
#True
print('Hello' not in 'Hellow World')
#False

#White Space Manipulation
padded = " padded "
print(padded.rstrip())
# padded
print(padded.lstrip())
#padded
print(padded.strip())
#padded

#Strings can be multipled. Can't use with floats
print('Alice' * 5)
#AliceALiceAliceAliceAlice

#Useful string methods
hw = 'Hello, World'
print(hw.upper()) #Return an uppercase version of string
print(hw.isupper()) #String is all uppercase letters
print(hw.lower()) #Return a lowercase version of string
print(hw.islower()) #String is all lowercase letters
print(hw.istitle()) #String is words of uppercase letter followed by lowercase letters
print(hw.isalpha()) #String is letters only
print(hw.isalnum()) #String is letters and numbers only
print(hw.isdecimal()) #String is a float
print(hw.isspace()) #String is just white space characters
print(hw.startswith('H')) #String starts with this substring
print(hw.endswith('rld')) #String ends with this substring

#Strings to lists and lists to strings
sl = 'My name is Simon'
l = sl.split(' ') #Divide the string into a list, using a single white space character to split upon
print(l)
s = ' '.join(l) #Join the elements in the list into a string, using a single white space character to divide the elements
print(s)

#Partition - split only on first occurance of the character 'o'
hw = 'Hello, World!'
print(hw.partition('o'))
#('Hell', 'o', ', World!')

#Formating strings
print(hw.rjust(30))
print(hw.ljust(30))
print(hw.center(30))

#Get unicode code point
print(ord('A'))
#65
#Get unicode character based on code point
print(chr(65))