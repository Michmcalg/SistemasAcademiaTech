import config

EXTRA_POINTS = 5

def clean_names(names): #to clean names
    newNames = [name.strip().title() for name in names]
      
    return newNames


def get_grade(grade): #to get a grade
    match grade:
        case n if n>=90:
            return "A"
        case n if n>=80:
            return "B"
        case n if n>=70:
            return "C"
        case n if n>=config.MINIMUM_GRADE:
             return "D"
        case _:
            return "F"


def extra_points(grade): #to add points
    EXTRA_POINTS = 10

    return grade+EXTRA_POINTS





