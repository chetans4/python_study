# 21 Keyword arguments, in the keyword argument we do not need to worry about oorder of the argument and readibility will be improved.
# but positional agr is prefered
#Keyword argument must come after positional argument in passing perameter greetuser(fname='john', 'smith') will give error but viceversa will be correct.

def cal_cost(price, shipping, discount):
    total = price + shipping - discount;
    print (total)
    
#cal_cost(discount=0.1, price =10, shipping=2)

print ("-----------------------Print statement 1 -------------------------")

def square(num):
    return num * num;
    
#print square(int(raw_input("Enter number to square : ")))

# If we try to get value of a function who is not returning anything then we will receive 'None'

def square(num):
    print (num * num);

print ("-----------------------Print statement 2 -------------------------")

#print square(int(raw_input("Enter number to square : ")))


#function can be reuasable in mutiple modules