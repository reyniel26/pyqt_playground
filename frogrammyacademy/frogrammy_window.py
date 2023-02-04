import os

from PyQt6 import uic
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFileDialog, QMainWindow

from .config import VERSION, static_image_path, static_ui_path

from .debugging_game_widget import DebuggingGameWidget

class FrogrammyAcademyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        ui_file = static_ui_path("frogrammy_window.ui")
        uic.loadUi(ui_file,self)

        self.setWindowTitle("Frogrammy Academy")

        iconpath = static_image_path("ICON.png")

        if os.path.exists(iconpath):
            self.setWindowIcon(QIcon(iconpath))

        self.version_label.setText(VERSION)

        self.center_form()

        # Game Widgets Additionals
        self.debugging_game = DebuggingGameWidget()

        # Add to stack
        self.main_stack_widget.addWidget(self.debugging_game)

        self.action_home.triggered.connect(self.display_home)
        self.action_credits.triggered.connect(self.display_credits)
        self.action_tutorial.triggered.connect(self.display_tutorial)

        # Game Widgets Action
        self.action_debugging.triggered.connect(self.display_debugging_game)

        self.action_exit_game.triggered.connect(self.close)




    def center_form(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def display_home(self):
        self.main_stack_widget.setCurrentIndex(0)

    def display_credits(self):
        self.main_stack_widget.setCurrentIndex(1)

    def display_tutorial(self):
        self.main_stack_widget.setCurrentIndex(2)

    def display_debugging_game(self):
        self.debugging_game.display_home()
        self.main_stack_widget.setCurrentIndex(3)
