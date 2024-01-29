import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot")
        self.setGeometry(300, 300, 300, 300)

        self.label = QLabel("Hello, I'm a chatbot. What's your name?")
        self.button = QPushButton("Send")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.label.setText("You said: " + self.input.text())


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()