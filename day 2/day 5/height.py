student_height=input("what are students height??\n").split()
for n in range(0, len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)
total_height=0
for s in student_height:
    total_height+=s
num=0
for a in student_height:
    num+=1
print(round(total_height/num))


       
    


