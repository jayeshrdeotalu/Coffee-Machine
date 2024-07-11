# App will be present here ...
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Adding coustom widget to add background images to each layout if required...
class BackgroundWidget(QWidget):
    def __init__(self, layout, image_path):
        super().__init__()
        self.image_path = image_path
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.image_path)
        painter.drawPixmap(self.rect(), pixmap)

def set_background(layout, image_path):
    return BackgroundWidget(layout, image_path)


class MainWindow(QWidget):  # Passinf QWidget class to main window
    # Qwidget is a parent class and this is a child class
    def __init__(self):
        super().__init__()   # Calling __init__ function of parent class i.e. QWidget using super()
        ## super() is used to access parent class.

        self.setWindowTitle("Coffee Machine") # Setting heading to our app
        self.setGeometry(500, 50, 800, 800) # Setting up Gometry of the window
        # The four arguments are : x, y point to start the window, heigth , width

        # Creating a main layout
        self.main_layout= QHBoxLayout()
        self.main_layout2= QHBoxLayout()
        self.center_layout = QVBoxLayout()

        self.hamburger_button = QPushButton("☰")
        self.hamburger_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.hamburger_button.clicked.connect(self.toggle_sidebar)
        self.center_layout.addWidget(self.hamburger_button, 0)
        self.main_layout.addWidget(self.hamburger_button, alignment=Qt.AlignTop | Qt.AlignLeft)

        # Create buttons for our UI
        self.button1 = QPushButton("Click me")
        self.button1.clicked.connect(self.on_click)
        self.center_layout.addWidget(self.button1)

        # Set background for the left layout
        self.center_layout_background = set_background(self.center_layout, r"C:\Users\Om\Desktop\Coffee-Machine\Data\coffee_2.jpg")

        # Create sidebar
        self.sidebar = QWidget()
        sidebar_width = int(self.width()*0.4)
        self.sidebar.setFixedWidth(sidebar_width)
        sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_button1 = QPushButton("Sidebar Button 1")
        self.sidebar_button1.clicked.connect(self.on_click)
        sidebar_layout.addWidget(self.sidebar_button1)

        # Creating stacked widget to manage main content and sidebar
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.center_layout_background)
        self.stacked_widget.addWidget(self.sidebar)

        # Add the stacked widgets to main layout
        self.main_layout.addWidget(self.stacked_widget)

        # Set the layout 
        self.setLayout(self.main_layout)
        

    def on_click(self):
        print("The Button is Clicked !!!")

    def toggle_sidebar(self):
        # Toggle between main content and sidebar
        current_index = self.stacked_widget.currentIndex()
        target_index = 1 - current_index  # Switch between 0 and 1
        self.stacked_widget.setCurrentIndex(target_index)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())