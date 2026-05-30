import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card=random.choice(cards),random.choice,random.choice(cards),random.choice,random.choice(cards),random.choice
com_cards=random.choice(cards),random.choice(cards)
def cal():
    s=0
    if s==0:
        s+1
        return user_card[0]+user_card[1]
    if s==1:
         s+1
         return user_card[0]+user_card[1]+user_card[2]
    if s==2:
         s+1
         return user_card[0]+user_card[1]+user_card[2]+user_card[3]



j=True
while cal()<21 and j==True :
    p=0
    draw=input("would you like to draw card")
    if draw=="yes":
       p+1 
       if p==0:
           print(user_card[0],user_card[1],user_card[2])
       if p==1:
         print(user_card[0],user_card[1],user_card[2],user_card[3])
    if cal()>21:
        print("you lose")
    if com_cards<user_card and user_card<21:
        print("you win")
        j=False    

print(user_card)
