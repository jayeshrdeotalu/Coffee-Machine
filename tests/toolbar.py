from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, 
    QMenu, QMenuBar, QToolBar, QMessageBox
)
from PyQt6.QtGui import QIcon, QAction
import sys

class CoffeeMachine(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee Machine with Menu and Toolbar")

        # Set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Welcome to the Coffee Machine!"))
        central_widget.setLayout(layout)

        # Add menu bar
        self.create_menu_bar()

        # Add toolbars
        self.create_toolbars()

    def create_menu_bar(self):
        # Create menu bar
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")
        new_action = QAction("New Order", self)
        new_action.triggered.connect(lambda: QMessageBox.information(self, "New Order", "New order created!"))
        file_menu.addAction(new_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Help menu
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(lambda: QMessageBox.information(self, "About", "Coffee Machine v1.0"))
        help_menu.addAction(about_action)

    def create_toolbars(self):
        # Create toolbar
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)

        # Add actions to the toolbar
        new_order_action = QAction(QIcon(), "New Order", self)
        new_order_action.triggered.connect(lambda: QMessageBox.information(self, "New Order", "New order created!"))
        toolbar.addAction(new_order_action)

        about_action = QAction(QIcon(), "About", self)
        about_action.triggered.connect(lambda: QMessageBox.information(self, "About", "Coffee Machine v1.0"))
        toolbar.addAction(about_action)

        exit_action = QAction(QIcon(), "Exit", self)
        exit_action.triggered.connect(self.close)
        toolbar.addAction(exit_action)

if __name__ == "__main__":
    app = QApplication([])
    coffee_machine = CoffeeMachine()
    coffee_machine.show()
    app.exec()

'''
---

### **Key Points to Note**
1. **Menu Bar**:
   - Use `menuBar()` to create menus like "File", "Help", etc.
   - Use `QAction` to define actions within menus.
   - Connect each action to a method or lambda function for functionality.

2. **Toolbars**:
   - Use `addToolBar()` to add a toolbar to the main window.
   - Use `QAction` for toolbar buttons, just like in the menu bar.
   - Toolbars can be docked or undocked, and their position can be customized.

3. **Integration**:
   - can reuse the same `QAction` objects for both menus and toolbars, ensuring consistency.

---

### **Output**
- A **menu bar** with "File" and "Help" menus.
- A **toolbar** with buttons for "New Order", "About", and "Exit".
- Both the menu items and toolbar buttons trigger corresponding actions.

---
'''