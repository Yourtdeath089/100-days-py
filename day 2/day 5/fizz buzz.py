
for i in range(1, 16):
 con1=i%3==0 and i%5!=0
 con2=i%5==0 and i%3!=0
 if i%3==0 and i%5==0:
  print("fizz buzz")
 if con1:
   print("fizz")
 if con2:
    print("buzz")
 elif i%3!=0 and i%5!=0:
  print(i)