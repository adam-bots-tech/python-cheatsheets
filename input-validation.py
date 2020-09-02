#pip install pyinputplus
import pyinputplus as pip

#inputStr
#inputNum
#inputChoice
#inputMenu
#inputDateTime
#inputYesNo
#inputBool
#inputEmail
#inputFilepath
#inputPassword

age = pip.inputNum(prompt = 'What is your age? ', greaterThan = 1)
#Alow blank
age = pip.inputNum(prompt = 'What is your age? ', greaterThan = 1, blank=True)
#Limit retries on wrong answers
age = pip.inputNum(prompt = 'What is your age? ', greaterThan = 1, limit=2)
#Timeout after 30 seconds if no input given
age = pip.inputNum(prompt = 'What is your age? ', greaterThan = 1, timeout=30)
#Define a defaul value so retrylimitexception or timeoutexception aren't thrown
age = pip.inputNum(prompt = 'What is your age? ', greaterThan = 1, limit=2,default=18)
#Only accept roman numerals via a regex
age = pip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+'])
#Don't accept numbers ending in 00
age = pip.inputNum(blockRegexes=[r'00$'])

#Custom input example
def addsUpToTen(numbers):
	l = list(numbers)
	for i, digit in enumberate(l):
		l[i] = int(digit)
	if sum(l) != 10:
		raise Exception('The digits must add up to 10.')
	else:
		return int(numbers)

age = pip.inputCustom(addsUpToTen)

