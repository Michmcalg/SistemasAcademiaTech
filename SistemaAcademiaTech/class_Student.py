from class_Person import Person

class Student (Person):

    total_students = 0

    def __init__(self, name, age, type_class):
        super().__init__(name, age)
        self.type_class= type_class
        Student.total_students += 1

    def Introduction(self):
        super().Introduction()
        print(f"I am student from the {self.type_class} class.")

    @classmethod
    def sum_students(cls):
        print(f"Total of registered students: {cls.total_students}")






