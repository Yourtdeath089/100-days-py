class question:
    def __init__(self, new_q,new_a):
        self.text=new_q
        self.ans=new_a
import questionss
from quiz import Quizbrain
ques=questionss.question_data
data=[]
for i in ques:
    data_ques=i["text"]
    data_ans=i["answer"]
    new_q=question(data_ques,data_ans)
    data.append(new_q)
    qq=Quizbrain(data)
    qq.next_question()
    
































