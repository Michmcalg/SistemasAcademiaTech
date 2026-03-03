from class_Person import Person

class Instructor (Person):

    total_instructors = 0
    
    def __init__(self, name, age, speciality):
        super().__init__(name, age)
        self.speciality= speciality
        Instructor.total_instructors += 1

    def Introduction(self):
        super().Introduction()
        print(f"I am an instructor of {self.speciality}.")

    @classmethod
    def sum_instructors(cls):
        print(f"Total of registered instructors: {cls.total_instructors}")


