#Strings
course = "Python's course for bigineers!"

print(course)
print(course[0])
print(course[-1])
print("o to 2 : "+course[0:3])
print("o to 2 : "+course[:3])
print("3 to end : "+course[3:])

another = course[:]
print another

print("1 to second last: "+course[1:-1])

course1 = 'Python for "bigineers"!\n'

print(course1)
print(course1[-1])
print(course1[-2])

msg = '''Hi Chetan,

This is message.

Thannks.'''

print msg
print '-----------------------------------Formated String---------------------------------------'

first = "Chetan"
last = 'Choudhary'

#python 2
msg = first+" ["+last+"] is a coder"
print msg

#in python 3
#message = f'{first} [{last}] is a coder'
#print( message)

print '-----------------------------------String Functions---------------------------------------\n'

course = "Python's course for bigineers!"
# len is a general purpose fuction
print len(course)

#string methods
print course.upper();
print course.lower();
print "Origional : "+course

print course.find("P")
print course.find("O")
print course.find("o")
print course.find("bigineers")
print course.replace("bigineers", "abs bigineers")
print course.replace("o", "A")#relpace will replace all.

print 'Title : '+course.title()

print "Python"in course;
print "python"in course;



















