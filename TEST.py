# from matplotlib import pyplot as plt

# class Dot:
	# x_cor = 0
	# y_cor = 0
	# radius = 1
	# def __init__(self, x = 0, y = 0, r = 1):
		# self.x_cor = x
		# self.y_cor = y
		# self.radius = r
		
		
	# def MoveTo(self, x, y):
		# self.x_cor = x
		# self.y_cor = y
	
	# def ChangeRad(self, r):
		# self.radius = r

# def main():
	# dots = []
	# for i in range(10):
		# dots.append(Dot(r=i+1))
	
	# for i in range(10):
		# print("{}:{}:{}".format(dots[i].x_cor, dots[i].y_cor, dots[i].radius))
		
	
# main()

import numpy as np
import pyqtgraph as qt
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5 import QtTest
from math import *
x = np.array([2,4])
import sys

plt = qt.plot()
app = qt.mkQApp()

t = np.arange(0, 10, 1)
x = np.array([9,6,7,8,6,7,5,4,3,4,5,6,7,8,9,7,6,6,5,8])
z = np.array([1,2,3,4,5,6,7,8,5,6,7,5,3,4,5,6,7,3,5,4])

def PlotData(qt_obj, x_data, delay, **kwargs):
	prev = {}
	keys = kwargs.keys()
		
	for indx, x_inst in enumerate(x_data):
		for key in keys:
			if indx == 0:
				prev[key] = [x_data[0], kwargs[key][0]]
			else:
				prev[key] = [x_data[indx-1], kwargs[key][indx-1]]
			qt_obj.plot( [x_inst, prev[key][0]], [kwargs[key][indx],prev[key][1]], pen=qt.mkPen('b', width=5))
		
		QtTest.QTest.qWait(delay)





PlotData(qt_obj=plt, x_data=t, y_data=x, delay=200, z_data=z)




	
	
if __name__ == '__main__':
     
    # importing system
    import sys
     
    # Start Qt event loop unless running in interactive mode or using
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        sys.exit(app.exec_())