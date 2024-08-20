from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
import json

# Importing ingredients
from ingredients import INGREDIENTS, COFFEE_TYPES

class Coffee():

    def __init__(self, ctype):
        self.coffeeType = ctype
        self.ingredients = INGREDIENTS[(self.coffeeType).lower()]['ingredients']
        self.cost = INGREDIENTS[(self.coffeeType).lower()]['cost']
        print(self.ingredients)
        print(self.cost)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sliding Sidebar Example")
        self.setGeometry(550, 150, 800, 800)

        self.image_path = "Data/coffee_2.jpg"
        self.pixmap = QPixmap(self.image_path)
        self.scaled_pixmap = None

        # Defining variables using thoughoutly in the code
        self.Coffee = None
        self.money = 0
        self.resources = None

        # Importing prebuild assets to machine
        self.addPredefinedItemsToMachine()
        
        # Add make Coffee button 
        self.add_makeCoffeeButton()

        # Hamburger button at the leftmost corner
        self.hamburger_button = QPushButton("☰", self)
        self.hamburger_button.setFixedSize(50, 50)
        self.hamburger_button.move(0, 0)
        self.hamburger_button.setStyleSheet("background-color: darkgray;")
        self.hamburger_button.clicked.connect(self.toggle_sidebar)

        # Sidebar
        self.sidebar = QWidget(self)
        self.sidebar.setGeometry(-200, 0, 200, self.height())
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar.setStyleSheet("background-color: lightblue;")

        self.sidebar_button = QPushButton("x", self.sidebar)
        self.sidebar_button.setFixedSize(40, 40)
        self.sidebar_layout.addWidget(self.sidebar_button)
        self.sidebar_button.clicked.connect(self.toggle_sidebar)
        self.sidebar_button.setStyleSheet("background-color: darkgray;")

        self.sidebar_button_1 = QPushButton("Sidebar Button", self.sidebar)
        self.sidebar_button_1.setStyleSheet("background-color: darkgray;")
        self.sidebar_layout.addWidget(self.sidebar_button_1)
        self.sidebar_layout.addStretch()

        # Sidebar animation
        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"geometry")

    def add_makeCoffeeButton(self):
        print("DEBUG: Inside get_makeCoffeeButton()")

        # Main button in the middle
        central_widget = QWidget()
        self.main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        self.makeCoffeeButton = QPushButton("Make coffee", self)

        self.makeCoffeeButton.setStyleSheet("""
            QPushButton {
                background-color: gray;
                color: white;
                border-radius: 20px; /* This makes the button rounded */
                padding: 10px 20px; /* Adjust padding  */
                font-size: 16px; /* Increase in font size */
                border: 2px solid #555; /* Added a border */
            }
            QPushButton:hover {
                background-color: #888; /* To hange background color on hover */
            }
            QPushButton:pressed {
                background-color: #666; /* To change background color when pressed */
            }
        """)

        self.makeCoffeeButton.clicked.connect(self.selectCoffeeType)
        self.main_layout.addWidget(self.makeCoffeeButton, alignment=Qt.AlignCenter)

        return
    
    def paintEvent(self, event):
        painter = QPainter(self)
        if not self.scaled_pixmap or self.scaled_pixmap.size() != self.size():
            self.scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        painter.drawPixmap(0, 0, self.scaled_pixmap)
        return


    def toggle_sidebar(self):
        if self.sidebar.x() == 0:
            self.sidebar_animation.setDuration(300)
            self.sidebar_animation.setStartValue(QRect(0, 0, 200, self.height()))
            self.sidebar_animation.setEndValue(QRect(-200, 0, 200, self.height()))
            self.sidebar_animation.start()
        else:
            self.sidebar_animation.setDuration(300)
            self.sidebar_animation.setStartValue(QRect(-200, 0, 200, self.height()))
            self.sidebar_animation.setEndValue(QRect(0, 0, 200, self.height()))
            self.sidebar_animation.start()
        return
    
    def addPredefinedItemsToMachine(self):
        print("Inside addPredefinedItemsToMachine")
        with open('predefined.json', 'r') as file:
            data = json.load(file)
        self.resources = data["ingredients"]
        self.money = data["money"]
        print("Resources : ", self.resources)
        print("Money: ", self.money)
        return

    def selectCoffeeType(self):

        self.makeCoffeeButton.hide()
        
        # Create a new widget with coffee selection options
        selection_widget = QWidget()
        selection_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 15px; padding: 10px;")
        selection_layout = QVBoxLayout()
        
        # Message label
        message_label = QLabel("Select coffee type")
        message_label.setAlignment(Qt.AlignCenter)
        message_label.setStyleSheet("background-color: darkgray; color: white; padding: 20px 30px; border-radius: 10px;")

        selection_layout.addWidget(message_label)
        # List of coffee options
        coffee_types = ["Espresso", "Latte", "Cappuccino", "Americano"]
        
        # Add coffee option buttons
        for coffee in coffee_types:
            button = QPushButton(coffee)

            button.setStyleSheet("""
            QPushButton {
                    background-color: gray;
                    color: white;
                    border-radius: 20px; /* This makes the button rounded */
                    padding: 10px 20px; /* Adjust padding  */
                    font-size: 16px; /* Increase in font size */
                    border: 2px solid #555; /* Added a border */
                }
                QPushButton:hover {
                    background-color: #888; /* To hange background color on hover */
                }
                QPushButton:pressed {
                    background-color: #666; /* To change background color when pressed */
                }
            """)

            button.clicked.connect(lambda checked, coffee=coffee: self.prepareCoffee(coffee))
            selection_layout.addWidget(button)
        
        selection_widget.setLayout(selection_layout)
        
        self.main_layout.addStretch(3)
        self.main_layout.addWidget(selection_widget, alignment=Qt.AlignCenter)
        self.main_layout.addStretch(2)

    def prepareCoffee(self, coffee_type):
        print(f"Preparing {coffee_type}...")
    
    def setCoffeeType(self, coffee):
        self.Coffee = Coffee(coffee)
        print("Type of coffee choosen :", self.Coffee.coffeeType)
        #Callinh checingredients to check if have minimum ingredients.
        self.checkIngredients()
    
    def checkIngredients(self):
        print("Inside Check Ingredients")
        is_avail = True
        for ingredient in INGREDIENTS[self.Coffee.coffeeType.lower()]["ingredients"]:
            print(ingredient)
            if int(self.resources[ingredient]) < int(self.Coffee.ingredients[ingredient]):
                print("Not enough Ingredients")
                msg = QMessageBox()
                msg.setText("No Ingredients Available")
                msg.exec_()
                is_avail = False
                return
        if is_avail:
            self.getAndProcessMoney()
        return
    
    def getAndProcessMoney(self):
        msg = QMessageBox()
        msg.setText(f"The cost of coffee is: {self.Coffee.cost}")
        msg.exec_()
        return

    def buttonClicked(self):
        print("Button Clicked")
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
