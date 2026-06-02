
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
off=False
while off==False:

    order=(input("waht order would you like\n"))
    if order in MENU:
    

        s=MENU[order]
        wate=s["ingredients"]
        cos=s["cost"]
        tt=wate["water"]
        coff=wate["coffee"]
        def cal(wate):
            for i in wate:
                if resources[i]<wate[i]:
                    return False

        if order!="espresso":
            mil=wate["milk"]
        cen=3
        nic=2
        dolatte=23
        money=(0.25*cen,0.12*nic,1*dol)
        re=(sum(money))-cos

        if cos>sum(money):
            print("you poor loser me fr fr")
        if cal(wate) is False:
            print("not enough resourses")
        else:
            if order!="espresso":
                rm=resources["milk"]-mil
            rw=resources["water"]-tt
            rc=resources["coffee"]-coff
            print(f"you paid your return value is{re} ")
    if order not in MENU:
        print("the order isnt on the menu")
    ag=input("would you like to go again or see the report??\n")
    if ag=="report":
        print(rm , rc , rw , money )
    if ag=="n":
     off=True
    
print(sum(money))
