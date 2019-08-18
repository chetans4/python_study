#Inheritance

class Mammal:
    def walk(self):
        print "Walk"

class Dog(Mammal):
    pass
    
class Cat(Mammal):
    def be_annoying(self):
        print "Annoying!"
        

dog = Dog()
dog.walk()

cat = Cat()
cat.walk()
cat.be_annoying()

#For more details get docs