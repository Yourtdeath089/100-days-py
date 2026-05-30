b=float(input("how much is the bill??\n"))
t=float(input("how much would you like to tip 12,13,custom\n"))
p=int(input("how many people are their\n"))
tip_total=round(t/100*b + b ,2)
bill_payble=round(tip_total/p,2)
print(bill_payble)











# p=int(persons)
# b=int(bill)
# t=int(tip)
# total_without_bil=b*t//100
# total=b,+total_without_bil
# split=(bas/p)
# print(f"each person should pay {split}")
