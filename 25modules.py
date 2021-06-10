# Modules

import A21keyword_arg
#A21keyword_arg.cal_cost(discount=0.1, price =20, shipping=2)

from A21keyword_arg import cal_cost

cal_cost(discount=0.1, price =20, shipping=2)

#NameError: name 'square' is not defined if not complete import or method not import.
#print A21keyword_arg.square(int(raw_input("Enter number to square : ")))

print ("-----------------------Assignment---------------------------------------------")

import utils_module

numbers = [10,2,5,19, 99]
print (f"Max by utils_module : {utils_module.find_max(numbers)}")

