from class_Person import Person
from class_Student import Student
from class_Instructor import Instructor
from class_Access import online_access
from class_Hybrid import hybrid_estudent

def present_people(people_list): 
    for person in people_list:
        person.Introduction()
    

if __name__ == "__main__":

        people_list = [
        Student("Daniela", 30, "Cyber Security"),
        Student("Alexa", 16, "Cloud Computing"),
        Instructor("María", 28, "Computer Science"),
        Instructor ("Miguel", 26, "Math"),
        hybrid_estudent ("Mich", 18, "Data Analysis")
     ] 

        present_people(people_list)


    
    