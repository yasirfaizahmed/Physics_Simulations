from math import *
import numpy as np


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
		print(self.__netforce[1], self.__netforce[0])
		self.__angle = np.arctan2(self.__netforce[1], self.__netforce[0])
	
	
		
	def UpdateNetForce(self, force=[0,0]):
		np.append(self.force_list, force)
		self.__netforce += force
	
	def UpdateVelocity(self, t_inst):
		self.__velocity = (self.__netforce/self.__mass)*t_inst
		return self.__velocity
		
	def UpdatePosition(self, t_inst):
		self.__position = self.UpdateVelocity(t_inst)*t_inst
		return self.__position
		
			
	def Display(self):
		pass
		#print("{}:{}:{}:{}:{}".format(self.__mass, self.__radius, self.__velocity, self.__netforce, self.__magnetforce))
		print( "{}:{}".format(self.__netforce, degrees(self.__angle)) ) 
		
		