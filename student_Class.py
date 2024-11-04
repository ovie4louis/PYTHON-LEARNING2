class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.total = []


    def get_Student_Details(self):
        return self.name, self.age, self.grade
    
    def get_grade(self):
        return self.grade
    def age_and_name(self):
        return self.age + self.grade
    def total_name(self):
       
            return self.name
       


 # Create two instances of the Student class and print their details and sum of their grades.   
s1 = Student("ovie", 35, 97)
s2 = Student("enakarhire", 65, 99)
print(s2.age_and_name())
print(Student.s1)

            



