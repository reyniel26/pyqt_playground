import os
import sys

VERSION = "v0.1"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        # pylint: disable=no-member
    except Exception:
        # base_path = os.path.abspath(".")
        base_path = os.path.dirname(__file__)



    return os.path.join(base_path, relative_path)

def static_path(path):
    """
    get the static path of the certain path of file
    """
    return resource_path(os.path.join("static", path))

def static_ui_path(ui_form_name):
    """
    get the static ui path of the certain path or file
    """
    return os.path.join(static_path("ui"), ui_form_name)

def static_image_path(image_filename):
    """
    get the static image path of the certain path or file
    """
    return os.path.join(static_path("images"), image_filename)