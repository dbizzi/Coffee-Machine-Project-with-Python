from resources import resources
from menu import MENU


def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


def can_make_drink(beverage):
    for key in MENU[beverage]["ingredients"]:
        if resources[key] < MENU[beverage]["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            return False
        else:
            return True


def make_drink(beverage):
    resources["water"] -= MENU[beverage]["ingredients"]["water"]
    resources["coffee"] -= MENU[beverage]["ingredients"]["coffee"]
    if beverage != "espresso":
        resources["milk"] -= MENU[beverage]["ingredients"]["milk"]


def add_coins(my_coins):
    resources["coins"] += my_coins
    print(round(resources["coins"],2))


def remove_coins(beverage):
    resources["coins"] -= MENU[beverage]["cost"]
    if resources["coins"] < 0:
        resources["coins"] -= resources["coins"]
        return False
    else:
        make_drink(beverage)
        resources["money"] += MENU[beverage]["cost"]
        print(f"Here is ${round(resources["coins"], 2)} dollars in change")
        resources["coins"] -= resources["coins"]
        return True


def turn_off():
    print("Coffee Machine is off")
    return True
