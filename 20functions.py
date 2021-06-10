#Functions
# Top to bottom

def greet_user():
    print ("Hi There,");
    print("Welcome aboard!")
    
print ("start")
greet_user()
print ("finish")



#Parameters

def greet_user(name):
    print ("Hi "+name)
    print ("Welcome aboard!")
    
print ("start")
#if do not pass or pass extra perameter the error will be: TypeError
greet_user("Chetan")
print ("finish")


def greet_user(fname, lname):
    print ("Hi "+fname+", "+lname)
    print ("Welcome")
    

print ("2 arg start")
greet_user("Ch", "Jat")
print ("2 arg end")

# Veriable length arguments and names arguments, are these present in Python?