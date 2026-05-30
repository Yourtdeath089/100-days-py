row1=("X" , "X" , "X")
row2=("X" , "X" , "X")
row3=("X" , "X" , "X")
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
hidden=(input("where you like to hide??\n"))
horizontal=int (hidden[0])
vertical= int(hidden[1])
map[vertical-1][horizontal-1]="Y"
print(f"{row1}\n{row2}\n{row3}\n")