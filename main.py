from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Creating a variable to store the Money Machine class in
money_machine = MoneyMachine()
#Creating a variable to store the coffee maker class in
coffee_machine = CoffeeMaker()
#Creating a variable to store the menu class in
menu = Menu()
#The machine's on/off status
is_on = True

#Generating a report showing the money in the machine and the resources if the user asks for it
money_machine.report()
coffee_machine.report()


while is_on:
    options = menu.get_items()
    choice = input(f"What will you have? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        #Generating a report showing the money in the machine and the resources if the user asks for it
        money_machine.report()
        coffee_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and print(money_machine.make_payment(drink.cost)):
            coffee_machine.make_coffee(drink)



