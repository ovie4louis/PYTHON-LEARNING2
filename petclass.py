class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print (f"I am {self.name} I am {self.age} years old")

class Dog(Pet):

    def speaks(self):
        print("bark")

class Cat(Dog):
    def speak(self):
        print("Mweo")

# a = Pet("black dog", 5)
# a.show()
b = Dog("dog inside class of dog",  10)
b.speaks()
b.show()
c = Pet("class in pet", 67)
c.show()
        

