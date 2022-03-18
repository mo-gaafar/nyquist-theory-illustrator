''' 
1. Updates the plot with the actual signal and interpolated signal
2. plots intersection points each time
3. updates the graph when the '''

import classes
import numpy as np
import utility as util


def move_to_viewer(self, Input):
    print("move")

    if Input =="composer" :
        print("composer_if")
        #plot summed signal on primary and secondary screens (DONE)
        #we need to get  the summed signal (DONE)
        self.signal=self.summed_signal
        self.plotter_window_dict["Primary"].plot_reference.setData(self.summed_signal.xAxis, self.summed_signal.yAxis)
        self.plotter_window_dict["Secondary"].plot_reference.setData(self.summed_signal.xAxis, self.summed_signal.yAxis)
    
    elif Input == "browse":
        self.plotter_window_dict["Primary"].plot_reference.setData(self.summed_signal.xAxis, self.summed_signal.yAxis)        
        self.plotter_window_dict["Secondary"].plot_reference.setData(self.summed_signal.xAxis, self.summed_signal.yAxis)

        # plot the browsed signal on the prim and sec screens 
        # change 
       
    #plot it on the primary and secondary screens
    # add changes on the prim screen    

 
    #TODO change the tab to viewer
        # TODO  if not make a dialogue box 

def change_sampling_rate (self):
    
    # add points based on sampling rate 
    # plot the points
    # connect them by using interpolation 
    # plot the interpolated signal 
    # 3 Fmax

    return 

def delete_primary_secondary(self):
    self.plotter_window_dict["Primary"].plot_reference.setData(xAxis=0,yAxis=0)
    self.plotter_window_dict["Secondary"].plot_reference.setData(xAxis=0,yAxis=0)


