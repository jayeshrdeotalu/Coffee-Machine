from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QSlider, QPushButton, QDialog
)
from PyQt6.QtCore import Qt
import sys

class PaymentPage(QDialog):
    def __init__(self, price, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Payment Page")
        self.setFixedSize(300, 200)
        layout = QVBoxLayout()

        # Payment Details
        payment_label = QLabel(f"Please pay: \u20b9 {price}")
        payment_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(payment_label)

        # Confirm Payment Button
        confirm_button = QPushButton("Confirm Payment")
        confirm_button.clicked.connect(self.accept_payment)
        layout.addWidget(confirm_button)

        self.setLayout(layout)

    def accept_payment(self):
        self.accept()

class CoffeePricePage(QWidget):
    def __init__(self, coffee_name, base_price, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Coffee Customization")
        self.setFixedSize(400, 300)

        self.base_price = base_price
        self.coffee_name = coffee_name

        # Layouts
        main_layout = QVBoxLayout()
        options_layout = QVBoxLayout()
        milk_layout = QHBoxLayout()
        coffee_layout = QHBoxLayout()
        sugar_layout = QHBoxLayout()

        # Coffee Name
        coffee_label = QLabel(f"{self.coffee_name} - Customize Your Coffee")
        coffee_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        coffee_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        main_layout.addWidget(coffee_label)

        # Milk Option
        milk_label = QLabel("Milk (ml):")
        self.milk_slider = QSlider(Qt.Orientation.Horizontal)
        self.milk_slider.setRange(0, 500)
        self.milk_slider.setValue(100)  # Default value
        self.milk_slider.valueChanged.connect(self.update_price)
        milk_layout.addWidget(milk_label)
        milk_layout.addWidget(self.milk_slider)
        options_layout.addLayout(milk_layout)

        # Coffee Option
        coffee_label = QLabel("Coffee (grams):")
        self.coffee_slider = QSlider(Qt.Orientation.Horizontal)
        self.coffee_slider.setRange(0, 50)
        self.coffee_slider.setValue(10)  # Default value
        self.coffee_slider.valueChanged.connect(self.update_price)
        coffee_layout.addWidget(coffee_label)
        coffee_layout.addWidget(self.coffee_slider)
        options_layout.addLayout(coffee_layout)

        # Sugar Option
        sugar_label = QLabel("Sugar (grams):")
        self.sugar_slider = QSlider(Qt.Orientation.Horizontal)
        self.sugar_slider.setRange(0, 50)
        self.sugar_slider.setValue(5)  # Default value
        self.sugar_slider.valueChanged.connect(self.update_price)
        sugar_layout.addWidget(sugar_label)
        sugar_layout.addWidget(self.sugar_slider)
        options_layout.addLayout(sugar_layout)

        main_layout.addLayout(options_layout)

        # Price Label
        self.price_label = QLabel(f"Price: \u20b9 {self.base_price}")
        self.price_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.price_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        main_layout.addWidget(self.price_label)

        # Payment Button
        payment_button = QPushButton("Proceed to Payment")
        payment_button.clicked.connect(self.open_payment_page)
        main_layout.addWidget(payment_button)

        self.setLayout(main_layout)

    def update_price(self):
        # Price Calculation
        milk_price = self.milk_slider.value() * 0.1  # Milk: 0.1 per ml
        coffee_price = self.coffee_slider.value() * 0.5  # Coffee: 0.5 per gram
        sugar_price = self.sugar_slider.value() * 0.2  # Sugar: 0.2 per gram

        total_price = self.base_price + milk_price + coffee_price + sugar_price
        self.price_label.setText(f"Price: \u20b9 {total_price:.2f}")
        self.total_price = round(total_price, 2)

    def open_payment_page(self):
        payment_page = PaymentPage(self.total_price, self)
        if payment_page.exec():
            self.payment_successful()

    def payment_successful(self):
        self.price_label.setText("Payment Successful! Enjoy your coffee.")

class CoffeeMachineApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee Machine")
        self.setFixedSize(400, 300)

        # Default Coffee Selection Page
        coffee_name = "Cappuccino"
        base_price = 50  # Base price for Cappuccino
        self.price_page = CoffeePricePage(coffee_name, base_price, self)
        self.setCentralWidget(self.price_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeMachineApp()
    window.show()
    sys.exit(app.exec())
