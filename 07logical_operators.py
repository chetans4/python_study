#Logical operators

has_high_income = True
has_good_credit = False

#if has_high_income & has_good_credit:
if has_high_income and has_good_credit:
    print "Eligible for loan"

elif has_high_income or has_good_credit:
    print "Eligible for small loan"

print "-----------------------------------------------------"
has_criminal_record= False

if has_high_income and not has_criminal_record:
    print "Eligible for loan"