# Classes

class Point:
# If we don't provide seft as argument. Error will be > Python 2: TypeError: draw() takes no arguments (1 given)
# Python 3: TypeError: draw() takes 0 positional arguments but 1 was given
    def draw(self):
        print ("Draw")
        
    def move(self):
        print ("Move")
        

point1 = Point()
point1.draw()

point1.x = 10

print (point1.x)


print ("----------------------------Constructor-----------------------------------")

class Point:
    #Special type method, to construct the object so it called : Constructor
    def __init__(self, x, y):
        self.x= x
        self.y = y
        
    def draw(self):
        print (f"Draw self.x : {self.x}, self.y : {self.y}")
        
point1 = Point(10,20)
print (point1.x)
print (point1.y)

point1.draw()
point1.x = 11
print (point1.x)
point1.draw()

print ("----------------------------Excersis-----------------------------------")


class Person:
    def __init__(self, name): #constructor
        self.name = name;
        
    def talk(self):
        print ("Hi, I am "+self.name);
        

p1 = Person("Choudhary")
print (p1.talk())



