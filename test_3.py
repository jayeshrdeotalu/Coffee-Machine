import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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
        self.setGeometry(500, 50, 800, 800)

        self.image_path = "Data/coffee_2.jpg"
        self.pixmap = QPixmap(self.image_path)
        self.scaled_pixmap = None

        # Defining variables using thoughoutly in the code
        self.coffeeType = None
        self.money = 0
        self.resources = None

        # Importing prebuild assets to machine
        self.addPredefinedItemsToMachine()

        # Main button in the middle
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)
        main_layout.addStretch(2)
        self.main_button = QPushButton("Make coffee", self)
        self.main_button.setStyleSheet("background-color: darkgray;")
        self.main_button.clicked.connect(self.selectCoffeeType)
        # self.main_button.setFixedSize(100, 50)
        main_layout.addWidget(self.main_button, alignment=Qt.AlignCenter)
        main_layout.addStretch(1)

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
        return
    
    def selectCoffeeType(self):

        msg = QMessageBox()
        msg.setText("Please select Coffee Type:")

        for coffee in COFFEE_TYPES:
            button = msg.addButton(coffee, QMessageBox.ActionRole)
            button.clicked.connect(lambda checked, coffee=coffee: self.checkIngredients(coffee))

        msg.exec_()
        return

    def checkIngredients(self, ctype):
        print("Type of coffee choosen :", ctype)
        self.coffee = Coffee(ctype=ctype)
        return

    def buttonClicked(self):
        print("Button Clicked")
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
