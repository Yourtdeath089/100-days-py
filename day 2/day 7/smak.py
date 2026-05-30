import random
words=["ardvark","baboon","camel"]
p=random.choice(words)
print(p)
l=len(p)-1
input1="a"
life=3
for i in p:
  if i==input1:
    print("yes")
  else:
    print("wrong")
# for loop will go in any str and seprate them automatically.for firse padhle 
#for (i) in p : you have to give what it has to loop through in last value
#i is for the number of loop it will perform it can also be used for value and will change according to the letters in the
# word or the list veriables/items 
