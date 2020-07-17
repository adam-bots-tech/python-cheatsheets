#Inherited class definition
class Animal:
	def __init__(self, name):
		self.name=name

	#Overriden by the method in the child class
	def get_long_name(self):
		return f"{self.name} the Animal"

#Class definition
class Dog(Animal):
	"""Simple model of a dog"""

	#Constructor
	#self argument is automatically passed by method call for every class method
	#class properties are attributes and can be added to self at will
	def __init__(self, name, age):
		#Initializing the parent class
		super().__init__(name)
		#Assigning values to attributes
		self.age=age
		#Default value
		self.breed = 'mixed'

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")

	def get_long_name(self):
		return f"{self.name} the Dog"

	def set_name(self, name):
		self.name=name

#Creating an instance and accessing attributes
dog = Dog('Jack', 6)
print(f"{dog.name} is {dog.age} years old.")

#Modifying attributes
dog.age=12
print(f"{dog.name} is {dog.age} years old.")

#Calling methods
dog.sit()
dog.roll_over()

#Using a getter and setter
dog.set_name('Clover')
print(dog.get_long_name())

#How to import classes
#Whole module
import classes
#Single class to namespace
from classes import Dog
#Multiple classes to namespace
from classes import Animal, Dog
#All classes directly to namespace
from classes import *
#Alias
from classes import Dog as d