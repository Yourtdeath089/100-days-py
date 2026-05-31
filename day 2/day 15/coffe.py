
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}
order=(input("waht order would you like"))

s=MENU[order]
wate=s["ingredients"]
cos=s["cost"]
tt=wate["water"]
coff=wate["coffee"]
if order!="espresso":
    mil=wate["milk"]
cen=3
nic=2
dol=23
money=(0.25*cen,0.12*nic,1*dol)
re=(sum(money))-cos
resou=sum()
if cos>sum(money):
    print("you poor loser me fr fr")
if sum(resou)<sum(mil,tt,coff):
    print("not enough resourses")
else:
    if order!="espresso":
        resources["milk"]-mil
    resources["water"]-tt
    resources["coffee"]-coff
    print(f"you paid your return value is{re} ")
print(sum(money))
