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

plt = qt.plot()

t = np.arange(0, 10, 0.5)
x = np.array([9,6,7,8,6,7,5,4,3,4,5,6,7,8,9,7,6,6,54,8])
temp = [t[0], x[0]]
for i,tt in enumerate(t):
	plt.plot([tt,temp[0]], [x[i],temp[1]])
	temp = [tt, x[i]]
	QtTest.QTest.qWait(500)
	
if __name__ == '__main__':
     
    # importing system
    import sys
     
    # Start Qt event loop unless running in interactive mode or using
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()