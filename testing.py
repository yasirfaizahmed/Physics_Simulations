
from math import *
import numpy as np

def Mag(a):
	return np.sqrt(a.dot(a))

class Body:
	force_list = np.array( [[]] )
	def __init__(self, mass=1, radius=1, velocity=[0,0], initforce=[0,0]):
		self.__mass = mass
		self.__radius = radius
		self.__velocity = np.array(velocity)
		self.__netforce = np.array(initforce)
		self.__magnetforce = Mag(self.__netforce)
		
	def GetAlpha(self, force):
		theta1, theta2 = 0, 0
		if self.__netforce[1] == 0 and self.__netforce[0] != 0:
			theta1 = 0.0
		elif self.__netforce[1] != 0 and self.__netforce[0] == 0:
			theta1 = radians(90.0)
		elif self.__netforce[1] == 0 and self.__netforce[0] == 0:
			theta1 = 0.0
		else:
			theta1 = atan(self.__netforce[1]/self.__netforce[0])
			print(theta1)
			
		if force[1] == 0 and force[0] != 0:
			theta2 = 0.0
		elif force[1] != 0 and force[0] == 0:
			theta2 = radians(90.0)
		elif force[1] == 0 and force[0] == 0:
			theta2 = 0.0
		else:
			theta2 = atan(force[1]/force[0])
			print(theta2)
		alpha = (theta1 - theta2)
		if alpha < 0:
			return alpha*-1
		return alpha
	
	def GetTheta(self, force, alpha):
		temp = self.__magnetforce*sin(alpha) / (Mag(force) + self.__magnetforce*cos(alpha))
		return atan(temp)
		
	
	def UpdateNetForce(self, force):
		self.__magnetforce = Mag(self.__netforce)
		for force in self.force_list:
			magforce = Mag(force)
			alpha = self.GetAlpha(force)
			magnetforce = sqrt( (self.__magnetforce**2) + (magforce**2) + 2*self.__magnetforce*magforce*cos(alpha) )
			theta = self.GetTheta(force, alpha)
			
			self.__netforce = [magnetforce*cos(theta), magnetforce*sin(theta)]
			
	def Display(self):
		print("{}:{}:{}:{}:{}".format(self.__mass, self.__radius, self.__velocity, self.__netforce, self.__magnetforce))
		print( "{}".format( degrees(self.GetAlpha([0,0])) ) )