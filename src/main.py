# please for the love of god https://namingconvention.org/python/ use the python naming convention here
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui, QtCore, QtWidgets
import sys

import classes
import connectors
import utility as util
import openfile
import viewer


DebugMode = True


class MainWindow(QtWidgets.QMainWindow):
    ''' This is the PyQt5 GUI Main Window'''

    def __init__(self, *args, **kwargs):
        ''' Main window constructor'''
        
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('mainwindow.ui', self)
        # set the title and icon
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setWindowTitle("Nyquist Theory Illustrator")

        connectors.init_connectors(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
