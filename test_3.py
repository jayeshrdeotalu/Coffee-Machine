import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sliding Sidebar Example")
        self.setGeometry(500, 50, 800, 800)

        self.image_path = "Data/coffee_2.jpg"
        self.pixmap = QPixmap(self.image_path)
        self.scaled_pixmap = None

        # Main button in the middle
        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        main_layout.addStretch(2)
        self.main_button = QPushButton("Make coffee", self)
        self.main_button.setStyleSheet("background-color: darkgray;")
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

    def set_background(self):
        # Scale the image to fit the window
        scaled_pixmap = self.pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        brush = QBrush(scaled_pixmap)
        palette = self.palette()
        palette.setBrush(QPalette.Window, brush)
        self.setPalette(palette)

    def on_resize(self, event):
        self.set_background()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
