import menu
import monye
import maker
munes=menu.Menu()
makeros=maker.CoffeeMaker()
money_machine=monye.MoneyMachine()
money_machine.report()
makeros.report()
on=True
while on==True:
    ui=munes.get_items()
    ori=input(f"what coffe would you like?? ({ui})\n")
    see=munes.find_drink(ori)
    if  makeros.is_resource_sufficient(see):
        makeros.make_coffee(see)
    else:
        print(f"the resourses isnt {makeros.is_resource_sufficient(see)} enough try a diffrent drink or would you like to see report\n")
        