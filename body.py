from math import *
import numpy as np
import pyqtgraph as qt
from pyqtgraph.Qt import QtCore, QtGui
from PyQt5 import QtTest

def PlotData(qt_obj, x_data, y_data, delay):
	prev = []
	for indx, x_inst in enumerate(x_data):
		if indx == 0:
			prev = [x_data[0], y_data[0]]
		else:
			prev = [x_data[indx-1], y_data[indx-1]]
		qt_obj.plot([x_inst,prev[0]], [y_data[indx],prev[1]])
		QtTest.QTest.qWait(delay)


class Body:
	force_list = np.array( [[]] )
	
	def Mag(self, a):
		return np.sqrt(a.dot(a))
	
	def __init__(self, initpos = [0,0], mass=1, radius=1, velocity=[0,0], initforce=[0,0]):
		self.__position = np.array(initpos)
		self.__mass = mass
		self.__radius = radius
		self.__velocity = np.array(velocity)
		self.__netforce = np.array(initforce)
		self.__magnetforce = self.Mag(self.__netforce)
		self.__angle = np.array([0, 0])
		
		np.append(self.force_list, initforce)
		try:
			for f in self.force_list:
				self.__netforce += f
		except:
			pass
		self.__angle = np.arctan2(self.__netforce[1], self.__netforce[0])
		
	def UpdateNetForce(self, force=[0,0]):
		np.append(self.force_list, force)
		self.__netforce += force
	
	def GetVelocity(self, t_inst):
		self.__velocity = (self.__netforce/self.__mass)*t_inst
		return self.__velocity
		
	def GetPosition(self, t_inst):
		self.__position = self.GetVelocity(t_inst)*t_inst
		return self.__position
		
	def GetData(self, t, datatype):
		temp = np.array([])
		for t_inst in t:
			if datatype == "velocity":
				temp = np.append(temp, self.Mag(self.GetVelocity(t_inst)))
			elif datatype == "Xdis":
				temp = np.append(temp, self.GetPosition(t_inst)[0])
			elif datatype == "Ydis":
				temp = np.append(temp, self.GetPosition(t_inst)[1])
		return temp
		
	
		
			
	def Display(self):
		pass
		#print("{}:{}:{}:{}:{}".format(self.__mass, self.__radius, self.__velocity, self.__netforce, self.__magnetforce))
		#print( "{}:{}".format(self.__netforce, degrees(self.__angle)) ) 
		
		