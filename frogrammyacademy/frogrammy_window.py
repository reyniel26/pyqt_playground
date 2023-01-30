import os

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFileDialog, QMainWindow

from .config import VERSION, static_image_path, static_ui_path


class FrogrammyAcademyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        ui_file = static_ui_path("frogrammy_window.ui")
        uic.loadUi(ui_file,self)

        self.setWindowTitle("Frogrammy Academy")

        iconpath = static_image_path("ICON.png")

        if os.path.exists(iconpath):
            self.setWindowIcon(QIcon(iconpath))

        self.center_form()


    def center_form(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
