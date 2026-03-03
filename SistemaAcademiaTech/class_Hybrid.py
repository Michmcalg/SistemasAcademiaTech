from class_Student import Student
from class_Access import online_access, onsite_access

class hybrid_estudent(Student,online_access, onsite_access):
    def Introduction(self):
        super().Introduction()
        print(f"I do study in hybrid mode because of my job.")