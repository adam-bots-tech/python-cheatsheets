import re

#Create a regex for matching phone numbers
r = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#Matching
#Search for the phone number
s = 'My phone number is 888-888-8888'
m = r.search(s)
#Print the phone number we found
print(m.group())
#888-888-8888

#Grouping
#Search for the phone number and group the match into different sub strings
r = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
m = r.search(s)
print(m.group(0))
#888-888-8888
print(m.group(1))
#888
print(m.group(2))
#888
print(m.group(3))
#8888

#Multiple Matching groups with pipes
r = re.compile(r'Bat(mobile|man|copter|bat)')
m = r.search('Batmobile lost a wheel')
print(m.group(0))
#Batmobile
print(m.group(1))
#mobile

#Optional Matching with question marks
r = re.compile(r'Bat(wo)?man')
m = r.search('I am Batman')
print(m.group(0))
#Batman
m = r.search('I am Batwoman')
print(m.group(0))
#Batwoman

#Matching zero or more
r = re.compile('I( )*am batman')
m = r.search('Iam batman')
#Iam batman
print(m.group(0))
m = r.search('I am batman')
#I am batman
print(m.group(0))
m = r.search('I   am batman')
#I   am batman
print(m.group(0))

#Matching one or more
r = re.compile('I( )+am batman')
m = r.search('Iam batman')
#None
print(m)
m = r.search('I am batman')
#I am batman
print(m.group(0))
m = r.search('I   am batman')
#I   am batman
print(m.group(0))

#Specific repetitions
r = re.compile(r"(Ha){3}")
m = r.search('I am the Joker. HaHaHaHa')
#HaHaHa
print(m)

#Find all
r = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
m = r.findall('Home: 888-888-8888, Work: 999-999-9999')
print(m)
#['888-888-8888', '999-999-9999']

#Character classes
#\d - 0-9
#\D - NOT 0-9
#\w - 0-9,a-z,A-Z,_
#\W - NOT 0-9,a-z,A-Z,
#\s - Any whitespace character
#\S - NOT a whitespace character

#Custom character classes
#Any vowel
r = re.compile(r'[aeiouAEIOU]')
m = r.findall('I am NEW')
print(m)
#['I', 'a', 'E']

#Start and End of String
r = re.compile('^Hello$')
m = r.match('Hello World')
print(m == None)
#True
m = r.match('World Hello')
print(m == None)
#True
m = r.match('Hello')
print(m == None)
#False

#Wild card
r = re.compile(r'.at')
m = r.findall('cat hat mat ha rat')
print(m)
#['cat', 'hat', 'mat', 'rat']

#String subsititution
r = re.compile(r'(Agent) \w+')
s = r.sub(r'\1 Reese', 'Agent Cody')
print(s)