'''
developed by
George Macrae 2014

'''

import pygame

clock = pygame.time.Clock()
fps = clock.tick(30) / 1000.0
Hspeed = 10
Vspeed = 10

from math import *


class laser:

	def __init__(self, x, y,hspeed,vspeed,dir):
	

		self.x_coor = x
		self.y_coor = y
		self.x_speed = hspeed
		self.y_speed = vspeed
		self.dirrection = dir
		
		if dir >= 0 and dir < pi/2:
			self.x_coor-=10
			# self.y_coor-=10
			
		if dir>= pi/2 and dir < pi:
			self.x_coor+=10
			# self.y_coor-=10
		if dir>=-pi and dir < -pi/2:
			self.x_coor+=10
			# self.y_coor+=10
			
		if dir>= -pi/2 and dir < 0:
			self.x_coor-=10
			# self.y_coor+=10
			
	def getCoord(self):
		return (self.x_coor,self.y_coor)
	
	def setx(self,x):
		self.x_coor = x
	def sety(self,y):
		self.y_coor = y

	def move(self):
		projSpeed = 15
		dirr= self.dirrection
		dirr += pi/2

		self.y_coor += fps * (projSpeed * cos(-dirr))
		self.x_coor += fps * (projSpeed * sin(-dirr))

		return (self.x_coor, self.y_coor)
	
	def setSpeedZero(self):
		projSpeed =0
	def getDir(self):
		return self.dirrection
