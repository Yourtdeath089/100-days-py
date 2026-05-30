height=float (input("waht is your height\n"))
weight=int(input("waht is your weight\n"))
bmi=weight/height**2
print (round(bmi,2))
if bmi < 18.5:
    print(f" your bmi is {bmi}under weight",2)
elif bmi < 25:
    print( f"your bmi is {bmi} normal weight",2)
elif bmi < 32:
    print("your are fat")
else:
    print("dam son")