#Nested loop

#for x in range(4):
#    for y in range(3):
#        print "("+str(x)+","+str(y)+")"


print "-------Assignment--------------"
numbers = [5,2,5,2,2]
for i in numbers:
    output =""
    for j in range(i):
        output += '*'
    print output
    
print "-------Assignment 2--------------"
numbers = [2,2,2,2,5,5]
for i in numbers:
    output=''
    for j in range(i):
        output += '*'
    print output