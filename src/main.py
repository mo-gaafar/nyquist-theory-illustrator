# please for the love of god https://namingconvention.org/python/ use the pythonic naming convention here
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui, QtCore, QtWidgets
import sys

from classes import *
import interface
import utility as util
import openfile
import viewer


DebugMode = True


class MainWindow(QtWidgets.QMainWindow):
    ''' This is the PyQt5 GUI Main Window'''

    def __init__(self, *args, **kwargs):
        ''' Main window constructor'''

        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('./data/MainWindow.ui', self)

        # set the title and icon
        self.setWindowIcon(QtGui.QIcon('./data/icons/icon.png'))
        self.setWindowTitle("Nyquist Theory Illustrator")

        interface.init_connectors(self)
        util.printDebug(
            "this should be our print function (DONT USE THE STANDARD print() )")

        # initialize arrays
        self.sinusoid_creator_array = [Sinusoid()]
        self.interpolated_signal_array = [SampledSignal()]


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
