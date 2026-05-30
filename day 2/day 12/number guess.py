import random
print("welcome to the number guessing game!!\n i am thinking a number from 1 to 100.")
num=random.randint(0,100)
diff=input("chose the difficulty hard or easy\n")
if diff=="easy":
    lives=10
elif diff=="hard":
    lives=5
game_over=False
while lives!=0 and game_over is False :

    print(f"you have {lives} attempts to guess the number")
    guess=int(input("make a guess"))
    def cal(guess):
        if guess>num:
            print("too high")
        elif num>guess:
            print("too low")
        elif num==guess:
            print("you guessed right you win")
        
    cal(guess)
    if guess!=num:
        lives-=1
    elif num==guess:
        game_over=True
if lives==0:
    print(f"you lose the number was {num}")