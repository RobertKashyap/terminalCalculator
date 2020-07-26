#!/usr/bin/python3
import re

print('THE CALCULATOR')
print("Type 'quit' to exit\n")

previous = 0

def performMath():
	global previous
	equation = ""
	
	if previous == 0:
		equation = input('enter equation : ')
	else:
		equation = input(str(previous))
	
	if equation == 'quit':
		print('Good Bye!!')
		quit()
	else:
		equation = re.sub('[a-zA-Z,:" "=]','',equation)
		if previous == 0:
			previous = eval(equation)
		else:
			previous = eval(str(previous)+equation)

while True:
	performMath()
