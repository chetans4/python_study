#Comparision operators
# >, < >=, <=, ==, !=

name = raw_input("Enter your name : ") #"Chetan"

if len(name) < 3:
    print("Name must be atleast 3 char")
elif len(name) > 50:
    print "Name can be a max 50 char"
else:
    print "Name looks good"
    
    
print "----------------------------------------"
weight = int(raw_input("Weight : "))
unit = raw_input("L(bs) or K(gs) : ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print "You are "+str(converted)+" kilos"
else:
    converted= weight / 0.45
    print "You are "+str(converted)+" pounds"
    

