import sys

from PyQt6.QtWidgets import QApplication

from sierpinski_triangle.sierpinski_window import SierpinskiTriangleWindow

app = QApplication(sys.argv)

sierpinski_window = SierpinskiTriangleWindow()
sierpinski_window.show()

try:
    app.exec()
except Exception as error:
    print("Exiting..")

app.exit()

