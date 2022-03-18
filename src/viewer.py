''' 
1. Updates the plot with the actual signal and interpolated signal
2. plots intersection points each time
3. updates the graph when the '''

import classes
import numpy as np
import utility as util
from classes import *
import openfile
import main
from PyQt5 import QtWidgets


def move_to_viewer(self, Input):
    print("move")

    if Input == "composer":
        print("composer_if")
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
        print("browse elif")
    self.plotter_window_dict["Primary"].plot_reference.setData(
        self.viewer_original_signal.time, self.viewer_original_signal.magnitude)
    self.plotter_window_dict["Secondary"].plot_reference.setData(
        self.viewer_original_signal.time, self.viewer_original_signal.magnitude)

    self.WindowTabs.setCurrentIndex(1)
# plot the browsed signal on the prim and sec screens
    # change

    # self.plotter_window_dict["Primary"].plot_reference.setData(self.viewer_original_signal.time, self.viewer_original_signal.magnitude)
    # self.plotter_window_dict["Secondary"].plot_reference.setData(self.viewer_original_signal.time, self.viewer_original_signal.magnitude)

    # plot it on the primary and secondary screens
    # add changes on the prim screen

    # TODO change the tab to viewer
    # TODO  if not make a dialogue box


def change_sampling_rate(self, Input):

    # add points based on sampling rate
    # plot the points
    # connect them by using interpolation
    # plot the interpolated signal
    # 3 Fmax

    return


def delete_primary_secondary(self):
    self.plotter_window_dict["Primary"].plot_reference.setData(
        xAxis=0, yAxis=0)
    self.plotter_window_dict["Secondary"].plot_reference.setData(
        xAxis=0, yAxis=0)
    QtWidgets.QMessageBox.information(
        self, 'Deleted', 'Your signal has been deleted')
