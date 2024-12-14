# Contains code of coffee machine

''' TODOs:

*  Write menu, resources, conditions. - Done
* Wrtie startup menu - Done
*  Write Code for machine.
*  Wrtie and test edge condtitions.

'''

import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":100,
            "coffee": 18,
        },
        "cost": 25,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 50,
        },
        "cost": 50,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 100,
}

# TODO: Add multiple money options
# money = {
#     1 : 20,
#     5 : 5,
#     10 : 5, 
#     100 : 5
# }


class CoffeeMachine:

    def __init__(self):
        self.coffee = None
        self.money = 100
        

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
        self.coffee = (input('\n:')).lower()
        if self.coffee not in MENU.keys():
            if trys > 1 :
                print("Sorry, Available Drinks are : ")
                trys -= 1
                self.showMenu(trys)
            else:
                print("Please Run the program again.")
        if self.areEnoughIngredients():
            self.doTransaction()

    def areEnoughIngredients(self):
        passed = True
        if self.coffee is None:
            print("Coffee type not choosen")
            return
        
        required_resources = MENU[self.coffee]["ingredients"]
        for each_res in required_resources:
            if required_resources[each_res] > resources[each_res]:
                print("Not enough resource to make ", self.coffee)
                print('Lacked Resource :', each_res, "\nPresent : ", resources[each_res], "\nRequired : ", required_resources[each_res])
                passed = False
            
        return passed
    
    def doTransaction(self, trys = 3):
        
        print('Cost of the coffee will be : ', MENU[self.coffee]["cost"])
        # print("Please enter your amount as 1, 5, 10, 100")
        print("Please enter your amount")
        total_amount = int(input())
        # ones, fives, tens, hundrends = int(input().split(" "))
        # total_amount = ones + 5 * fives + 10*tens + 100*hundrends

        if total_amount < MENU[self.coffee]["cost"]:
            print("The given amount is not enough. \nRequired amount:", MENU[self.coffee]["cost"], "\nReceived amount:", total_amount)
            print("Please Enter the amount again")
            return
            # TODO: Wrtie a code with tries...
            # if trys > 1:
            #     trys -= 1
            #     self.doTransaction(trys)
            # else:
            #     print("Maximum tries are finished, please try again.")
            #     return
        elif total_amount > MENU[self.coffee]["cost"]:
            # TODO: Enter case if amount we have not enough to return exchange
            print("Here is your remaining amount : ", total_amount - MENU[self.coffee]["cost"])
            self.money = self.money + MENU[self.coffee]["cost"]
            print("Present Money : ", self.money)
        else :
            self.money = self.money + total_amount
            print("Present Money :", self.money)
        
        self.makeCoffee()

    def makeCoffee(self):
        print("\n   Please wait your coffee is getting ready !!!  \n")
        time.sleep(2)
        for each_ingredients in MENU[self.coffee]["ingredients"]:
            resources[each_ingredients] -= MENU[self.coffee]["ingredients"][each_ingredients]
            print(resources[each_ingredients])
        print("\n\n\n -- Here is your coffee -- \n\n\n")
        is_enough = self.checkIngredients()
        if is_enough :
            print("Is there anything would you like to have ?")
            is_anything = input("Please enter yes/no\n")
            if is_anything == 'yes':
                self.startupMenu()
            else:
                print("Thank you for the transaction !! Please come again.")
                return
        else:
            print("Sorry, we are short on resources. We will open again soon.")
            print("                 Thank you !!!               ")

    
    def checkIngredients(self):
        isEnoughIngredients = True
        for each_ingredients in resources:
            if resources[each_ingredients] < MENU["espresso"]["ingredients"][each_ingredients]:
                print("####################### Warning ########################")
                print(f"   No enough {each_ingredients} to make any coffee ")
                print("--------------------------------------------------------")
                print("Resources present : ")
                isEnoughIngredients = False
                self.showResources()
        return isEnoughIngredients

    def showResources(self):
        for each_ingredients in resources:
            print(each_ingredients, ':', resources[each_ingredients])

    def reFillResources(self):
        ingredient = input("What you would like to refill ?\n")
        if ingredient in resources.keys():
            amount = int(input(f"Enter amount of {ingredient}\n"))
            resources[ingredient] += amount
        else :
            print("No such ingredients.")
        
        loop = input("Do you need to refill anything else ?")
        if loop == "yes":
            self.reFillResources()
        else :
            print("Thanks for refilling \nCurrent ingredients :")
            self.showResources()


def main():
    coffee = CoffeeMachine()
    coffee.startupMenu()
    # print(coffee.areEnoughIngredients())
    # if coffee.areEnoughIngredients():
    #     coffee.doTransaction()



if __name__ == "__main__":
    main()
