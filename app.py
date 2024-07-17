import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Adding custom widget to add background images to each layout if required...
class BackgroundWidget(QWidget):
    def __init__(self, layout, image_path):
        super().__init__()
        self.image_path = image_path
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(self.image_path)
        painter.drawPixmap(self.rect(), pixmap)
        super().paintEvent(event)

def set_background(layout, image_path):
    return BackgroundWidget(layout, image_path)

class MainWindow(QWidget):  # Passing QWidget class to main window
    def __init__(self):
        super(MainWindow, self).__init__()   # Calling __init__ function of parent class i.e. QWidget using super()
        
        self.setWindowTitle("Coffee Machine") # Setting heading to our app
        self.setGeometry(500, 50, 800, 800) # Setting up Geometry of the window

        # Creating a main layout
        self.main_layout= QHBoxLayout()
        self.splitter = QSplitter(Qt.Horizontal)
        self.center_layout = QVBoxLayout()

        self.hamburger_button = QPushButton("☰")
        self.hamburger_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.hamburger_button.clicked.connect(self.toggle_sidebar)

        # self.hamburger_button_2 = QPushButton("X")
        # self.hamburger_button_2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # self.hamburger_button_2.clicked.connect(self.toggle_sidebar)

        # Create buttons for our UI
        self.button1 = QPushButton("Click me")
        self.button1.clicked.connect(self.on_click)
        self.center_layout.addWidget(self.hamburger_button, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.center_layout.addStretch()
        self.center_layout.addWidget(self.button1,  alignment=Qt.AlignCenter)
        self.center_layout.addStretch()

        # Set background for the center layout
        self.center_layout_background = set_background(self.center_layout, r"C:\Users\Om\Desktop\Coffee-Machine\Data\coffee_2.jpg")

        # Create a central widget to hold the center layout
        self.center_widget = QWidget()
        self.center_widget.setLayout(self.center_layout)

        # Create sidebar
        self.sidebar = QWidget()
        sidebar_width = int(self.width() * 0.4)
        self.sidebar.setFixedWidth(sidebar_width)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_button1 = QPushButton("Sidebar Button 1")
        self.sidebar_button1.clicked.connect(self.on_click)
        self.sidebar_button2 = QPushButton("Sidebar Button 2")
        self.sidebar_button2.clicked.connect(self.on_click)
        self.sidebar_button3 = QPushButton("Sidebar Button 3")
        self.sidebar_button3.clicked.connect(self.on_click)
        # self.sidebar_layout.addWidget(self.hamburger_button_2, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.sidebar_layout.addWidget(self.sidebar_button1)
        self.sidebar_layout.addWidget(self.sidebar_button2)
        self.sidebar_layout.addWidget(self.sidebar_button3)
        self.sidebar_layout.addStretch()

        # Add widgets to the splitter
        self.splitter.addWidget(self.sidebar)
        self.splitter.addWidget(self.center_widget)
        self.sidebar.hide()  # Hide the sidebar initially

        # # Creating stacked widget to manage main content and sidebar
        # self.stacked_widget = QStackedWidget()
        # self.stacked_widget.addWidget(self.center_layout_background)
        # self.stacked_widget.addWidget(self.sidebar)

        # Add the stacked widgets to main layout
        self.main_layout.addWidget(self.splitter)

        # Set the layout 
        self.setLayout(self.main_layout)

    def on_click(self):
        print("The Button is Clicked !!!")

    def toggle_sidebar(self):
        # Toggle between main content and sidebar
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
