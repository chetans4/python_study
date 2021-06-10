import re

previous = 0
run = True

print("Type 'quite' to exit")

def performCleaning(equation):
	return re.sub('[a-zA-Z" "`~!@#$&()_=|}{;:,.?><^]','',equation)

def performMath():
	global previous
	global run
	if previous == 0:
		equation = input("Enter the equation: ");
	else:
		equation = input(str(previous))
	
	if equation == "quite":
		run = False
	else:
		equation = performCleaning(equation);
		if previous == 0:
			print("You typed : ",equation)
			previous = eval(equation)
		else:
			previous = eval(str(previous) + str(equation))

while run:
	performMath()
	