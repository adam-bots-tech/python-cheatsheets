#Key Value Pair
#Can mix variable types
alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

#Adding new keys
alien['x-position'] = 0
alien['y-position'] = 25
alien['armor'] = 100
print(alien)

#Empty dictionary
alien_new = {}

#Modifiying a key
alien['color'] = 'yellow'

print(alien)

#Deleting a key
del alien['points']
print(alien)

#Formatting
alien_new = {
	'color': 'green',
	'points': 10
}
print(alien_new)

#Pretty printing
import pprint
pprint.pprint(alien_new)

#Using a default value if key not found
point_value = alien.get('points', 5)
print(point_value)

alien.setdefault('points', 5)
print(alien.get('points'))

#Looping
for key,value in alien_new.items():
	print(f"Key: {key} Value: {value}")

#Key Looping
for key in alien_new.keys():
	print(f"Key: {key}")

#Sorting the keys
sorted_alien = sorted(alien)
print(alien)
print(sorted_alien)

#Value looping
for value in alien_new.values():
	print(f"Value: {value}")

#Nesting
nested_alien = {
	'points': 10,
	'color': 'green',
	'coordinates': {
		'x': 0,
		'y': 25
	},
	'attributes': [
		'small',
		'fast'
	]
}
print(nested_alien)
for attribute in nested_alien['attributes']:
	print(attribute)
print(nested_alien['coordinates']['x'])
print(nested_alien['coordinates']['y'])

#List of aliens
#Make 10 aliens
aliens = []
for i in range(10):
	aliens.append({'color': 'green', 'points': 25, 'id': i})
#Print first five
for alien in aliens[:5]:
	print(alien)
#Count the aliens
print(len(aliens))
