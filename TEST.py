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
from math import *
x = np.array([0,1/0])
#print(degrees(atan(x[1]/x[0])))
print(np.arctan(x))
