#Simple function with doc string
def greet_user():
	"""Greet me"""
	print("Hello!")

greet_user()

#Simple function with parameter
def greet_user(name):
	print(f"Hello, {name}!")

greet_user('Adam')

#Keyword arguments
greet_user(name='Ben')

#Simple function with two parameters, one with a default value
def greet_user(name, user_type='admin'):
	print(f"Hello, {name}! You are an {user_type}.")

greet_user('Sam')

#Returning a value
def format_name(name):
	return name.title()

name = format_name('Sam the man')
print(name)

#The contents of lists and dictionaries can be modfied via the reference passed
def modify_person(person):
	person['last-name'] = 'Gates'

person = {'first-name': 'Bill', 'last-name': 'Watterson'}
print(person)
modify_person(person)
print(person)

#Arbitary number of arguments. Arguments are stored in a tuple
def print_arguments(*arguments):
	print(arguments)

print_arguments('1', '2', '3')

#Arbitary keyword arguments can be assembled into a dictionary
def build_person(**attributes):
	print(attributes)

build_person(first_name='Adam', last_name='Long')

import modules

#Functions can be used from modules
modules.make_pizza(16, 'cheese', 'pepperoni')

from modules import make_pizza

#They can be referenced via their namespace or directly if specifically imported. 
make_pizza(16, 'cheese', 'sausage')

import modules as m
from modules import make_pizza as mp

#Modules and functions from modules can be assigned an alias
m.make_pizza(16, 'cheese', 'meatballs')
mp(16, 'cheese', 'olives')

from modules import *

#All functions can be imported from a module into the script's namespace
make_pizza(16, 'cheese', 'sausage', 'pepperoni')

#Call Stack Example
def a():
	print('a() starts')
	b()
	d()
	print('a() returns')

def b():
	print('b() starts')
	c()
	print('b() returns')

def c():
	print('c() starts')
	print('c() returns')

def d():
	print('d() starts')
	print('d() returns')

a()

#End program early
import sys
sys.exit()