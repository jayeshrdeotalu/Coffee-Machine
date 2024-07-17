import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sliding Sidebar")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create main layout
        main_layout = QHBoxLayout(central_widget)

        # Create sidebar
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setGeometry(0, 0, 200, self.height())
        self.sidebar.hide()

        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_button = QPushButton("Sidebar Button")
        sidebar_layout.addWidget(sidebar_button)

        # Create content area
        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)
        central_button = QPushButton("Central Button")
        content_layout.addWidget(central_button)

        # Create hamburger button
        hamburger_button = QPushButton()
        hamburger_button.setIcon(QIcon("hamburger_icon.png"))  # Replace with your icon

        # Add widgets to main layout
        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(content_area)

        # Create animation
        self.sidebar_animation = QPropertyAnimation(self.sidebar, b"geometry")
        self.sidebar_animation.setDuration(250)

        # Connect hamburger button
        hamburger_button.clicked.connect(self.toggle_sidebar)

        # Add hamburger button to content area
        content_layout.addWidget(hamburger_button, alignment=Qt.AlignTop | Qt.AlignLeft)

    def toggle_sidebar(self):
        if self.sidebar.isVisible():
            self.sidebar_animation.setEndValue(QRect(0, 0, 0, self.height()))
        else:
            self.sidebar_animation.setEndValue(QRect(0, 0, 200, self.height()))
        self.sidebar_animation.start()
        self.sidebar.setVisible(not self.sidebar.isVisible())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
