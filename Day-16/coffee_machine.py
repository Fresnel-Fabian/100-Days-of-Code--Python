MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients":{
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
profit = 0


# TODO.1: ask user what they want
def main():
    run = True
    while run:
        user_input = input("What would you like? (espresso/latte/cappucino): ")
        if user_input == "off":
            run = False
        elif user_input == "report":
            print(f"Water: {resources.get('water')}\nMilk: {resources.get('milk')}\nCoffee: {resources.get('coffee')}"
                  f"\nMoney: {profit}")
        else:
            drink = MENU[user_input]
            if sufficient_resources(drink["ingredients"]):
                payment = process_coins()
                if transaction(payment, drink["cost"]):
                    brew(drink["ingredients"])
                    print(f"Here is your balance {round(payment - drink['cost'], 2)}")
                    print(f"Enjoy Your {user_input}")


# TODO.2: create brew function
def brew(beverage):
    global resources
    for item in beverage:
        resources[item] -= beverage[item]


# TODO.3: function to check if resources is sufficient
def sufficient_resources(drink_recipe):
    for ingredient in drink_recipe:
        if resources[ingredient] < drink_recipe[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
            return True
        

# TODO.4: function to process coin
def process_coins():
    quarter = 0.25 * int(input("How many quarters: "))
    dimes = 0.1 * int(input("how many dimes: "))
    nickles = 0.05 * int(input("How many nickles: "))
    pennies = 0.01 * int(input("How many pennies: "))
    return quarter + dimes + nickles + pennies


# TODO.5: function to check if payment is solid
def transaction(payment, drink_cost):
    if payment >= drink_cost:
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
if __name__ == "__main__":
    main()
