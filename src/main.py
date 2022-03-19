# please for the love of god https://namingconvention.org/python/ use the pythonic naming convention here

from PyQt5 import QtGui, QtCore, QtWidgets, uic
from pyqtgraph import PlotWidget
import sys
import numpy as np

from classes import *
import interface
import utility as util
import composer


DEBUG_MODE = True
MAX_SAMPLES = 200


class MainWindow(QtWidgets.QMainWindow):
    ''' This is the PyQt5 GUI Main Window'''

    def __init__(self, *args, **kwargs):
        ''' Main window constructor'''

        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('./data/MainWindow.ui', self)

        # set the title and icon
        self.setWindowIcon(QtGui.QIcon('./data/icons/icon.png'))
        self.setWindowTitle("Nyquist Theory Illustrator")

        #for deleted graph/Empty Graph
        self.graph_deleted=False
        self.graph_empty=True


       # initialize arrays and variables
        self.sinusoid_creator_array = []
        self.sinusoid_index = 0
        self.sinusoid_number = 1
        self.browsed_signal = SampledSignal()
        self.summed_signal = SummedSinusoid()
        self.viewer_orginal_signal = Signal()
        self.interpolated_signal = Signal()

        interface.init_connectors(self)
        util.printDebug(
            "Connectors Initialized")

        # initialize graph objects array/dict
        self.plotter_window_dict = {"Primary": PlotterWindow(self.primaryPlot.plot()),
                                    "Primary2": PlotterWindow(self.primaryPlot.plot()),
                                    "Primary3": PlotterWindow(self.primaryPlot.plot()),
                                    "Secondary": PlotterWindow(self.reconstructedPlot.plot()),
                                    "Sinusoid": PlotterWindow(self.sinusoidalSignal.plot()),
                                    "Summed": PlotterWindow(self.summedSignal.plot())
                                    }
        ''' 
        Primary is the original signal\n
        Primary2 is the resampled points \n
        Primary3 is the upsampled/interpolated signal\n
        '''

        util.printDebug(
            "Plotters Initialized")

        composer.plotSinusoidal(self)


def main():

    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
