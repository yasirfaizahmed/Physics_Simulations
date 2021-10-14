import numpy as np
import pyqtgraph as qt
from pyqtgraph.Qt import QtCore, QtGui
import time
from body import Body



b1 = Body(initpos=[0,0], mass=1, radius=1, velocity=[0,0], initforce=[1,1])
#force = np.array([1,0])
#b1.UpdateNetForce(force)


b1.UpdateNetForce([1,1])
b1.Display()

t = np.arange(0,10,0.2)
v = np.array([])
for t_inst in t:
	v = np.append( v, b1.Mag(b1.UpdateVelocity(t_inst)) )
	 

qt.plot(t, v)

if __name__ == '__main__':
     
    # importing system
    import sys
     
    # Start Qt event loop unless running in interactive mode or using
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()