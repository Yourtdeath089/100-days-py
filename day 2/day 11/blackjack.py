import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_card=[random.choice(cards),random.choice(cards)]
com_cards=[random.choice(cards),random.choice(cards)]

def cal(user_card):
    s=0
    for i in user_card:
        s+=i
        nuser=user_card
        return nuser



print(user_card)
j=True
while sum(user_card)<21 and j==True :
    p=0
    draw=input("would you like to draw card")
    if draw=="yes":
       p+1 
       if p==0:
           (user_card).append(random.choice(user_card))
           print(user_card[0],user_card[1],user_card[2])
       if p==1:
         (user_card).append(random.choice(user_card))
         print(user_card[0],user_card[1],user_card[2],user_card[3])
    if sum(user_card)>21:
        print("you lose")
    if sum(user_card)<21:
        draw=input("would you like to draw card")
    if draw=="yes":
        (user_card).append(random.choice(user_card))
    if sum(com_cards)<sum(user_card) and sum(user_card)<21:
        print("you win")
        j=False    

print(user_card)