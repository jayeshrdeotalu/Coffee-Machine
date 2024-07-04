# Contains code of coffee machine

''' TODOs:

*  Write menu, resources, conditions. - Done
* Wrtie startup menu - Done
*  Write Code for machine.
*  Wrtie and test edge condtitions.

'''

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

money = {
    1 : 20,
    5 : 5,
    10 : 5, 
    100 : 5
}


class CoffeeMachine:

    def startupMenu(self):
        print("---------------------------------")
        print("|                                |")
        print("|   Welcome to Coffee Machine!!  |")
        print("|                                |")
        print("---------------------------------")

        print("What would you like to have?")
        trys = 3
        self.showMenu(trys)  

    def showMenu(self, trys):
        for each_coffee in MENU:
            print(each_coffee, end= ", ")
            # TODO : Add Add-ups, like extra milk or something
        choosen_coffee = (input('\n:')).lower()
        if choosen_coffee not in MENU.keys():
            if trys > 1 :
                print("Sorry, Available Drinks are : ")
                trys -= 1
                self.showMenu(trys)
            else:
                print("Please Run the program again.")

coffee = CoffeeMachine()
coffee.startupMenu()