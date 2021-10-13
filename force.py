import numpy as np
import pyqtgraph as qt
from pyqtgraph.Qt import QtCore, QtGui
import time
from body import Body



b1 = Body(mass=1, radius=1, velocity=[0,0], initforce=[1,1])
#force = np.array([1,0])
#b1.UpdateNetForce(force)

qt.plot([1,2,3], [2,3,4])

b1.UpdateNetForce([1,1])
b1.Display()


if __name__ == '__main__':
     
    # importing system
    import sys
     
    # Start Qt event loop unless running in interactive mode or using
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()