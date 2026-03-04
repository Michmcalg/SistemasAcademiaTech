#practica de ✅ List comprehensions, match-case, Módulos, Scope resolution (LEGB), if __name__ == "__main__"

import config
import utils

def main():

    names = [" Ana gutierrez", "MariA ACOSTA", "miGuel alzate"] #unorganized names
    grades = [85, 60, 95] #grades

    get_names = utils.clean_names(names) #clean names
    extra = [utils.extra_points(grade) for grade in grades] #grades updaated

    for name, grade in zip(get_names, extra):
        letter = utils.get_grade(grade)
        print(f"{name:<20} | {grade:<10} | {letter}")
        
        print(f"{name:<20} | {grade:<10} | {letter}")

if __name__ == "__main__":
    main()