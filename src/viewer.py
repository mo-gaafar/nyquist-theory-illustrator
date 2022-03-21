''' 
1. Updates the plot with the actual signal and interpolated signal
2. plots intersection points each time
3. updates the graph when the '''

import numpy as np
from classes import *
import interface
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import openfile

def control_viewer(self):
    ''' Control the transition from composer to viewer'''
    if len(self.sinusoid_creator_array) == 0:
        QtWidgets.QMessageBox.warning(
            self, 'NO SIGNAL ', 'You have to plot a signal first')
    else:
        move_to_viewer(self, Input="composer")


def move_to_viewer(self, Input):

    if Input == "composer":
        # plot summed signal on primary and secondary screens (DONE)
        # we need to get  the summed signal (DONE)
        if len(self.sinusoid_creator_array) < 1:
            QtWidgets.QMessageBox.warning(
                self, 'NO SIGNAL ', 'You have to plot a signal first')
        else:
          #save the summed signal as csv file
            openfile.export_summed_signal(self)
            self.viewer_original_signal = Signal(
                self.summed_signal.yAxis, self.summed_signal.xAxis, self.summed_signal.max_analog_frequency)            
            self.WindowTabs.setCurrentIndex(1)
    elif Input == "browse":

        self.viewer_original_signal = Signal(
            self.browsed_signal.magnitude_array, self.browsed_signal.time_array, self.browsed_signal.max_analog_frequency)
        self.WindowTabs.setCurrentIndex(1)
        self.viewer_original_signal.get_max_frequency()  # updates max frequency using fft

    # update slider maximum
    self.samplingSlider.setMaximum(
        3*(self.viewer_original_signal.max_analog_frequency))

    # initialize plots
    self.plotter_window_dict["Primary"].plot_reference.setData(
        self.viewer_original_signal.time, self.viewer_original_signal.magnitude)

    self.plotter_window_dict["Secondary"].plot_reference.setData(
        self.viewer_original_signal.time, self.viewer_original_signal.magnitude)
    self.graph_empty = False
    self.graph_deleted = False


def toggle_secondary(self):
    if interface.ToggleSecondary == False:
        interface.ToggleSecondary = True
        self.reconstructedPlot.show()
        # change size back to default
    else:
        interface.ToggleSecondary = False
        self.reconstructedPlot.hide()
        # change size to 0x0x0


def change_sampling_rate(self, freqvalue):

    if freqvalue == 0:  # TODO: implement within functions
        freqvalue = 1

    if self.graph_deleted == True:
        QtWidgets.QMessageBox.warning(
            self, 'NO SIGNAL ', 'The signal is deleted')
    elif self.graph_empty == True:
        QtWidgets.QMessageBox.warning(self, 'NO SINGAL ', 'No signal imported')

    else:

        returned_tuple = ()
        returned_tuple = downsample(
            self.viewer_original_signal.time, self.viewer_original_signal.magnitude, freqvalue)
        self.resampled_magnitude = np.array(returned_tuple[1])
        self.resampled_time = np.array(returned_tuple[0])


        # sinc interpolation
        self.interpolated_magnitude = sinc_interpolation(
            self.resampled_magnitude, self.resampled_time, self.viewer_original_signal.time)

        # refresh all viewer graphs
        self.pen = pg.mkPen(color=(150, 150, 150), width=2,
                            style=QtCore.Qt.DotLine)
        self.plotter_window_dict["Primary"].plot_reference.setData(
            self.viewer_original_signal.time, self.viewer_original_signal.magnitude, pen=self.pen)

        self.pen = pg.mkPen(color=(0, 200, 0), width=0)
        self.plotter_window_dict["Primary2"].plot_reference.setData(
            self.resampled_time, self.resampled_magnitude, symbol='o', pen=self.pen)

        self.pen = pg.mkPen(color=(0, 200, 0), width=2)
        self.plotter_window_dict["Primary3"].plot_reference.setData(
            self.viewer_original_signal.time, self.interpolated_magnitude, pen=self.pen)

        self.plotter_window_dict["Secondary"].plot_reference.setData(
            self.viewer_original_signal.time, self.interpolated_magnitude, pen=self.pen)


def sinc_interpolation(input_magnitude, input_time, original_time):
    '''Whittaker Shannon interpolation formula linked here:
      https://en.wikipedia.org/wiki/Whittaker%E2%80%93Shannon_interpolation_formula '''

    if len(input_magnitude) != len(input_time):
        print('not same')

    # Find the period
    if len(input_time) != 0:
        # T = max(input_time) / len(input_time)
        T = input_time[1] - input_time[0]

    # the equation
    sincM = np.tile(original_time, (len(input_time), 1)) - \
        np.tile(input_time[:, np.newaxis], (1, len(original_time)))
    output_magnitude = np.dot(input_magnitude, np.sinc(sincM/T))
    return output_magnitude


def downsample(array_x, array_y, frequency):
    '''Returns a tuple containting downsampled (array_x, array_y) '''

    resampled_x = []
    resampled_y = []

    # divide total samples over maximum time to get 1/period
    max_sampling_frequency = len(array_x)/max(array_x)
    length = len(array_x)
    step = round(max_sampling_frequency/frequency)

    for index in range(0, length, step):
        resampled_x.append(array_x[index])
        resampled_y.append(array_y[index])

    return resampled_x, resampled_y


def delete_primary_secondary(self):
    # once the signal deleted
    if self.graph_empty == True:
        QtWidgets.QMessageBox.information(
            self, 'NO SIGNAL', 'No signal to delete')

    else:
        # overwrite variables
        #self.browsed_signal = []
        #self.summed_signal = []
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
        self.graph_deleted = True
        self.graph_empty = True
