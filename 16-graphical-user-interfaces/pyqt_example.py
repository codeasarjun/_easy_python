
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

class ExampleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # initialize the UI
        self.init_ui()

    def init_ui(self):
        # create a central widget and set it as the main window's central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # create a vertical layout
        layout = QVBoxLayout()

        # create a label
        self.label = QLabel("Hello, PyQt!")
        layout.addWidget(self.label)

        # create a button and connect it to the slot method
        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        # set the layout on the central widget
        central_widget.setLayout(layout)

        # set main window properties
        self.setWindowTitle('PyQt Example')
        self.setGeometry(100, 100, 300, 200)

    def on_button_click(self):
        self.label.setText("Button Clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = ExampleApp()
    main_win.show()
    sys.exit(app.exec_())
