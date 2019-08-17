#2d lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#print matrix

for row in matrix:
    for item in row:
        print item
        
print "----------------------List methods---------------------------"

numbers = [4,7,5,2,7,1,6]

numbers.append(20)

numbers.insert(0,10)

numbers.remove(5)

#since python 3.3
#numbers.clear()

#remove last item from list
numbers.pop()

#to check first occurance of object, if not in list ValueError will occure
print numbers.index(2)

print 50 in numbers


print numbers.count(7)

print numbers

# retun None: means absnce of value, null in java
print numbers.sort()
print numbers
numbers.reverse()
print numbers


# copy not working ????????
#numbersCopy = numbers.copy()

numbersCopy = list(numbers)

print numbersCopy


print "--------------------------Remove Duplicate from list -------------------------------"

duplicateList = [2,3,6,1,3,7,9,4,1]

print duplicateList


for number in duplicateList:
    if duplicateList.count(number) > 1:
        duplicateList.remove(number)

print duplicateList


uniqueList = []
for number in duplicateList:
    if number not in uniqueList:
        uniqueList.append(number)

print uniqueList






























