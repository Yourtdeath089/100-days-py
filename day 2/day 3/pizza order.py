size=input("what size of pizza would you like, L , M , S\n")
perper=input("would you like peper Y , N ??\n")
cheese=input("WOULD YOU LIKE EXTRA CHEESE Y , N??\n")
bill=0
if size=="L":
    bill+=25
if size=="M":
    bill+=20
if size=="S":
    bill+=15
if perper=="Y":
    bill+=3
if cheese=="Y":
    bill+=2
print(bill)