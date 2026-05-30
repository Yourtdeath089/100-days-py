import random
letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
symbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
    '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
    '_', '`', '{', '|', '}', '~']
# d=""
# input=2
# for a in range(0,input):
#  r=random.randint(0,len(symbols)-1)
#  d+=symbols[r]
# input2=5
# l1=""
# for a in range(0,input2):
#  l=random.randint(0,len(letter)-1)
#  l1+=letter[l]
# print(l1+d)
d=[]
input1=3
input2=4
for a in range (1,input1+1):
    d. append(random.choice(symbols))
for a in range (1,input2+1):
    d+=random.choice(letter)
print(d)
random.shuffle(d)
print(d)
passo=""
for a in d :
    passo+=a
print(passo)