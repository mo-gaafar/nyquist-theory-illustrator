
from PyQt5.QtWidgets import QTabWidget, QAction, QPushButton, QSlider, QComboBox, QLCDNumber ,QMessageBox
from PyQt5.QtGui import *
import composer
import openfile
import viewer
# interface globals
CreatorSelectedIndex = 0
''' Sould be connected to the combobox on change'''
ToggleSecondary = True
''' If true then visible'''


def init_connectors(self):
    '''Initializes all event connectors and triggers'''

    ''' Menu Bar'''
    self.actionOpen = self.findChild(QAction, "actionOpen")
    self.actionOpen.triggered.connect(
        lambda: openfile.browse_window(self))

    self.actionExport = self.findChild(QAction, "actionExport")
    self.actionExport.triggered.connect(
        lambda: openfile.export_summed_signal(self))
    
    self.actionAbout_Us = self.findChild(QAction, "actionAbout_Us")
    self.actionAbout_Us.triggered.connect(
        lambda: about_us(self))    

    self.WindowTabs = self.findChild(QTabWidget, "WindowTabs")

    ''' Composer Tab'''

    self.clearComposerButton = self.findChild(
        QPushButton, "clearComposerButton")
    self.clearComposerButton.clicked.connect(
        lambda: composer.clearComposer(self))

    self.addSineButton = self.findChild(QPushButton, "addSineButton")
    self.addSineButton.clicked.connect(
        lambda: composer.addSinusoidal(self))
  

    self.deleteSineButton = self.findChild(QPushButton, "deleteSineButton")
    self.deleteSineButton.hide()
    self.deleteSineButton.clicked.connect(
        lambda: composer.deleteSinusoidal(self))

    # Creator Sliders and LCD
    # Frequency
    self.frequencySlider = self.findChild(QSlider, "frequencySlider")
    self.frequencySlider.valueChanged.connect(
        lambda: composer.plotSinusoidal(self))

    self.frequencyLCD = self.findChild(QLCDNumber, "frequencyLCD")
    self.frequencySlider.valueChanged.connect(
        lambda: self.frequencyLCD.display(self.frequencySlider.value()))

    # Magnitude
    self.magnitudeSlider = self.findChild(QSlider, "magnitudeSlider")
    self.magnitudeSlider.valueChanged.connect(
        lambda: composer.plotSinusoidal(self))

    self.magnitudeLCD = self.findChild(QLCDNumber, "magnitudeLCD")
    self.magnitudeSlider.valueChanged.connect(
        lambda: self.magnitudeLCD.display(self.magnitudeSlider.value()))

    # Phase
    self.phaseSlider = self.findChild(QSlider, "phaseSlider")
    self.phaseSlider.valueChanged.connect(
        lambda: composer.plotSinusoidal(self))

    self.phaseLCD = self.findChild(QLCDNumber, "phaseLCD")
    self.phaseSlider.valueChanged.connect(
        lambda: self.phaseLCD.display(self.phaseSlider.value()))

    # Confirm move to viewer
    self.confirmButton = self.findChild(QPushButton, "confirmButton")
    self.confirmButton.clicked.connect(
        lambda: viewer.control_viewer(self))

    # Created signals combobox
    self.signalsMenu = self.findChild(QComboBox, "signalsMenu")
    self.signalsMenu.currentIndexChanged.connect(
        lambda: composer.updateSinusoid(self, input=self.signalsMenu.currentIndex()))

    '''Viewer Tab'''

    self.clearViewerButton = self.findChild(QPushButton, "clearViewerButton")
    self.clearViewerButton.clicked.connect(
        lambda: viewer.delete_primary_secondary(self))
    self.splitButton = self.findChild(QPushButton, "splitButton")
    self.splitButton.clicked.connect(lambda: viewer.toggle_secondary(self))

    # Sampling frequency control
    self.samplingSlider = self.findChild(QSlider, "samplingSlider")
    self.samplingSlider.setMinimum(1)
    self.samplingSlider.valueChanged.connect(
        lambda: viewer.change_sampling_rate(self, self.samplingSlider.value()))

    self.samplingLCD = self.findChild(QLCDNumber, "samplingLCD")
    self.samplingSlider.valueChanged.connect(
        lambda: self.samplingLCD.display(self.samplingSlider.value()))



def about_us(self):
    QMessageBox.about(
            self, ' About ', 'This is a nyquist theory illustrator \nCreated by junior students from the faculty of Engineering, Cairo Uniersity, Systems and Biomedical Engineering department \n \nTeam members: \n-Mohammed Nasser \n-Abdullah Saeed \n-Zeyad Mansour \n-Mariam Khaled \n \nhttps://github.com/mo-gaafar/Nyquist_Theory_Illustrator.git ')