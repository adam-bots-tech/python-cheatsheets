#Collecting Input
#message = input('Enter number of loops: ')
message = '40'
print(message)

#Casting the message for use
loops = 0
if(message.isnumeric()):
	loops = int(message)
	print(loops)
else:
	print("Not an integer!")

#While loop with a continue and a break
i = 0
while i < loops:
	i += 1

	if i == 20:
		break
	elif i % 2 == 0:
		continue
	else:
		print(i)

#Moving Items from one list to another
numbers = [1,2,3,4]
print(numbers)
swaps = []
print(swaps)

while numbers:
	swaps.append(numbers.pop())

print(numbers)
print(swaps)

#Removing all instances of a specific value
pets = ['dog', 'cat', 'dog', 'cat', 'horse','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

#input("Press ENTER to exit.")