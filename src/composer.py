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
    xAxis = np.linspace(0, np.pi * 2, 200)
    self.sinusoid_creator_array[self.sinusoid_index].yAxis = mag * np.sin((xAxis * freq) + phase)
    self.plotter_window_dict["Sinusoid"].plot_reference.setData(xAxis, self.sinusoid_creator_array[self.sinusoid_index].yAxis)
    #change axes and sliders to rad


def clearSinusoidal(self):
    xAxis = np.linspace(0, np.pi * 0, 200)
    yAxis = np.sin(xAxis)
    self.plotter_window_dict["Sinusoid"].plot_reference.setData(xAxis, yAxis)


def setSelectedSignal(self, Input):
    self.sinusoid_index = Input
    plotSinusoidal(self)
    print(self.sinusoid_creator_array[self.sinusoid_index]._is_added)


def setFrequency(self, Input):
    self.sinusoid_creator_array[self.sinusoid_index].frequency = Input
    plotSinusoidal(self)


def setMagnitude(self, Input):
    self.sinusoid_creator_array[self.sinusoid_index].magnitude = Input
    plotSinusoidal(self)


def setPhaseshift(self, Input):
    self.sinusoid_creator_array[self.sinusoid_index].phaseshift = Input
    plotSinusoidal(self)


def addSinusoidal(self):
    if self.sinusoid_creator_array[self.sinusoid_index]._is_added == False:
        self.sinusoid_creator_array[self.sinusoid_index]._is_added = True
        self.sinusoid_creator_array.append(classes.Sinusoid())
        self.sinusoid_number += 1
        self.signalsMenu.addItem("Signal " + str(self.sinusoid_number))
        self.signalsMenu.setCurrentIndex(len(self.sinusoid_creator_array) - 1)
    sumSinusoids(self)
    print(len(self.sinusoid_creator_array))


def deleteSinusoidal(self):
    self.sinusoid_creator_array.pop(self.sinusoid_index)
    self.signalsMenu.removeItem(self.sinusoid_index)



def sumSinusoids(self):
    yAxis_sum = self.sinusoid_creator_array[0].yAxis
    for item in self.sinusoid_creator_array:
        yAxis_sum += item.yAxis
    yAxis_sum -= self.sinusoid_creator_array[0].yAxis
    xAxis = np.linspace(0, np.pi * 2, 200)
    self.plotter_window_dict["Summed"].plot_reference.setData(xAxis, yAxis_sum)
    #bayez