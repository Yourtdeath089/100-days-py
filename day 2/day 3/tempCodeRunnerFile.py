import random
words=["ardvark","baboon","camel"]
p=random.choice(words)
print(p)
l=len(p)
d=[]
g=[]
life=4
lives=4
art=["1","@","3","4","5"]
for i in range(0,l):
     g+="_"
while not life==0 and life>0 :
 print(g)   
 input1=input("what letter would you like to guess??\n").lower()
 
 if input1 in g:
  print("you have already guessed the letter")
 for i in range(0,l):
     if p[i]==input1:
         g[i]=input1
 if input1 not in p:
      print(f"{input1} is not in the words")
      life-=1
      print(art[life])
print(g)

    
if life!=0:
  print("you win")      
print(g)


















