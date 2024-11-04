class Course:
    number_students = 5  # Keep track of registered students (class variable)

    def __init__(self, name, course, units):
        self.name = name
        self.course = course
        self.units = units

    def student_name(self):
        return self.name

    def student_course(self):
        return self.course

    def student_units(self):
        return self.units

    def student_name_course_unit(self):
        return self.name, self.course, self.units

    def register_course(self):
        # Check if the number of students is less than 6
        if Course.number_students > 0 :
            Course.number_students -= 1  # Increment the class-level count
            return self.student_name_course_unit()
        else:
            return "Maximum number reached"

# Testing the class
student1 = Course("ovie", "PHY101", 3)
student2 = Course("paul", "BIO101", 2)
student3 = Course("peace", "MATH101", 1)
student4 = Course("joy", "CHM101", 3)
student5 = Course("louis", "GEO101", 1)
student6 = Course("James", "FUR104", 3)

# Registering each student and printing the results
print(student1.register_course())  # ('ovie', 'PHY101', 3)
print(student2.register_course())  # ('paul', 'BIO101', 2)
print(student3.register_course())  # ('peace', 'MATH101', 1)
print(student4.register_course())  # ('joy', 'CHM101', 3)
print(student5.register_course())  # ('louis', 'GEO101', 1)
print(student6.register_course())
