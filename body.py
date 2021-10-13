from math import *
import numpy as np

def Mag(a):
	return np.sqrt(a.dot(a))

class Body:
	force_list = np.array( [[0,0],[0,0]] )
	def __init__(self, mass=1, radius=1, velocity=[0,0], initforce=[0,0]):
		self.__mass = mass
		self.__radius = radius
		self.__velocity = np.array(velocity)
		self.__netforce = np.array(initforce)
		self.__magnetforce = Mag(self.__netforce)
		self.__angle = np.array([0, 0])
		
		np.append(self.force_list, initforce)
		for f in self.force_list:
			self.__netforce += f
		print(self.__netforce[1], self.__netforce[0])
		self.__angle = np.arctan2(self.__netforce[1], self.__netforce[0])
		
	def UpdateNetForce(self, force=[0,0]):
		np.append(self.force_list, force)
		self.__netforce += force

			
	def Display(self):
		pass
		#print("{}:{}:{}:{}:{}".format(self.__mass, self.__radius, self.__velocity, self.__netforce, self.__magnetforce))
		print( "{}:{}".format(self.__netforce, degrees(self.__angle)) ) 
		
		