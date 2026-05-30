# int(input("which year would you like to check??\n"))
# year=20099
# if year%4==0:
#     print("leap year")
# elif year%100!=0:
#     print("leap year")
# elif year%400==0:
#     print("leap year")
# else:
#     print("not a leap year")
year=int(input("which year would you like to check??\n"))
if year%400==0:
    print("leap year")
elif year%100==0:
    print(" not a leap year")
elif year%4==0:
    print("leap year")
else:
    print("not a leap year")



