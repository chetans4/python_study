#if statements

is_hot = True

if is_hot:
    print ("it's a hot day")
    print ("drink bhut water")
print ("Enjoys your day")

print ("-------------------------------------------")
is_hot = False
is_cold = True

if is_hot:
    print ("it's a hot day")
    print ("drink bhut water")
elif is_cold:
    print ("It's a cold day")
    print ("wear warm cloths")
else: 
    print ("it's a lovely day")
#else if is_cold:
 #   print "It's a cold day"
  #  print "wear warm cloths"

print ("Enjoys your day")

print ("-------------------------------------------")
print ("-------------------------------------------")

buyer_credit = "good credit"

if "good credit" == buyer_credit:   # Case Sencitive
    down_payment = "put down 10%"
else:
    down_payment = "put down 20%"
print ("down payment : "+down_payment)

print("Case Fold StR".casefold())
