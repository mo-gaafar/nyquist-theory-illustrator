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

import numpy as np

import classes
import interface
import main



def plotSinusoidal(self):
    freq = self.sinusoid_creator_array[self.sinusoid_index].frequency
    mag = self.sinusoid_creator_array[self.sinusoid_index].magnitude
    phase = self.sinusoid_creator_array[self.sinusoid_index].phaseshift
    xAxis = np.linspace(0, np.pi * freq, 200)
    yAxis = mag * np.sin(xAxis + phase)
    self.plotter_window_dict["Sinusoid"].plot_reference.setData(xAxis, yAxis)
    #change axes and sliders to rad


def setSelectedSignal(self, Input):
    self.sinusoid_index = Input


def setFrequency(self, Input):
    self.sinusoid_creator_array[self.sinusoid_index].frequency = Input
    plotSinusoidal(self)


def setMagnitude(self, Input):
    self.sinusoid_creator_array[self.sinusoid_index].magnitude = Input
    plotSinusoidal(self)


def setPhaseshift(self, Input):
    self.sinusoid_creator_array[self.sinusoid_index].phaseshift = Input
    plotSinusoidal(self)


def addSinusoidal():
    np.append(self.sinusoid_creator_array, Sinusoid())
    #add combobox item