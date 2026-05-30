from game_data import data
import random
game_over=False
def new():
    so=data[random.randint(0,50)]
    name=so["name"]
    follow=so["follower_count"]
    country=so["country"]
    description=so["description"]
while game_over==False:
    so=data[random.randint(0,50)]
    name=so["name"]
    follow=so["follower_count"]
    country=so["country"]
    description=so["description"]
    do=data[random.randint(0,50)]
    name2=do["name"]
    follow2=do["follower_count"]
    country2=do["country"]
    description2=do["description"]
    print(f"compare A :{name}, a {description},from {country}")
    print(f"compare B :{name2}, a {description2},from {country2}")
    p=input("higer or lower H or L").lower()
    if p=="h" and follow2>follow:
        do=so
        new()
    elif p=="l" and follow2<follow:
        do=so
        new()
    else:
        print("game over")
        game_over=True


# rando=(random.randint[0,100])

# random_key = random.choice(list(data.keys()))
# random_item = data[random_key]
# print(random_item)  # {'name': 'Instagram', 'followers': 400

