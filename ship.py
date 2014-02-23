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


class ship:

	def __init__(self, x, y,colour,WINDOWWIDTH,WINDOWHEIGHT):
		self.wH = WINDOWHEIGHT
		self.wW = WINDOWWIDTH

		self.shipSurface = pygame.Surface((10,10))
		self.ship = self.shipSurface.convert()
		self.ship.fill((colour))

		self.ship_x = x
		self.ship_y = y
		self.ship_Vmove = 0
		self.ship_Hmove = 0
	def moveUp(self):
		self.ship_Vmove = -Vspeed * fps
	def moveDown(self):
		self.ship_Vmove = Vspeed * fps
	def moveLeft(self):
		self.ship_Hmove =  -Hspeed * fps
	def moveRight(self):
		self.ship_Hmove = Hspeed * fps
	def horizontalSlow(self):
		self.ship_Hmove = 0
	def verticalSlow(self):
		self.ship_Vmove = 0
	def updatePosition(self):
		self.ship_x += self.ship_Hmove
		self.ship_y += self.ship_Vmove
		if self.ship_x >= self.wW : self.ship_x = self.wW
		if self.ship_x <= 0 : self.ship_x = 0

		if self.ship_y >= self.wH : self.ship_y = self.wH
		if self.ship_y <= 0 : self.ship_y = 0

	def setX(self,x):
		self.ship_x = x
	def setY(self,y):
		self.ship_y = y
	def getX(self):
		return self.ship_x
	def getY(self):
		return self.ship_y
	def getShip(self):
		return self.ship


	