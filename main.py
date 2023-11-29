from machine_actions import report, can_make_drink, turn_off, add_coins, remove_coins

off = False

while not off:
    user_action = input("What would you like? (espresso/latte/cappuccino):").lower()

    if user_action == "report":
        report()
    elif user_action == "espresso" or user_action == "latte" or user_action == "cappuccino":
        drink = can_make_drink(user_action)
        if drink:
            add_coins(int(input("Insert quarters coins: ")) * 0.25)
            add_coins(int(input("Insert dimes coins: ")) * 0.10)
            add_coins(int(input("Insert nickels coins: ")) * 0.05)
            add_coins(int(input("Insert pennies coins: ")) * 0.01)
            result = (remove_coins(user_action))
            if result:
                print(f"Here is your {user_action}☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded")

    elif user_action == "off":
        machine_off = turn_off()
        off = machine_off
    else:
        print("Unavailable option, please select a valid option")
