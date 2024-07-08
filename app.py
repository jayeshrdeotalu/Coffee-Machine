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

        self.initUI()  # Callin a funtion to initialise UI. It will contain all out widgets.

    def initUI(self):
        self.setWindowTitle("Coffee Machine") # Setting heading to our app
        self.setGeometry(100, 50, 800, 500) # Setting up Gometry of the window
        # The four arguments are : x, y point to start the window, heigth , width

        # Calling a function to setup a background
        self.set_background(r"Data/pict_1.jpg")

        # Create a general layout 

        # Generally a vertical layout is made
        layout = QVBoxLayout()

        listlayout1 = QHBoxLayout()
        listlayout2 = QHBoxLayout()

        # Create buttons for our UI
        self.button1 = QPushButton("Click me")
        self.button1.clicked.connect(self.on_click)

        self.button2 = QPushButton("Click me")
        self.button2.clicked.connect(self.on_click)

        listlayout1.addWidget(self.button1)
        listlayout1.addWidget(self.button2)

        # Add this button to our layout
        layout.addLayout(listlayout1)
        layout.addLayout(listlayout2)

        # Set the layout 
        self.setLayout(layout)

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