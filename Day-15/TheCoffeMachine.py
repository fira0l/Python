from Dictionary import MENU,resources

is_off = False

def turn_off():
    global is_off
    is_off = True
    return is_off

def Report():
    coffee = resources["coffee"]
    water = resources["water"]
    milk = resources["milk"]
    
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    # print(f"Coffee: ${MENU[users_choice]["cost"]}")

def Users_order_handler(user_choice):
    if user_choice == "latte" or user_choice == "cappuccino":
        water = int(resources["water"])- int(MENU[user_choice]["ingredients"]["water"])
        coffee = int(resources["coffee"])- int(MENU[users_choice]["ingredients"]["coffee"])
        milk = int(resources["milk"]) - int(MENU[user_choice]["ingredients"]["milk"])
        cost = MENU[user_choice]["cost"]
    elif user_choice == "espresso":
        water = int(resources["water"])- int(MENU[user_choice]["ingredients"]["water"])
        coffee = int(resources["coffee"])- int(MENU[users_choice]["ingredients"]["coffee"])
        cost = MENU[user_choice]["cost"]
    print(f"water: {water}")        
    print(f"coffee: {coffee}")
    print(f"milk: {milk}")
    print(f"cost: {cost}")

    
#Prompt a user for a choice
users_choice = input("What Would u Like?(espresso/latte/cappuccino): ").lower()
#Turn off the coffe machine
if users_choice == "off":
    turn_off(users_choice)
elif users_choice == "report":
    Report()

Users_order_handler(users_choice)
#print Report
#check Resources Sufficient
#process coins
#check transaction successfull
#make a coffee
