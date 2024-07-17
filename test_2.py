import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QDockWidget, QToolBar, QAction, QStackedLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.button = QPushButton("Click me!")
        self.layout.addWidget(self.button)
        self.button.setGeometry(100, 100, 100, 30)  # set button in the middle

        self.toolbar = self.addToolBar("Toolbar")
        self.hamburger_action = self.toolbar.addAction(QIcon("hamburger.png"), "Hamburger")
        self.hamburger_action.triggered.connect(self.toggle_sidebar)

        self.sidebar = QDockWidget("Sidebar", self)
        self.sidebar.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.sidebar.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.sidebar_widget = QWidget()
        self.sidebar.setWidget(self.sidebar_widget)
        self.sidebar_layout = QStackedLayout()
        self.sidebar_widget.setLayout(self.sidebar_layout)
        self.sidebar_button = QPushButton("Sidebar button")
        self.sidebar_layout.addWidget(self.sidebar_button)
        self.sidebar_layout.addWidget(QWidget())  # add an empty widget to create a sliding effect
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)
        self.sidebar.hide()

    def toggle_sidebar(self):
        if self.sidebar.isVisible():
            self.sidebar.hide()
        else:
            self.sidebar.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())