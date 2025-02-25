from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# TODO 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino/):​
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

# TODO 2. Turn off the Coffee Machine by entering “​off​ ” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the
# machine. Your code should end execution when this happens.

# TODO 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows the
# current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough resources
# to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not
# continue to make the drink but print: “​Sorry there is not enough water.​ ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# TODO 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
machine_menu = Menu()
money_transaction = MoneyMachine()

is_on = True
while is_on:
    user_choice = input(f"What would you like? ({coffee_menu.get_items()}): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()  
        money_transaction.report() 
    else:
        user_order = machine_menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(user_order) and \
            money_transaction.make_payment(user_order.cost):
            coffee_maker.make_coffee(user_order)
            