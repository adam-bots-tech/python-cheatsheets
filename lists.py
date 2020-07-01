#Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#['trek', 'cannondale', 'redline', 'specialized']

#List Access
#First
print(bicycles[0])
#trek
#Last
print(bicycles[-1])
#specialized

#Modification
bicycles[0] = 'training'
print(bicycles[0])
#training

#Adding
bicycles.append('mountain')
print(bicycles[-1])
#mountain

#Inserts value at 0 and shifts all elements to the right
bicycles.insert(0, 'toddler')
print(bicycles[0])
#toddler

#Removal of list items
del bicycles[0]
print(bicycles)
# ['training', 'cannondale', 'redline', 'specialized', 'mountain']

#Popping from tail
bicycles.pop()
print(bicycles)
# ['training', 'cannondale', 'redline', 'specialized']

#Popping from inside list; all elements to right shift to left
bicycles.pop(1)
print(bicycles)
# ['training', 'redline', 'specialized']

#Remove by value
bicycles.remove('training')
print(bicycles)
#['redline', 'specialized']

#Sort the list
bicycles.sort(reverse = True)
print(bicycles)
#['specialized', 'redline']

#Returns a sorted list without sorting the list itself
print(sorted(bicycles))
print(bicycles)
#['redline', 'specialized']
#['specialized', 'redline']

#Reverse index order
bicycles.reverse()
print(bicycles)
#['redline', 'specialized']

#List length
print(len(bicycles))
#2