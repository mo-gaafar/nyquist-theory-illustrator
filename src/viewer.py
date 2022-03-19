''' 
1. Updates the plot with the actual signal and interpolated signal
2. plots intersection points each time
3. updates the graph when the '''

import classes
import numpy as np
import utility as util
from classes import *
import interface
import openfile
import main
from scipy import signal
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg


def move_to_viewer(self, Input):

    if Input == "composer":
        # plot summed signal on primary and secondary screens (DONE)
        # we need to get  the summed signal (DONE)
        if len(self.summed_signal.sinusoid_array) <= 1:
            QtWidgets.QMessageBox.warning(
                self, 'NO SIGNAL ', 'You have to plot a signal first')
        else:
            self.viewer_original_signal = Signal(
                self.summed_signal.yAxis, self.summed_signal.xAxis, self.summed_signal.max_analog_frequency)

    elif Input == "browse":
        self.viewer_original_signal = Signal(
            self.browsed_signal.magnitude_array, self.browsed_signal.time_array, self.browsed_signal.max_analog_frequency)

    self.samplingSlider.setMaximum(
        3*(self.viewer_original_signal.max_analog_frequency))

    self.plotter_window_dict["Primary"].plot_reference.setData(
        self.viewer_original_signal.time, self.viewer_original_signal.magnitude)


# plot the browsed signal on the prim and sec screens
    # change

    self.plotter_window_dict["Secondary"].plot_reference.setData(
        self.viewer_original_signal.time, self.viewer_original_signal.magnitude)

    self.WindowTabs.setCurrentIndex(1)
# plot the browsed signal on the prim and sec screens
    # change
    # self.plotter_window_dict["Primary"].plot_reference.setData(self.viewer_original_signal.time, self.viewer_original_signal.magnitude)
    # self.plotter_window_dict["Secondary"].plot_reference.setData(self.viewer_original_signal.time, self.viewer_original_signal.magnitude)

    # plot it on the primary and secondary screens
    # add changes on the prim screen


def toggle_secondary(self):
    # TODO: Make this work
    if interface.ToggleSecondary == False:
        interface.ToggleSecondary = True
        self.reconstructedPlot.show()
        # change size back to default
    else:
        interface.ToggleSecondary = False
        self.reconstructedPlot.hide()
        # change size to 0x0x0


def change_sampling_rate(self, freqvalue):
    # TODO: Fix errors when there is no signal imported../ or signals are deleted
    # TODO: Fix the slider range to not sample below 2 because it causes errors

    self.resampled_magnitude = signal.resample(
        x=self.viewer_original_signal.magnitude, num=freqvalue)
    self.resampled_time = np.linspace(0, self.viewer_original_signal.time[len(
        self.viewer_original_signal.time)-1], freqvalue, endpoint=False)

    self.new = sinc_interp(self.resampled_magnitude,
                           self.resampled_time, self.viewer_original_signal.time)

    self.pen = pg.mkPen(color=(150, 150, 150), width=2,
                        style=QtCore.Qt.DotLine)
    self.plotter_window_dict["Primary"].plot_reference.setData(
        self.viewer_original_signal.time, self.viewer_original_signal.magnitude, pen=self.pen)

    self.pen = pg.mkPen(color=(255, 0, 0), width=0)
    self.plotter_window_dict["Primary2"].plot_reference.setData(
        self.resampled_time, self.resampled_magnitude, symbol='o', pen=self.pen)

    self.pen = pg.mkPen(color=(0, 200, 0), width=2)
    self.plotter_window_dict["Primary3"].plot_reference.setData(
        self.viewer_original_signal.time, self.new, pen=self.pen)

    self.plotter_window_dict["Secondary"].plot_reference.setData(
        self.viewer_original_signal.time, self.new, pen=self.pen)


def sinc_interp(x, s, u):

    # Interpolates x, sampled at "s" instants
    # Output y is sampled at "u" instants ("u" for "upsampled")

    if len(x) != len(s):
        print('not same')

    # Find the period
    T = s[1] - s[0]

    sincM = np.tile(u, (len(s), 1)) - np.tile(s[:, np.newaxis], (1, len(u)))
    y = np.dot(x, np.sinc(sincM/T))
    return y


def delete_primary_secondary(self):
    # TODO: Doesnt delete the signal..
    # overwrite variables
    self.browsed_signal = []
    self.summed_signal = []
    self.viewer_orginal_signal = []
    self.interpolated_signal = []
    self.resampled_time = []
    self.resampled_magnitude = []

    # plots to be reinitialized
    dict_keys = ["Primary", "Primary2", "Primary3", "Secondary"]

    for index in dict_keys:
        self.plotter_window_dict[index].plot_reference.clear()

    QtWidgets.QMessageBox.information(
        self, 'Deleted', 'Your signal has been deleted')
