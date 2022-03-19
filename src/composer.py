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

from unittest import case
from matplotlib.axis import YAxis
import numpy as np

import classes
import interface
import main
import utility as util


# PLOTS THE SELECTED SINE IN SMALL COMPOSER WINDOW
def plotSinusoidal(self):
    
    # Get sliders values
    freq = self.frequencySlider.value()
    mag = self.magnitudeSlider.value()
    phase = self.phaseSlider.value()
    
    # Set axes and plot
    xAxis = np.linspace(0, np.pi * 2, 200)
    yAxis = mag * np.sin((xAxis * freq) + phase)
    pi_labels = [(0, 0), (np.pi / 2, "π/2"), (np.pi, "π"), (3 * np.pi / 2, "3π/2"), (np.pi * 2, "2π")]
    self.plotter_window_dict["Sinusoid"].plot_reference.setData(
        xAxis, yAxis)
    ax=self.sinusoidalSignal.getAxis('bottom')
    ax.setTicks([pi_labels])


    # CLEARS SINE PLOT WINDOW
def clearSinusoidal(self):
    xAxis = np.linspace(0, np.pi * 0, 200)
    yAxis = np.sin(xAxis)
    self.plotter_window_dict["Summed"].plot_reference.setData(xAxis, yAxis)


    # CALLED WHEN MENU INDEX CHANGES TO UPDATE COMPOSER DATA
def updateSinusoid(self, input):
    self.sinusoid_index = input

    # Set slider values to appropriate positions when user selects already added signal
    if len(self.sinusoid_creator_array) !=0:
        if self.sinusoid_index < len(self.sinusoid_creator_array):
            self.frequencySlider.setValue(
                self.sinusoid_creator_array[self.sinusoid_index].frequency)
            self.magnitudeSlider.setValue(
                self.sinusoid_creator_array[self.sinusoid_index].magnitude)
            self.phaseSlider.setValue(
                self.sinusoid_creator_array[self.sinusoid_index].phaseshift)
            self.deleteSineButton.show()
        # Set slider values to default when yet to be confirmed signal is selected
        else:
            self.frequencySlider.setValue(1)
            self.magnitudeSlider.setValue(1)
            self.phaseSlider.setValue(0)
            self.deleteSineButton.hide()
    else:
        self.frequencySlider.setValue(1)
        self.magnitudeSlider.setValue(1)
        self.phaseSlider.setValue(0)
        self.deleteSineButton.hide()
    plotSinusoidal(self)


    # ADDS GENERATED SINE TO SUMMER
def addSinusoidal(self):

    # Add new sine
    if self.sinusoid_index == len(self.sinusoid_creator_array):
        self.sinusoid_creator_array.append(classes.Sinusoid(index=self.sinusoid_index, magnitude=self.magnitudeSlider.value(
        ), phaseshift=self.phaseSlider.value(), frequency=self.frequencySlider.value()))
        self.sinusoid_number += 1
        self.signalsMenu.addItem("Signal " + str(self.sinusoid_number))
        
        # Edit existing sine
    else:
        self.sinusoid_creator_array[self.sinusoid_index].frequency = self.frequencySlider.value()
        self.sinusoid_creator_array[self.sinusoid_index].magnitude = self.magnitudeSlider.value()
        self.sinusoid_creator_array[self.sinusoid_index].phaseshift = self.phaseSlider.value()
        xAxis = np.linspace(0, np.pi * 2, 200)
        self.sinusoid_creator_array[self.sinusoid_index].yAxis = self.magnitudeSlider.value() * np.sin((xAxis * self.frequencySlider.value()) + self.phaseSlider.value())
    sumSinusoids(self)
    self.signalsMenu.setCurrentIndex(len(self.sinusoid_creator_array))


def deleteSinusoidal(self):
    self.sinusoid_creator_array.pop(self.sinusoid_index)
    self.signalsMenu.removeItem(self.sinusoid_index)
    sumSinusoids(self)


def sumSinusoids(self):
    xAxis = np.linspace(0, np.pi * 2, 200)

    # Create SummedSinusoid object with array of sinusoids where they get summed
    if len(self.sinusoid_creator_array) > 0:
        self.summed_signal = classes.SummedSinusoid(
            self.sinusoid_creator_array)
        pi_labels = [(0, 0), (np.pi / 2, "π/2"), (np.pi, "π"), (3 * np.pi / 2, "3π/2"), (np.pi * 2, "2π")]
        self.plotter_window_dict["Summed"].plot_reference.setData(
            xAxis, self.summed_signal.yAxis)
        ax=self.summedSignal.getAxis('bottom')
        ax.setTicks([pi_labels])
        util.printDebug("Max analog freq component: " +
                        str(self.summed_signal.max_analog_frequency))

    # If all sines are deleted
    else:
        clearSinusoidal(self)




def clearComposer(self):
    clearSinusoidal(self)
    self.sinusoid_creator_array = []
    self.signalsMenu.clear()
    self.sinusoid_number = 1
    self.signalsMenu.addItem("Signal " + str(self.sinusoid_number))

