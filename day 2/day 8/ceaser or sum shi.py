letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
d=input("decode or encode??\n")
text=input("write child\n")
shift=int(input("how much shift??\n"))
l=len(text)
def encrypt(text):
    for i in range(shift,l):
        letter[i]=text[i]
    print(text)
encrypt(text)