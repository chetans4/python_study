#Exceptions 
# Cammets must be used to tell whys and hows about some peace of code.

try:
    age = int(raw_input("Age : "))
    print age
    income = 20000
    risk = income / age
    print risk

except ZeroDivisionError:
    print "Age can not be zero!"
    
except ValueError:
    print "Age must be int!"


