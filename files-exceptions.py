#Reading a file
with open('numbers.txt') as file:
	contents = file.read()
	print(contents.rstrip())

#Reading line by line
with open('numbers.txt') as file:
	for line in file:
		print(line.rstrip())

#Buffering into a list
with open('numbers.txt') as file:
	lines = file.readlines()
	for line in lines:
		print(line.rstrip())

#Writing to an empty file
with open('inverse-numbers.txt', 'w') as file:
	i = 10
	while i >= 1:
		file.write(f'{i}\n')
		i -= 1

with open('inverse-numbers.txt') as file:
	print(file.read())

#Appending 
with open('inverse-numbers.txt', 'w') as file:
	file.write('0')

with open('inverse-numbers.txt') as file:
	print(file.read())

#Try Except Else blocks with pass statement to tell python to fail silently
try:
	answer = print(5/0)
except ZeroDivisionError:
	pass
else:
	print(answer)