rock='''    
     ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper='''
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''










# import random
# combination=([rock],[scissor],[paper])
# h=int(input("type 1 for rock 2 for scissor 3 for paper\n"))
# d=h-1
# c=random.randint(0,2)
# if d<=4:
#     print("are you retarted?")
# if c==d:
#      print("draw")
#      print (combination [c], combination[h])

# elif c==d-1 or c<d-1 or c==d-2:
#      print("you lose")
#      print (combination [c], combination[h])
# elif print (combination [c], combination[h]):
#      print("you win")
# else:
#   print("retarted")




import random
combination=([rock],[scissor],[paper])
h=int(input("type 1 for rock 2 for scissor 3 for paper\n"))
d=h-1
c=random.randint(0,2)
print (combination [c], combination[d])
if c==d:
 print("draw")
elif c==d-1 or c<d-1 or c==d-2:
 print("you lose")
else:
 print("you win")








# elif (c[0],h[2] ) or (c[1],h[2]) or (c[2],h[0]):
#  print("you lose")
# else:
#  print("you winnnnnnnnnnn")