
class Sinusoid():
    ''' One sinusoid function object'''
    def __init__(self, magnitude=1, phaseshift=0, frequency=1, sin_or_cos = 'sin'):
        self.magnitude = magnitude
        self.phaseshift = phaseshift  # in radians
        self.frequency = frequency
        self.sin_or_cos = sin_or_cos

        # self.np_object = self.generate_np_object()

    def generate_np_object(self):
        '''Should create a np sinusiod based on the input parameters'''
        return


class SampledSignal():
    '''An object containing sample points array'''
    def __init__(self, sampling_frequency=1, magnitude_array=[]):
        self.sampling_frequency = sampling_frequency
        self.magnitude_array = magnitude_array
        self.total_samples = len(magnitude_array)
        self.time_array = self.generate_time_array()

    def generate_time_array(self):
        for index in range(len(self.total_samples)):
            self.time_array.append(index/self.sampling_frequency)
