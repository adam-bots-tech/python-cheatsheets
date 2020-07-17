#If Statement
cars = ['audi','bmw','subaru','toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#Audi
#MW
#Subaru
#Toyota

#Other Comparators
# !=
# <
# <=
# >
# >=

#And Or
ages = (22, 24)
if ages[0] >= 22 and ages[1] <= 24:
	print(True)
#True
ages = (22, 24)
if ages[0] == 22 or ages[0] == 23:
	print(True)
#True

#Is a value in a list
toppings = ['mushrooms', 'sausage', 'pepperoni']
print('mushrooms' in toppings)
#True

#Not in a list
print('mushrooms' not in toppings)
#False

#List is not empty
if toppings:
	print(True)
#True

#List is empty
if not toppings:
	print(True)
else:
	print(False)

#Checking for a boolean
flag = False
if flag:
	print(flag)
elif not flag:
	print(flag)
#False

#Else If
age = 16
if age < 12:
	price = 25
elif age < 18:
	price = 50
else:
	price = 75
print(price)
#50

