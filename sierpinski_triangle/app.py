import sys

from path_config import static_image_path, static_ui_path
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from sierpinski import SierpinskiTriangle


class SierpinskiTriangleWindow(QMainWindow,SierpinskiTriangle):

    def __init__(self):
        super().__init__()

        ui_file = static_ui_path("sierpinski_window.ui")
        uic.loadUi(ui_file,self)

        self.setWindowTitle("Sierpinski Triangle Emulator")



app = QApplication(sys.argv)

sierpinski_window = SierpinskiTriangleWindow()
sierpinski_window.show()

try:
    app.exec()
except Exception as error:
    print("Exiting..")

app.exit()

