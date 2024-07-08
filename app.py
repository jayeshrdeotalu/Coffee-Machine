# App will be present here ...
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


'''
TODOs:

1. Create a app.
2. Change background, make it a beauty.
3. add widgets.
4. Make it userfriendly.

'''



class MainWindow(QWidget):  # Passinf QWidget class to main window
    # Qwidget is a parent class and this is a child class

    def __init__(self):
        super().__init__()   # Calling __init__ function of parent class i.e. QWidget using super()
        ## super() is used to access parent class.

        self.setWindowTitle("Coffee Machine") # Setting heading to our app
        self.setGeometry(100, 50, 800, 500) # Setting up Gometry of the window
        # The four arguments are : x, y point to start the window, heigth , width

        # Calling a function to setup a background
        self.set_background(r"Data/coffee_7.jpeg")

                # Create a general layout 

        # Creating a main layout
        self.main_layout= QHBoxLayout()
        
        # Two layout left and right layout 
        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()


        # Create buttons for our UI
        self.button1 = QPushButton("Click me")
        self.button1.clicked.connect(self.on_click)

        self.button2 = QPushButton("Click me")
        self.button2.clicked.connect(self.on_click)

        self.button3 = QPushButton("Click me")
        self.button3.clicked.connect(self.on_click)

        self.left_layout.addWidget(self.button1)
        self.right_layout.addWidget(self.button2)
        self.right_layout.addWidget(self.button3)

        # Add the layouts to main layout
        self.main_layout.addLayout(self.left_layout, 2)
        self.main_layout.addLayout(self.right_layout, 1)

        # Set the layout 
        self.setLayout(self.main_layout)
        

    def on_click(self):
        print("The Button is Clicked !!!")

    def set_background(self, img_path):
        '''Function to set background of the application'''
        
        palette = QPalette()  # Create a object of class ....use for decorating application
        pixmap = QPixmap(img_path)  # Importing image
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())