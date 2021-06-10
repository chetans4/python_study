#Strings
course = "Python's course for bigineers!"

print(course)
print(course[0]) #P
print(course[-1]) #!
print("o to 2 : "+course[0:3]) #Pyt
print("o to 2 : "+course[:3]) # Pyt
print("3 to end : "+course[3:]) #hon's course for bigineers!

another = course[:] # Python's course for bigineers!
#print another # py -2 	
print(another)

print("1 to second last: "+course[1:-1]) # ython's course for bigineers

course1 = 'Python for "bigineers"!\n'

print(course1) # Python for "bigineers"!\n
print(course1[-1]) #!
print(course1[-2]) # \n

msg = '''Hi Chetan,

This is message.

Thannks.'''

#print msg
print(msg)
print ('-----------------------------------Formated String---------------------------------------')

first = "Chetan"
last = 'Choudhary'

#python 2
msg = first+" ["+last+"] is a coder"
print (msg)

#in python 3
message = f'{first} [{last}] is a coder'
print( message)

print ('-----------------------------------String Functions---------------------------------------\n')

course = "Python's course for bigineers!"
# len is a general purpose fuction
print (len(course))

#string methods
print(course.upper());
print(course.lower());
print("Origional : "+course)
print (course.find("P"))
print (course.find("O")) #case sensitive
print (course.find("o"))
print (f'find B {course.find("B")}')
print (course.find("bigineers"))
print (course.replace("bigineers", "abs bigineers"))
print (course.replace("o", "A")) #relpace will replace all.
print ('Title : '+course.title())
print (f'find B in title : {course.title().find("B")}')
print ("Python"in course); # true is found
print ("python"in course);

