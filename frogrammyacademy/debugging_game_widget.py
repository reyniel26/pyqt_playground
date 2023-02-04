import os

from PyQt6 import uic
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QWidget

from .config import static_image_path, static_ui_path


class DebuggingGameWidget(QWidget):
    def __init__(self):
        super().__init__()
        ui_file = static_ui_path("debugging_game_widget.ui")
        uic.loadUi(ui_file,self)

        self.play_gif()

        self.back_home_btn_1.clicked.connect(self.display_home)
        self.back_home_btn_2.clicked.connect(self.display_home)

        self.tutorial_btn.clicked.connect(self.display_tutorial)
        self.trivia_btn.clicked.connect(self.display_trivia)

    def display_home(self):
        self.debugging_stack_widget.setCurrentIndex(0)

    def display_tutorial(self):
        self.debugging_stack_widget.setCurrentIndex(1)

    def display_trivia(self):
        self.debugging_stack_widget.setCurrentIndex(2)

    def play_gif_by_label(self,label,gif_file):
        movie = QMovie(static_image_path(gif_file))
        label.setMovie(movie)
        movie.start()

    def play_gif(self):
        self.play_gif_by_label(self.debugging_display_label,"DebuggingTitleScreenPicture.gif")