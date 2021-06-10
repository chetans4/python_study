#Lists

names= ["chetan", "mahendrs", "suendra", "rishu"]
print (names)
print (names[0])
print (names[-1])
print (names[2])
print (names[2:])    
names[0] = "CSChoudhay"; #will replace 0th index name.
print (names);


print ("-------------------------Assignment, find the lasgest number")

numbers = [12,34,11,9,56,31,13,56,78,43,98]
max_num = 0
for n in numbers:
    if max_num < n:
        max_num = n
print ("max number is : "+str(max_num))

