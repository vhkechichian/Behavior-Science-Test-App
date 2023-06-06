import sys
from PyQt6.QtWidgets import QApplication,QDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget

class SubWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sub-Window")
        
        # Add some widgets to the sub-window
        sub_window_layout = QVBoxLayout()
        sub_window_layout.addWidget(QPushButton("Button 1", self))
        sub_window_layout.addWidget(QPushButton("Button 2", self))
        self.setLayout(sub_window_layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Create a QPushButton
        self.button = QPushButton("Open Sub-Window", self)
        self.button.clicked.connect(self.show_sub_window)
        
        # Add the button to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        
        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
    def show_sub_window(self):
        # Create a new instance of the SubWindow class and show it inside the main window
        sub_window = SubWindow(self)
        sub_window.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
