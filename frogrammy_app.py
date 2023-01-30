import sys

from PyQt6.QtWidgets import QApplication

from frogrammyacademy.frogrammy_window import FrogrammyAcademyWindow

app = QApplication(sys.argv)

frogrammy_window = FrogrammyAcademyWindow()
frogrammy_window.show()

try:
    app.exec()
except Exception as error:
    print("Exiting..")

app.exit()

