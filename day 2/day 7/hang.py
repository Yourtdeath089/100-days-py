#didnt complete.gonna do it tomorrow


import random
words=["ardvark","baboon","camel"]
p=random.choice(words)
print(p)
l=len(p)
g=[]
life=4
art=["1","@","3","4","5"]
for i in range(0,l):
     g+="_"
while not life==0 or not d==g :
 print(g)   
 input1=input("what letter would you like to guess??\n").lower()
 for i in range(0,l):
    if p[i]==input1:
     g[i]=input1
     if input1 in g:
       print ("you have already guessed the letter")
    if input1 not in g:
      life-1
      print(art[i])
print(g)

    
if life!=0:
  print("you win")      
print(g)