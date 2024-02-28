#Dictionary containing the menu and resources for the coffee machine
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

#The moneybox for the coffee machine is stored in this variable
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#A function to loop through the drink choices. Order ingredients is the value.
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, but this machine currently lacks the required amount of {item} for that drink")
            return False
    return True           

#A function to process coins
def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

#A function to check that the user's payment went through
def is_transaction_successful(money_received, drink_cost):
    """Return true when they payment is accepted and vice-versa"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("That's not enough money for your order")
        return False

#A function to make the order
def make_order(drink_name, order_ingredients):
    """Deduct the required ingredients from the machine's resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


#Establishing that the machine is on
is_on = True

#While loop to ensure the prompt keeps coming up with the machine on
while is_on:
#Creating variable and storing the user's order in it
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    #If your input is 'off', this stops the above while loop and shuts down the coffee machine
    if choice == "off":
        is_on = False
    #If you input 'report', a list of machine resources will be printed    
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            #If they have enough money, they will be asked for the required funds below. A payment variable will hold their response.
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_order(choice, drink["ingredients"])

        
