'''
developed by
George Macrae 2014

'''

import pygame

clock = pygame.time.Clock()
fps = clock.tick(30) / 1000.0
projSpeed = 1
Hspeed = 10
Vspeed = 10



class laser:

	def __init__(self, x, y,hspeed,vspeed,dir):
	

		self.x_coor = x
		self.y_coor = y
		self.x_speed = hspeed
		self.y_speed = vspeed
		self.dirrection = dir

		
	def getCoord(self):
		return (self.x_coor,self.y_coor)
	
	def setx(self,x):
		self.x_coor = x
	def sety(self,y):
		self.y_coor = y

	def movex(self):
		dirr = self.dirrection
		if dirr == 0 or dirr == 2:
			r = 0

		if dirr == 1:
			r = 1

		if dirr == 3:
			r = -1

		projSpeed = 15
		try:
			self.x_coor += fps * (r * (projSpeed)) 
		except UnboundLocalError:
			return self.x_coor
		return self.x_coor


	def movey(self):
		dirr = self.dirrection
		if dirr == 1 or dirr == 3:
			r = 0

		if dirr == 0:
			r = -1

		if dirr == 2:
			r = 1
		projSpeed = 15
			
		try:
			self.y_coor += fps * (r * (projSpeed)) 
		except UnboundLocalError:	
			return self.y_coor


		return self.y_coor
	
	def setSpeedZero(self):
		projSpeed =0
	def getDir(self):
		return self.dirrection
