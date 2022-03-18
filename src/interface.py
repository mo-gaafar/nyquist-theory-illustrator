from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, QMenuBar, QMenu,  QApplication, QPushButton, QSlider, QTextEdit, QFileDialog, QScrollBar, QComboBox, QCheckBox, QScrollBar, QLCDNumber, QLineEdit
from PyQt5.QtGui import *

import main
import classes
import utility as util
import composer
import openfile
import viewer
# interface globals
CreatorSelectedIndex = 0
''' Sould be connected to the combobox on change'''


def init_connectors(self):
    '''Initializes all event connectors and triggers'''

    ''' Menu Bar'''
    self.actionOpen = self.findChild(QAction, "actionOpen")
    self.actionOpen.triggered.connect(
        lambda: openfile.browse_window(self))

    ''' Composer Tab'''

    self.clearComposerButton = self.findChild(
        QPushButton, "clearComposerButton")
    self.clearComposerButton.clicked.connect(
        lambda: util.printDebug("not connected"))

    self.addSineButton = self.findChild(QPushButton, "addSineButton")
    self.addSineButton.clicked.connect(
        lambda: composer.addSinusoidal(self))
    self.addSineButton.clicked.connect(
        lambda: composer.plotSinusoidal(self))

    self.deleteSineButton = self.findChild(QPushButton, "deleteSineButton")
    self.deleteSineButton.clicked.connect(
        lambda: composer.deleteSinusoidal(self))

    # Creator Sliders and LCD
    # Frequency
    self.frequencySlider = self.findChild(QSlider, "frequencySlider")
    self.frequencySlider.valueChanged.connect(
        lambda: composer.setFrequency(self, Input=self.frequencySlider.value()))

    self.frequencyLCD = self.findChild(QLCDNumber, "frequencyLCD")
    self.frequencySlider.valueChanged.connect(
        lambda: self.frequencyLCD.display(self.frequencySlider.value()))

    # Magnitude
    self.magnitudeSlider = self.findChild(QSlider, "magnitudeSlider")
    self.magnitudeSlider.valueChanged.connect(
        lambda: composer.setMagnitude(self, Input=self.magnitudeSlider.value()))

    self.magnitudeLCD = self.findChild(QLCDNumber, "magnitudeLCD")
    self.magnitudeSlider.valueChanged.connect(
        lambda: self.magnitudeLCD.display(self.magnitudeSlider.value()))

    # Phase
    self.phaseSlider = self.findChild(QSlider, "phaseSlider")
    self.phaseSlider.valueChanged.connect(
        lambda: composer.setPhaseshift(self, Input=self.phaseSlider.value()))

    self.phaseLCD = self.findChild(QLCDNumber, "phaseLCD")
    self.phaseSlider.valueChanged.connect(
        lambda: self.phaseLCD.display(self.phaseSlider.value()))

    # Confirm move to viewer
    self.confirmButton = self.findChild(QPushButton, "confirmButton")
    self.confirmButton.clicked.connect(
        lambda: viewer.move_to_viewer(self, "composer"))
    

    # Created signals combobox
    self.signalsMenu = self.findChild(QComboBox, "signalsMenu")
    self.signalsMenu.currentIndexChanged.connect(
        lambda: composer.setSelectedSignal(self, self.signalsMenu.currentIndex()))
    self.signalsMenu.currentIndexChanged.connect(
        lambda: self.frequencySlider.setValue(self.sinusoid_creator_array[self.sinusoid_index].frequency))
    self.signalsMenu.currentIndexChanged.connect(
        lambda: self.magnitudeSlider.setValue(self.sinusoid_creator_array[self.sinusoid_index].magnitude))
    self.signalsMenu.currentIndexChanged.connect(
        lambda: self.phaseSlider.setValue(self.sinusoid_creator_array[self.sinusoid_index].phaseshift))

    '''Viewer Tab'''

    self.clearViewerButton = self.findChild(QPushButton, "clearViewerButton")
    self.clearViewerButton.clicked.connect(
        lambda: viewer.delete_primary_secondary(self))
#************************************************************************************#
    self.splitButton = self.findChild(QPushButton, "splitButton")
    self.splitButton.clicked.connect(lambda: util.printDebug("not connected"))

    # Sampling frequency control
    self.samplingSlider = self.findChild(QSlider, "samplingSlider")
    self.samplingSlider.valueChanged.connect(
        lambda: viewer.change_sampling_rate(self, "freqrate"))

    self.samplingLCD = self.findChild(QLCDNumber, "samplingLCD")
