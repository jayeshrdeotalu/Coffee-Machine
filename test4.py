from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coffee-Machine")
        self.setGeometry(500, 50, 800, 800)

        # Setting a central widget first
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.main_layout = QHBoxLayout()

        self.left_layout = QVBoxLayout()
        self.middle_layout = QVBoxLayout()


        self.middle_button = QPushButton("Click Me")
        self.middle_button.setStyleSheet("background-color: darkgray;")
        self.middle_layout.addWidget(self.middle_button)

        # # Adding Hamburger button at leftmost corner
        self.hamburger_button = QPushButton("☰", self)
        self.hamburger_button.setFixedSize(50, 50)
        self.hamburger_button.move(0, 0)
        self.hamburger_button.setStyleSheet("background-color: darkgray;")
        # self.hamburger_button.clicked.connect(self.toggle_sidebar)
        # self.left_layout.addWidget(self.hamburger_button, alignment= Qt.AlignLeft)

        # Adding layouts to main
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.middle_layout)
        
        # Adding main layout to the central layout
        self.central_widget.setLayout(self.main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())    