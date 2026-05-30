student_score={
    "harry":81,
    "ron":78,
    "hermonie":99,
    "darco":74,
    "neville":2,}
for s in student_score:
    if student_score[s]>=91:
        student_score[s]="best" 
        print(student_score[s])
    elif student_score[s]>=81 and student_score[s]<=90:
         student_score[s]="okie" 
         print(student_score[s])
    elif student_score[s]>=71 and student_score[s]<=80:
         student_score[s]="avarage" 
         print(student_score[s])
    elif student_score[s]<70:
         student_score[s]="fail" 
         print(student_score[s])
print(student_score)