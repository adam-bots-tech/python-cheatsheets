# Loop, loop, loop
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
	print(magician)

# alice
# david
# carolina

# Using variables in a loop
for magician in magicians:
	print(f"{magician.title()} is a magician")

# Alice is a magician
# David is a magician
# Carolina is a magician

# Using tabs to control flow
for magician in magicians:
	print(f"{magician.title()} is a magician")
	print(f"{magician.title()} is in the list")

print(f"{magician.title()} is the last in the list")

#Alice is a magician
#Alice is in the list
#David is a magician
#David is in the list
#Carolina is a magician
#Carolina is in the list
#Carolina is the last in the list

#Generating a range of numbers to loop through
for value in range(1,5):
	print(value)

#Storing the range in a list
numbers = list(range(1,5))
for value in numbers:
	print(value)

#1
#2
#3
#4

#Even numbers using step size
numbers = list(range(2,11,2))
for value in numbers:
	print(value)

#2
#4
#6
#8
#10

#Odd numbers using step size
numbers = list(range(1,10,2))
for value in numbers:
	print(value)

#1
#3
#5
#7
#9

#Statistics with a set of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
#0
print(max(digits))
#9
print(sum(digits))
#45

#List Comphrensions
#1-10 raised to the power of 2 and added to the list
squares = [value**2 for value in range(1,11)]
print(squares)

#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#Slicing ou a subset of a list. Start at position 1 and end before position 4
players = ['a', 'b', 'c', 'd', 'e']
print(players[1:4])
#['b', 'c', 'd']

#Slicing : 0:3 is identical to :3
print(players[0:3])
print(players[:3])
#['a', 'b', 'c']
#['a', 'b', 'c']

#Slicing: 2:5 is identical to 2:
print(players[2:5])
print(players[2:])
#['c', 'd', 'e']
#['c', 'd', 'e']

#Inverse: Start from end of list. Last two players
print(players[-2:])
#['d', 'e']

# Copying a list.
food = ['pizza', 'falafel', 'carrot cake']
friends_food = food[:]
print(food)
print(friends_food)
#['pizza', 'falafel', 'carrot cake']
#['pizza', 'falafel', 'carrot cake']
food.append('ice cream')
friends_food.append('milkshake')
print(food)
print(friends_food)
#['pizza', 'falafel', 'carrot cake', 'ice cream']
#['pizza', 'falafel', 'carrot cake', 'milkshake']

# Tuples: Identical to lists except immutable and use () instead of []
dimensons = (400, 200)
print(dimensons[0])
print(dimensons[1])