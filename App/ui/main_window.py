from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import sys
import json

# Importing ingredients
from App.libs.ingredients import INGREDIENTS, COFFEE_TYPES

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
        self.sidebar_width = 200  # To make it dynamic and can handle errors
        self.current_page_index = 0

        #initialising central widget and main layout 
        central_widget = QWidget()
        self.main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        self.background_image_path = "App/resources/coffee_2.jpg"
        self.pixmap = QPixmap(self.background_image_path)
        self.scaled_pixmap = None

        # Defining variables using thoughoutly in the code
        self.Coffee = None
        self.money = 0
        self.resources = None

        # Importing prebuild assets to machine
        self.addPredefinedItemsToMachine()
        # Add sidebar to main window
        self.add_sidebar()

        # Create Stack Widget for paging...
        self.stacked = QStackedWidget()
        self.stacked.addWidget(self.create_main_page())
        self.stacked.addWidget(self.create_coffee_type_page())
        # self.stacked.addWidget(self.create_payment_page())
        # self.stacked.addWidget(self.create_brewing_page())
        
        self.main_layout.addWidget(self.stacked)
        self.stacked.setCurrentIndex(self.current_page_index)


    def add_sidebar(self):
        print("DEBUG: Inside add_sidebar()")

        # Hamburger button at the leftmost corner
        self.hamburger_button = QPushButton("☰", self)
        self.hamburger_button.setFixedSize(50, 50)
        self.hamburger_button.move(0, 0)
        self.hamburger_button.setStyleSheet("background-color: darkgray;")
        self.hamburger_button.clicked.connect(self.toggle_sidebar)

        # Sidebar
        self.sidebar = QWidget(self)
        self.sidebar.setGeometry(-self.sidebar_width, 0, self.sidebar_width, self.height())
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar.setStyleSheet("background-color: lightblue;")

        self.sidebar_button = QPushButton("x", self.sidebar)
        self.sidebar_button.setFixedSize(40, 40)
        self.sidebar_layout.addWidget(self.sidebar_button)
        self.sidebar_button.clicked.connect(self.toggle_sidebar)
        self.sidebar_button.setStyleSheet("background-color: darkgray;")

        self.sidebar_button_1 = QPushButton("Sidebar Button", self.sidebar)
        # self.sidebar_button_1.setStyleSheet("background-color: darkgray;")
        self.sidebar_layout.addWidget(self.sidebar_button_1, alignment= Qt.AlignmentFlag.AlignTop)
        # self.sidebar_layout.addStretch()

        # Sidebar animation
        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"geometry")
        self.sidebar_animation.setDuration(300)
        self.sidebar_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

        # Sidebar state, initial state
        self.sidebar_open = False

    def create_main_page(self):
        print("DEBUG: Inside add_makeCoffeeButton()")

        main_page_widget = QWidget()
        main_page_layout = QVBoxLayout(main_page_widget)

        self.makeCoffeeButton = QPushButton("Make coffee")
        self.makeCoffeeButton.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
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

        self.makeCoffeeButton.clicked.connect(lambda : self.stacked.setCurrentIndex(self.current_page_index + 1))
        main_page_layout.addWidget(self.makeCoffeeButton, alignment= Qt.AlignmentFlag.AlignCenter)

        return main_page_widget


    def toggle_sidebar(self):
        print("DEBUG: toggle_sidebar() called")

        if self.sidebar_animation.state() == QPropertyAnimation.State.Running:
            return  # Ignore clicks if animation is running ## Making Sure no anamolies occurs if clicked multiple times

        if self.sidebar_open:
            # Animate sidebar to hide
            self.sidebar_animation.setStartValue(self.sidebar.geometry())
            self.sidebar_animation.setEndValue(self.sidebar.geometry().adjusted(-self.sidebar_width, 0, -self.sidebar_width, 0))
        else:
            # Animate sidebar to show
            self.sidebar_animation.setStartValue(self.sidebar.geometry())
            self.sidebar_animation.setEndValue(self.sidebar.geometry().adjusted(self.sidebar_width, 0, self.sidebar_width, 0))

        self.sidebar_animation.start()
        self.sidebar_open = not self.sidebar_open
    

    def addPredefinedItemsToMachine(self):
        print("Inside addPredefinedItemsToMachine")
        with open('App/libs/predefined.json', 'r') as file:
            data = json.load(file)
        self.resources = data["ingredients"]
        self.money = data["money"]
        print("Resources : ", self.resources)
        print("Money: ", self.money)
        return


    def create_coffee_type_page(self):
        print("DEBUG: Inside create_coffee_type_page()")

        # Create a new widget with coffee selection options
        page_widget = QWidget()
        page_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 15px; padding: 10px;")
        page_layout = QVBoxLayout(page_widget)

        # self.makeCoffeeButton.hide()
        
        # Create a new widget with coffee selection options
        # selection_widget = QWidget()
        # selection_widget.setStyleSheet("background-color: #f0f0f0; border-radius: 15px; padding: 10px;")
        # selection_layout = QVBoxLayout()
        
        # Message label
        message_label = QLabel("Select coffee type")
        message_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message_label.setStyleSheet("background-color: darkgray; color: white; padding: 20px 30px; border-radius: 10px;")

        page_layout.addWidget(message_label)
        # List of coffee options
        # coffee_types = ["Espresso", "Latte", "Cappuccino", "Americano"]
        coffee_types = ["Espresso", "Latte", "Cappuccino"]
        
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

            button.clicked.connect(lambda checked, coffee=coffee: self.setCoffeeType(coffee))
            page_layout.addWidget(button)
        
        # selection_widget.setLayout(selection_layout)
        
        # self.main_layout.addStretch(3)
        # self.main_layout.addWidget(selection_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        # self.main_layout.addStretch(2)

        return page_widget


    def setCoffeeType(self, coffee):
        print("DEBUG: Inside setCoffeeType()")
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
        msg.exec()
        return


    def buttonClicked(self):
        print("Button Clicked")
        return


    def paintEvent(self, event):
        # painter to draw the background image
        painter = QPainter(self)
        
        # match image to- widget size, Ignoring the aspect ration...
        if not self.scaled_pixmap or self.scaled_pixmap.size() != self.size():
            self.scaled_pixmap = self.pixmap.scaled(self.size(), 
                                                    Qt.AspectRatioMode.IgnoreAspectRatio, 
                                                    Qt.TransformationMode.SmoothTransformation)
        
        # Draw the resized image
        painter.drawPixmap(0, 0, self.scaled_pixmap)
        return


    def resizeEvent(self, event):       

        # Initailize the parent class event
        super().resizeEvent(event)

        # Update size of sidebar
        self.sidebar.setGeometry(self.sidebar.x(), 0, self.sidebar_width, self.height())
        # To trigger the resize event
        self.update()