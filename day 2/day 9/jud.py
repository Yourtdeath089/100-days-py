import clear
all=[]
def player(name,money):
    new_dec={"nam":name,"bid":money}
    all.append(new_dec)
    print(new_dec)
    tit=0
    win=()
    if bid>tit:
        tit=bid
        win=name

o="yes"
while o=="yes":
    char=input("name?\n")
    bid=int(input("money??\n"))
    os=input("would you like to continue??\n").lower()
    if os=="no":
        o="tity"
    clear()
    player(char,bid)