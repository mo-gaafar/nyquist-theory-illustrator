
import numpy as np

class Sinusoid():
    ''' One sinusoid function object'''

    def __init__(self, index=0, magnitude=1, phaseshift=0, frequency=1, sin_or_cos='sin', _is_added=False):
        self.index = index
        self.magnitude = magnitude
        self.phaseshift = phaseshift  # in radians
        self.frequency = frequency
        self.sin_or_cos = sin_or_cos
        self._is_added = _is_added
        self.xAxis = np.linspace(0, np.pi * 2, 200)
        self.yAxis = self.magnitude * np.sin((self.xAxis * self.frequency) + self.phaseshift)

        # self.np_object = self.generate_np_object()
    def __add__(self, sinusoid2):
        ''' Operator overloading '''
        return self.yAxis + sinusoid2.yAxis

    def get_frequency(self):
        return self.frequency

    def generate_np_object(self):
        '''Should create a np sinusiod based on the input parameters'''
        return


class SummedSinusoid():
    ''' Data object containing the small sinusoids and their magnitude sum'''

    def __init__(self, sinusoid_array=[Sinusoid()]):
        self.sinusoid_array = sinusoid_array
        self.max_analog_frequency = 1
        self.xAxis = []
        self.yAxis = []
        
        if len(sinusoid_array) > 0:
            self.xAxis = sinusoid_array[0].xAxis  # TODO: think of a better way
            yAxis_sum = sinusoid_array[0].yAxis

            if len(sinusoid_array) > 1:
                for index in range(len(self.sinusoid_array)):
                    if index != 0:
                        yAxis_sum = yAxis_sum + self.sinusoid_array[index].yAxis
            self.yAxis = yAxis_sum
            self.max_analog_frequency = self._get_max_frequency()

    def _get_max_frequency(self):
        ''' written because I dont know how to get max of an array of object attributes '''
        maxfrequency = -999
        for item in self.sinusoid_array:
            if item.frequency > maxfrequency:
                maxfrequency = item.frequency

        return maxfrequency


class SampledSignal():
    '''An object containing sample points array'''

    def __init__(self, sampling_frequency=1, magnitude_array=[]):
        self.sampling_frequency = sampling_frequency
        self.max_analog_frequency = (1/2)*self.sampling_frequency
        self.magnitude_array = magnitude_array
        self.total_samples = len(magnitude_array)
        self.time_array = []
        self.generate_time_array()

    def generate_time_array(self):
        for index in range(self.total_samples):
            self.time_array.append(index/self.sampling_frequency)
    


class Signal():
    '''An object containing the generic signal'''
    def __init__(self, magnitude = [], time = [] , max_analog_frequency = 1):
        self.magnitude= magnitude
        self.time= time
        self.max_analog_frequency= max_analog_frequency
    


class PlotterWindow():
    '''Abstraction of plotter window properties'''

    def __init__(self, plot_reference,  x_start=0, x_end=1, y_start=-1, y_end=1):
        self.plot_reference = plot_reference
        
        self.x_range_tuple = (x_start, x_end)
        self.y_range_tuple = (y_start, y_end)

    def update_plot(self, PlotWindow):
        "Updates range of passed plot instance"
        self.plot_reference.setXRange(xMin=self.x_range_tuple[0], xMax=self.x_range_tuple[1],
                                      yMin=self.y_range_tuple[0], yMax=self.y_range_tuple[1])
