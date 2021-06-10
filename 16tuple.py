#TUples are immutable lists

numbers = (2,5,3,8)
# we can not change in tuple

print (numbers[3])

print (numbers.count(3))
print (numbers.index(3))
# print(numbers.reverse())

#this will give type error
numbers[3] = 1

