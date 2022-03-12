# please for the love of god https://namingconvention.org/python/ use the python naming convention here

import classes
import connectors
import utility as util
import openfile
import viewer

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui, QtCore, QtWidgets


DebugMode = True


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('mainwindow.ui', self)
        connectors.init_connectors()
