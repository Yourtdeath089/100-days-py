class Quizbrain:
    def __init__(self,q):
        self.ques_num=0
        self.question_list=q
    def next_question(self):
        text= self.question_list[self.ques_num]
        self.ques_num+=1
        input(f"Q{self.ques_num} {text}true or false\n")



























# import classs
# ques_num=0
# question_list=classs.data
# over=False
# score=0
# while over==False or ques_num>11:
#     print(question_list[ques_num])
#     print(question_list[ques_num+1])
#     ques_num+=1
#     user=input("true or false\n")
#     if user==question_list[ques_num+1]:
#         score+=1
#     else:
#         print("over")
#         over=True
