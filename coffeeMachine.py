from coffeeMAchine_data import MENU, resources
money = 0

making_coffee = True
def getList(dict):
    return [*dict]

drinks = getList(MENU)
def calculate_coins(drink ,quarters,dimes, nickels, pennis):
    global money
    sum_quarters = quarters * 0.25
    sum_dimes = dimes * 0.10
    sum_nickles = nickels * 0.05
    sum_pennis = pennis * 0.01
    sum = sum_quarters + sum_dimes + sum_nickles + sum_pennis
    cost = MENU[drink]['cost']
    if sum < cost : 
        print("Sorry, thats not enough money. Money refunded")
    else:
        money += cost
        change = sum - cost
        print(f"Here is ${change} in change. \nHere is your {drink}☕. Enjoy!")

def calculate_is_enough(drink):
    for item in MENU[drink]['ingredients']:
        if resources[item] < MENU[drink]['ingredients'][item] :
            print(f"Sorry not enough {item}")
            return False
        else: 
            resources[item] -= MENU[drink]['ingredients'][item]
    return True


while making_coffee:
    user_choice = input("What would you like? (Espresso\ Latte\ Cappuccino): ").lower()
    if user_choice in drinks: 
        if calculate_is_enough(user_choice):
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickels = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            calculate_coins(user_choice, quarters, dimes, nickels, pennies)

    if user_choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${money}")
    elif user_choice == "off":
        making_coffee = False
    

