#2d lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#print matrix

for row in matrix:
    for item in row:
        print( item)

print ("----------------------List methods---------------------------")

numbers = [4,7,5,2,7,1,6]

print(numbers.append(20))

print(numbers.insert(0,10))

print(numbers.remove(5))

#remove last item from list
print(numbers.pop())

print (f"numbers : {numbers}")

#to check first occurance of object, if not in list ValueError will occure
print (numbers.index(7))

print (2 in numbers)

print (numbers.count(7))

print (numbers)

# retun None: means absnce of value, null in java
print (numbers.sort())
print (numbers)
numbers.reverse()
print (numbers)

numbersListCopy = list(numbers)
print (f"numbersListCopy : {numbersListCopy}")

# copy working in python 3
numbersCopy = numbers.copy()

#since python 3.3
numbers.clear()
print (f"numbers after clear : {numbers}")

print (f'dot numbersCopy :  {numbersCopy}')


print ("--------------------------Remove Duplicate from list -------------------------------")

duplicateList = [2,3,3,6,1,3,7,9,4,1]
duplicateListCopy = duplicateList.copy();

print (duplicateList)
print(f"removes first occurance : {duplicateList.remove(3)}")
print(duplicateList)


# keep last occurance
for number in duplicateList:
    if duplicateList.count(number) > 1:
        duplicateList.remove(number)

print (f'duplicateList : {duplicateList}')

# keep first occurance
uniqueList = []
for number in duplicateListCopy:
    if number not in uniqueList:
        uniqueList.append(number)

print (uniqueList)


