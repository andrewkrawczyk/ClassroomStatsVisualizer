import os.path

import pandas as pd
from django.db.models import F
from django.db.models import Max

from TeacherApp.models import *

s_data = Student.objects.filter(teacher=8861)
dra_data = Dra.objects.annotate(max_date=Max('student__dra__entry_date')).filter(entry_date=F('max_date'))\
    .filter(student__teacher__teacher_id=8861)
math_data = Ireadymath.objects.annotate(max_date=Max('student__ireadymath__entry_date'))\
    .filter(entry_date=F('max_date')).filter(student__teacher__teacher_id=8861)
reading_data = Ireadyreading.objects.annotate(max_date=Max('student__ireadyreading__entry_date'))\
    .filter(entry_date=F('max_date')).filter(student__teacher__teacher_id=8861)

# ~~~~ CONFIGS ~~~~
# Change to sort by whichever column you want
sort_by = "CompScore"
# Scaling factor for unexcused absences
absence_factor = 0.95
# Cap for number of absences
absence_cap = 5
dataDF = pd.read_csv('Algorithm_Comp_Score/test/testdata.csv')

# Holds mean, sd
statsDF = dataDF.describe()

adjDF = dataDF.copy()

col_names = ["Reading", "Ilearn_1", "Ilearn_2"]

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

dataDF.sort_values(by=[sort_by])
print(statsDF)
print(adjDF)
print(dataDF)

input("Press [Enter] to continue.")
