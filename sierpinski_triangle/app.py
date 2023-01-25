import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import load_ui

from sierpinski import SierpinskiTriangle

class SierpinskiTriangleWindow(QMainWindow,SierpinskiTriangle):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sierpinski Triangle Emulator")

app = QApplication(sys.argv)

sierpinski_window = SierpinskiTriangleWindow()
sierpinski_window.show()

try:
    app.exec()
except Exception as error:
    print("Exiting..")

app.exit()

