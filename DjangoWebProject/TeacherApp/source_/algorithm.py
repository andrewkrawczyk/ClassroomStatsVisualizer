import pandas as pd

from DjangoWebProject.TeacherApp.models import Teacher, Student, Dra, Ireadymath, Ireadyreading


# ~~~~ CONFIGS ~~~~
# Change to sort by whichever column you want
sort_by = "CompScore"
# Scaling factor for unexcused absences
absence_factor = 0.95
# Cap for number of absences
absence_cap = 5

# TODO holds original student data, change to pull from database
# student = Student.objects.all().filter(teacher=8861)
# student
mainDF = pd.read_csv("test/testdata.csv")


def calc_score(dataDF =mainDF):

    # Holds mean, sd
    statsDF = dataDF.describe()

    adjDF = dataDF.copy()
    col_names = ["Reading", "Ilearn_1", "Ilearn_2"]  # TODO change if we add more columns

    row_count = adjDF.shape[0]

    for i in range(row_count):

        std_avg = 0
        absences = 0
        for col in col_names:
            # normalize "grade" columns to number of st.dev. above or below mean
            adjDF.loc[i, col] = (adjDF.loc[i, col] - statsDF.loc["mean", col]) / statsDF.loc["std", col]
            std_avg += adjDF.loc[i, col]
            absences = dataDF.loc[i, "Attendance"]

        # calculate average of student st.dev.
        std_avg /= len(col_names)
        if std_avg < -1:
            std_avg = -1
        elif std_avg > 1:
            std_avg = 1
        if absences > absence_cap:
            absences = absence_cap

        comp_score = (3 + 2 * std_avg) * absence_factor ** absences

        dataDF.at[i, "CompScore"] = comp_score

    return dataDF


def change_value(student_id, col_name, new_value):  # TODO
    raise Exception("Function not implemented yet!")

def add_student(student_name, student_id, ilearn1 = 0, ilearn2 = 0, attendance = 0, compscore = 0):  # TODO
    raise Exception("Function not implemented yet!")


def delete_student(student_id):  # TODO
    raise Exception("Function not implemented yet!")


dataDF = calc_score()
dataDF.sort_values(by=[sort_by], axis=0, ascending=False, inplace=True)

print(dataDF)


