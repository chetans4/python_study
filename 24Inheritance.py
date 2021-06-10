#Inheritance

class Mammal:
    def walk(self):
        print("Walk : "+self.type)

class Dog(Mammal):

    def __init__(self):
        self.type = "Dog"
   # pass

class Cow(Mammal):
    pass

class Cat(Mammal):
    
    def __init__(self):
        self.type = "Cat"

    def be_annoying(self):
        print (self.type + " Annoying!")
        

dog = Dog()
dog.walk()

cat = Cat()
cat.walk()
cat.be_annoying()

#cow = Cow()
#cow.walk()
#cow.be_annoying()

#For more details get docs