import numpy as np
import pyqtgraph as qt
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5 import QtTest
import time
from body import *



b1 = Body(initpos=[0,0], mass=1, radius=1, velocity=[0,0], initforce=[0,0])
#force = np.array([1,0])
#b1.UpdateNetForce(force)


b1.UpdateNetForce([2,1])

t_list = [0, 10, 20]
delta = 0.2
delta_time = int(delta*1000)

t = np.arange(t_list[0], t_list[1], delta)
v = np.array([])
x = np.array([])
y = np.array([])

plt = qt.plot()

v = b1.GetData(t, "velocity")
x = b1.GetData(t, "Xdis")
y = b1.GetData(t, "Ydis")


PlotData(qt_obj=plt, x_data=t, y_data=x, delay=200, z_data=v)







if __name__ == '__main__':
    
    # importing system
    import sys
     
    # Start Qt event loop unless running in interactive mode or using
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()