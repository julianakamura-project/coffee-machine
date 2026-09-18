from art import logo
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

current_money = 0.0

def print_report():
    print(f"\nWater: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${current_money:.2f}\n")

def check_resources(order):
    if (MENU[order]['ingredients']['water'] > resources['water']
            or MENU[order]['ingredients']['milk'] > resources['milk']
            or MENU[order]['ingredients']['water'] > resources['water']):
        return False
    else:
        return True

def consume_ingredients(order):
    global resources
    for item in resources:
        resources[item] = resources[item] - MENU[order]['ingredients'][item]

def check_money(order, penny, nickel, dime, quarter):
    global current_money
    total_money = penny * 0.01 + nickel * 0.05 + dime * 0.1 + quarter * 0.25
    if total_money < MENU[order]['cost']:
        return False, 0
    elif total_money >= MENU[order]['cost']:
        money_change = total_money - MENU[order]['cost']
        current_money += MENU[order]['cost']
        return True, money_change

def return_missing(order):
    missing_resources = []
    for item in MENU[order]['ingredients']:
        if MENU[order]['ingredients'][item] > resources[item]:
            missing_resources.append(item)
    if len(missing_resources) == 1:
        print(f"Sorry there is not enough {missing_resources[0]}")
    elif len(missing_resources) == 2:
        print(f"Sorry there is not enough {missing_resources[0]} and {missing_resources[1]}")
    else:
        print(f"Sorry there is not enough {missing_resources[0]}, {missing_resources[1]} and {missing_resources[2]}")

off = False
print(logo)
while not off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == 'off':
        off = True
        continue

    elif user_choice == 'report':
        print_report()
        continue

    elif user_choice not in MENU:
        print("\nPlease input a valid command.\n")
        continue

    elif check_resources(user_choice):
        print("\nPlease insert coins.\n")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        enough, change = check_money(user_choice, pennies, nickels, dimes, quarters)

        if enough:
            consume_ingredients(user_choice)
            if change != 0:
                print(f"\nHere is ${change:.2f} in change.")
            print(f"\nHere is your {user_choice}. Enjoy!\n")
            time.sleep(5)
            print("\n" * 20)
            print(logo)

        elif not enough:
            print("\nSorry that's not enough money. Money refunded.")

    else:
        return_missing(user_choice)