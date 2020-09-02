import json

#Example of working with json files and dictionaries

#Dumping a dictionary to a json file
user = {
	'name': 'Adam',
	'age': 36,
	'occupation': 'Software Engineer'
}

with open('user.json', 'w') as file:
	json.dump(user, file)

with open('user.json') as file:
	print(file.read())

#Loading a json file into a dictionary
user_copy = {}

with open('user.json') as file:
	user_copy = json.load(file)

print(user_copy)
