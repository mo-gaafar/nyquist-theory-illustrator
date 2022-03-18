# COMPOSER MODULE

# WHAT SHOULD THE COMPOSER DO?
'''
Rightmost graph
1. Connect to all the sliders
2. Modify(return) "sinusoid" object accordingly
X. if confirmation button is clicked, 1. pass finished sinusiod object array to the summing function
                                      2. create new sinusiod object to start modifying again
X. if delete sinusiod button is clicked, 1.sinusiod creator array.pop(current combobox index) 
                                        2. update combobox accordingly?
Leftmost graph
1. Connect to confirmation button of sinusoid creator
2. if sinusoid confirmation or deletion button is clicked trigger the sine summing function
3. and then update plot with the sine summing function's output array'''

from matplotlib.axis import YAxis
import numpy as np

import classes
import interface
import main
import utility as util


def plotSinusoidal(self):
    #freq = self.sinusoid_creator_array[self.sinusoid_index].frequency
    #mag = self.sinusoid_creator_array[self.sinusoid_index].magnitude
    #phase = self.sinusoid_creator_array[self.sinusoid_index].phaseshift
    #xAxis = np.linspace(0, np.pi * 2, 200)
    #self.sinusoid_creator_array[self.sinusoid_index].yAxis = mag * \
    #    np.sin((xAxis * freq) + phase)
    #self.plotter_window_dict["Sinusoid"].plot_reference.setData(
    #    xAxis, self.sinusoid_creator_array[self.sinusoid_index].yAxis)

    freq = self.frequencySlider.value()
    mag = self.magnitudeSlider.value()
    phase = self.phaseSlider.value()
    xAxis = np.linspace(0, np.pi * 2, 200)
    yAxis = mag * np.sin((xAxis * freq) + phase)
    self.plotter_window_dict["Sinusoid"].plot_reference.setData(
        xAxis, yAxis)

    # change axes and sliders to rad


def clearSinusoidal(self):
    xAxis = np.linspace(0, np.pi * 0, 200)
    yAxis = np.sin(xAxis)
    self.plotter_window_dict["Sinusoid"].plot_reference.setData(xAxis, yAxis)
    sumSinusoids(self)  # calls sum sinusoids again to update sum


def setSelectedSignal(self, Input):
    self.sinusoid_index = Input
    if self.sinusoid_index < len(self.sinusoid_creator_array):
        self.signalsMenu.currentIndexChanged.connect(
        lambda: self.frequencySlider.setValue(self.sinusoid_creator_array[self.sinusoid_index].frequency))
        self.signalsMenu.currentIndexChanged.connect(
        lambda: self.magnitudeSlider.setValue(self.sinusoid_creator_array[self.sinusoid_index].magnitude))
        self.signalsMenu.currentIndexChanged.connect(
        lambda: self.phaseSlider.setValue(self.sinusoid_creator_array[self.sinusoid_index].phaseshift))
    else:
        self.signalsMenu.currentIndexChanged.connect(
        lambda: self.frequencySlider.setValue(1))
        self.signalsMenu.currentIndexChanged.connect(
        lambda: self.magnitudeSlider.setValue(1))
        self.signalsMenu.currentIndexChanged.connect(
        lambda: self.phaseSlider.setValue(0))
    plotSinusoidal(self)


def addSinusoidal(self):
    #if self.sinusoid_creator_array[self.sinusoid_index]._is_added == False:
        #self.sinusoid_creator_array[self.sinusoid_index]._is_added = True
    self.sinusoid_creator_array.append(classes.Sinusoid(index = self.sinusoid_index, magnitude = self.magnitudeSlider.value(), phaseshift = self.phaseSlider.value(), frequency = self.frequencySlider.value()))
    self.sinusoid_number += 1
    self.signalsMenu.addItem("Signal " + str(self.sinusoid_number))
    sumSinusoids(self)
    self.signalsMenu.setCurrentIndex(len(self.sinusoid_creator_array))
    print(len(self.sinusoid_creator_array))
    print(self.signalsMenu.currentIndex())
    print("-----------")


def deleteSinusoidal(self):
    self.sinusoid_creator_array.pop(self.sinusoid_index)
    self.signalsMenu.removeItem(self.sinusoid_index)
    sumSinusoids(self)
    print(len(self.sinusoid_creator_array))
    print(self.signalsMenu.currentIndex())
    print("-----------")


def sumSinusoids(self):
    xAxis = np.linspace(0, np.pi * 2, 200)

    if len(self.sinusoid_creator_array) > 1:
        self.summed_signal = classes.SummedSinusoid(self.sinusoid_creator_array)
        self.plotter_window_dict["Summed"].plot_reference.setData(
        xAxis, self.summed_signal.yAxis)
        #xAxis = np.linspace(0, np.pi * 2, 200)
        util.printDebug("Max analog freq component: " +
                        str(self.summed_signal.max_analog_frequency))
    else:
        self.summed_signal = self.sinusoid_creator_array
        self.plotter_window_dict["Summed"].plot_reference.setData(
        xAxis, self.sinusoid_creator_array[self.sinusoid_index].yAxis)

    # TODO: it keeps automatically summing an extra 1hz default sine wave on confirm
    # TODO: sum does not update on delete??
    # TODO: program crashes when all the signal are deleted
