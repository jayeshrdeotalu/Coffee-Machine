from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
)
from PyQt6.QtCore import Qt

class CoffeeMachine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee Machine with Persistent Sidebar")

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        self.main_layout = QHBoxLayout(main_widget)

        # Sidebar
        self.sidebar = QWidget()
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar.setStyleSheet("background-color: lightblue;")
        self.sidebar.setFixedWidth(200)

        # Hamburger button
        self.hamburger_button = QPushButton("☰")
        self.hamburger_button.setFixedSize(50, 50)
        self.hamburger_button.setStyleSheet("background-color: darkgray;")
        self.hamburger_button.clicked.connect(self.toggle_sidebar)
        self.sidebar_layout.addWidget(self.hamburger_button)

        # Add some buttons to the sidebar
        self.sidebar_button_1 = QPushButton("Home")
        self.sidebar_layout.addWidget(self.sidebar_button_1)
        self.sidebar_button_2 = QPushButton("Settings")
        self.sidebar_layout.addWidget(self.sidebar_button_2)
        self.sidebar_layout.addStretch()

        self.main_layout.addWidget(self.sidebar)

        # Page area (stacked widget)
        self.pages = QStackedWidget()
        self.main_layout.addWidget(self.pages)

        # Add pages to the stacked widget
        self.add_pages()

    def add_pages(self):
        # Page 1
        page1 = QWidget()
        page1_layout = QVBoxLayout(page1)
        page1_layout.addWidget(QPushButton("Welcome to Home Page!"))
        self.pages.addWidget(page1)

        # Page 2
        page2 = QWidget()
        page2_layout = QVBoxLayout(page2)
        page2_layout.addWidget(QPushButton("Settings Page"))
        self.pages.addWidget(page2)

    def toggle_sidebar(self):
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()

if __name__ == "__main__":
    app = QApplication([])
    window = CoffeeMachine()
    window.show()
    app.exec()
