# for key in dictionary
#   print(key)
#   print(dict[key])


student_scores={
    "Harry": 81,
    "Ron":78,
    "Hermione": 99,
    "Draco":74,    
    "Neville": 62,
}

student_grades = {}

for i in student_scores:
    scores = student_scores[i]
    if scores > 90 and scores <=100:
        student_grades[i]= "Outstanding"
    elif scores > 80 and scores <=90:
        student_grades[i]= "Exceeds Expectations"
    elif scores > 70 and scores <=80:
        student_grades[i]= "Acceptable"
    else:
        student_grades[i]="Fail"


print(student_grades)