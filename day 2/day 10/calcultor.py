def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    return n1/n2
def mul(n1,n2):
    return n1*n2
s=True    
oper={"+":add,"-":sub,"/":div,"*":mul}
num1=float(input("number"))
num2=float(input("number"))
for i in oper:
    print(i)
opt=(input("sign"))
cal=oper[opt]
answer=cal(num1,num2)
print(f"{num1} {opt} {num2}={answer}")
con=input("would you like to continue??\n")
print(answer)
while s==True:
    if con=="n":
        s="n"
    else:
        opt=(input("sign"))
        cal=oper[opt]
        num3=float(input("num"))
        answer2=cal(answer,num3)
        print(f"{answer} {opt} {num3}={answer2}")
        con=input("would you like to continue??\n")
        if con=="n":
            s="n"
        print(answer2)