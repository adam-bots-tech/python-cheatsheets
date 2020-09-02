#Exceptions
#Try Except Else blocks with pass statement to tell python to fail silently
try:
	answer = print(5/0)
except ZeroDivisionError as err:
	print(err)
	pass
else:
	print(answer)