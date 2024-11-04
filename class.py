class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(name)

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age_1):
        self.age = age_1
        # return self.age
    
       
        



d = Dog("tim", 5)
print(d.get_name())
print(d.get_age())
d.set_age(2334)
print(d.get_age())
# print(d.set_age(345))
# d2 = Dog("louis", 10)
# print(d2.get_name())



#     # def bark(self):
#     #     print("barking")

# d = Dog('ovie')
# print(d.get_name())
# # d2 = Dog("louis")

