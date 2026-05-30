# score=input("what are students height??\n").split()
# for n in range (0, len(score)):
#     score[n]=int(score[n])
# print(score)
#learn loops again from a video or a tutorial make something from the loop hard and long

score=input("what are the score\n").split()
for n in range(0,len(score)):
    score[n]=int(score[n])
print(score)
total_score=0
for mark in score:
    if total_score<mark:
     score=mark
print(score)
