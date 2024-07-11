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
        # Two layout left and right layout 
        self.center_layout = QVBoxLayout()

        # Create buttons for our UI
        self.button1 = QPushButton("Click me")
        self.button1.clicked.connect(self.on_click)

        self.center_layout.addWidget(self.button1)

        # Set background for the left layout
        self.center_layout_background = set_background(self.center_layout, r"C:\Users\Om\Desktop\Coffee-Machine\Data\coffee_2.jpg")

        # Add the layouts snd widgets to main layout
        self.main_layout.addWidget(self.center_layout_background, 2)
        # self.main_layout.addLayout(self.right_layout, 1)

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