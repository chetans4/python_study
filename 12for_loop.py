#For loop
for item in 'Python':
    print(item)
    
for item in ['chetan', 'mahendra', 'surendra']:
    print (item)
    
for item in [1,2,3,4]:
    print (item)
print( "--------------------------------range")    
for item in range(10):
    print (item)
    
print( "--------------------------------")
for item in range(5, 10):
    print (item)
    
print ("--------------------------------step")
for item in range(5, 10,2):
    print (item)


print ("--------------------------------Assignment")
prices = [10, 20, 30]
total_price = 0
for item in prices:
    total_price += item

print ("total cost in price : "+str(total_price))