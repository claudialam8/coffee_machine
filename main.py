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


def resource_data(resource):
    """Prints resources data"""
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    if "money" in resource:
        money = resource["money"]
        return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"
    else:
        return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g"


# TODO: format data and check resources
def check_resources(drink):
    """Prints what resources are available"""
    # to avoid error out cuz espresso does not contain milk
    if drink == 'espresso':
        MENU[drink]["ingredients"]["milk"] = 0
    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            resources[item] -= drink[item]
    return True


def insert_coins():
    """Asks user to insert coins"""
    print("Please insert coins")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    amount = round(float(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01), 2)
    print(f"amount inserted: S{amount}")
    return amount


profit = 0


def check_coins(drink):
    """Checks if the coins inserted is enough or not"""
    cost = MENU[drink]["cost"]
    accepted_amount = insert_coins()
    if accepted_amount >= cost:
        global profit
        profit += cost
        resources["money"] = profit
        change = accepted_amount - cost
        print(f"Here is ${change} in change")
    else:
        print("Sorry that's not enough money. Money refunded")


continue_coffee = True

while continue_coffee:
    user_wants = input("What would you like? (espresso/latte/cappuccino): ")
    if user_wants == "off":
        continue_coffee = False
    elif user_wants == "report":
        print(resource_data(resources))
    elif user_wants not in MENU:
        print("Try again")
    else:
        chosen_drink = MENU[user_wants]
        check = check_resources(chosen_drink["ingredients"])
        if check:
            check_coins(user_wants)
            print(f"Here is your {user_wants}. Enjoy!")

# TODO: Prompt user asking what would you like? Check user's input
# TODO: Turn off the machine by entering "off"
# TODO: print report: current resource values
# TODO: check resources are sufficient
# TODO: process coins
# TODO: check if transaction is successful
# TODO: Make coffee
# TODO: Give Coffee to user
