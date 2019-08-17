#Guessing Game
#i =1
#num = 9
#while i <= 3:
#    guess_num = int(raw_input("Guess : "))
#    if guess_num == 9:
#        print "You win!"
#        i = 4
#    else:
#        i +=1
#        if i > 3:
#            print "You failed!"
#-----------------------------------------------------------------------------     
#    guess_num = raw_input("Guess : ")
#    if str(guess_num) != "9":
#        i += 1
#        if i > 3:
#            print "You failed!"
#    else:
#        print "You win."
#        break
#print "Done"
#-----------------------------------------------------------------------------     
#-----------------------------------------------------------------------------     


guess_limit = 3
secret_num = 9
guess_count = 0
while guess_count < guess_limit:
    guess_count +=1
    guess_num = int(raw_input("Guess : "))
    if guess_num == secret_num:
        print "You won!"
        break
else:   #In python while has an else part
    print "You failed!"
print "Done."



