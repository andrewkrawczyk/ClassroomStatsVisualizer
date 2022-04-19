class Student:

    name = ""
    grade_array = []
    weighted_array = []

    def __init__(self, name, grades):
        self.name = name
        for grade in grades:
            self.grade_array.append(grade)

        

