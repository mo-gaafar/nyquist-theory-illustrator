from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSlider, QTextEdit, QFileDialog, QScrollBar, QComboBox, QCheckBox, QScrollBar, QLCDNumber, QLineEdit
from PyQt5.QtGui import *

import main
import classes


def init_connectors(self):
    '''Initializes all event connectors and triggers'''
    # Confirmation button
    self.confirmButton = self.findChild(QPushButton, "confirmButton")

    return
