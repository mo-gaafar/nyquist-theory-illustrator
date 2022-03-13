from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QSlider, QTextEdit, QFileDialog, QScrollBar, QComboBox, QCheckBox, QScrollBar, QLCDNumber, QLineEdit
from PyQt5.QtGui import *

import main
import classes
import utility as util
# interface globals
CreatorSelectedIndex = 0
''' Sould be connected to the combobox on change'''


def init_connectors(self):
    '''Initializes all event connectors and triggers'''

    ''' Composer Tab'''

    self.clearComposerButton = self.findChild(
        QPushButton, "clearComposerButton")
    self.clearComposerButton.clicked.connect(
        lambda: util.printDebug("not connected"))

    self.addSineButton = self.findChild(QPushButton, "addSineButton")
    self.addSineButton.clicked.connect(
        lambda: util.printDebug("not connected"))

    self.deleteSineButton = self.findChild(QPushButton, "deleteSineButton")
    self.deleteSineButton.clicked.connect(
        lambda: util.printDebug("not connected"))

    # Creator Sliders and LCD
    # Frequency
    self.frequencySlider = self.findChild(QSlider, "frequencySlider")
    self.frequencySlider.valueChanged.connect(
        lambda: util.printDebug("not connected"))

    self.frequencyLCD = self.findChild(QLCDNumber, "frequencyLCD")

    # Magnitude
    self.magnitudeSlider = self.findChild(QSlider, "magnitudeSlider")
    self.magnitudeSlider.valueChanged.connect(
        lambda: util.printDebug("not connected"))

    self.magnitudeLCD = self.findChild(QLCDNumber, "magnitudeLCD")

    # Phase
    self.phaseSlider = self.findChild(QSlider, "phaseSlider")
    self.phaseSlider.valueChanged.connect(
        lambda: util.printDebug("not connected"))

    self.phaseLCD = self.findChild(QLCDNumber, "phaseLCD")

    # Confirm move to viewer
    self.confirmButton = self.findChild(QPushButton, "confirmButton")
    self.confirmButton.clicked.connect(
        lambda: util.printDebug("not connected"))

    # Created signals combobox
    self.signalsMenu = self.findChild(QComboBox, "signalsMenu")
    self.signalsMenu.currentIndexChanged.connect(
        lambda: util.printDebug("not connected"))

    '''Viewer Tab'''

    self.clearViewerButton = self.findChild(QPushButton, "clearViewerButton")
    self.clearViewerButton.clicked.connect(
        lambda: util.printDebug("not connected"))

    self.splitButton = self.findChild(QPushButton, "splitButton")
    self.splitButton.clicked.connect(lambda: util.printDebug("not connected"))

    # Sampling frequency control
    self.samplingSlider = self.findChild(QSlider, "samplingSlider")
    self.samplingSlider.valueChanged.connect(
        lambda: util.printDebug("not connected"))

    self.samplingLCD = self.findChild(QLCDNumber, "samplingLCD")
