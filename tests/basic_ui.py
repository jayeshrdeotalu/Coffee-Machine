from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QLabel, QPushButton

class CoffeeMachine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee Machine")

        # Create the QStackedWidget
        self.stack = QStackedWidget()

        # Add pages
        self.stack.addWidget(self.create_home_page())
        self.stack.addWidget(self.create_customization_page())
        self.stack.addWidget(self.create_brewing_page())

        # Set the initial page
        self.stack.setCurrentIndex(0)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

    def create_home_page(self):
        page = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Welcome! Choose your coffee:"))
        layout.addWidget(QPushButton("Espresso", clicked=lambda: self.stack.setCurrentIndex(1)))
        layout.addWidget(QPushButton("Cappuccino", clicked=lambda: self.stack.setCurrentIndex(1)))
        layout.addWidget(QPushButton("Latte", clicked=lambda: self.stack.setCurrentIndex(1)))

        page.setLayout(layout)
        return page

    def create_customization_page(self):
        page = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Customize your coffee:"))
        layout.addWidget(QPushButton("Add Sugar", clicked=lambda: print("Sugar added")))
        layout.addWidget(QPushButton("Add Milk", clicked=lambda: print("Milk added")))
        layout.addWidget(QPushButton("Proceed to Brew", clicked=lambda: self.stack.setCurrentIndex(2)))

        page.setLayout(layout)
        return page

    def create_brewing_page(self):
        page = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Brewing your coffee..."))
        layout.addWidget(QPushButton("Go Back to Home", clicked=lambda: self.stack.setCurrentIndex(0)))

        page.setLayout(layout)
        return page

if __name__ == "__main__":
    app = QApplication([])
    coffee_machine = CoffeeMachine()
    coffee_machine.show()
    app.exec()
