'''
developed by
George Macrae 2014

'''

import pygame, sys

from pygame.locals import *

from laser import *

from pygame.locals import *
from socket import *

import threading


FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 750



def start(player):

	pygame.init()
	global screen
	screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption('Space')

	score = 0
	score_en = 0

	back = pygame.Surface((WINDOWWIDTH,WINDOWHEIGHT))
	background = back.convert()
	background.fill((0,0,0))
	ship = pygame.Surface((10,10))
	
	global ship1
	ship1 = ship.convert()
	ship1.fill((0,255,0))


	global ship2
	global ship2_Vmove 

	global ship2_Hmove
	global ship2_x
	global ship2_y
	global ship1_x
	global ship1_y

	global laserlist

	ship2 = ship.convert()
	ship2.fill((0,0,255))

	Vspeed = 10.
	Hspeed = 10.
	ship1_Vmove = 0
	ship1_Hmove = 0
	
	ship1_x = 220
	ship1_y = 620
	ship2_x = 20
	ship2_y = 620
	
	if player == 'p1':
		ship1_x = 20
		ship1_y = 620
		ship2_x = 220
		ship2_y = 620


	ship2_Vmove = 0
	ship2_Hmove = 0
	
	laserlist = []

	clock = pygame.time.Clock()
	fps = clock.tick(30) / 1000.0

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				if event.key == K_UP:
					ship1_Vmove = -Vspeed * fps
				elif event.key == K_DOWN:
					ship1_Vmove = Vspeed * fps
				elif event.key == K_LEFT:
					ship1_Hmove = -Hspeed * fps
				elif event.key == K_RIGHT:
					ship1_Hmove = Hspeed * fps
				
				elif event.key == K_w:
					l=laser(ship1_x,ship1_y-20,Hspeed,Vspeed,0)
					laserlist.append(l)
					clientsocket.send(str(ship1_x)+":"+str(ship1_y-20)+':'+str(player)+':laser:0')

				elif event.key == K_d:
					l=laser(ship1_x+20,ship1_y,Hspeed,Vspeed,1)
					laserlist.append(l)
					clientsocket.send(str(ship1_x+20)+":"+str(ship1_y)+':'+str(player)+':laser:1')

				elif event.key == K_s:
					l=laser(ship1_x,ship1_y+20,Hspeed,Vspeed,2)
					laserlist.append(l)
					clientsocket.send(str(ship1_x)+":"+str(ship1_y+20)+':'+str(player)+':laser:2')

				elif event.key == K_a:
					l=laser(ship1_x-20,ship1_y,Hspeed,Vspeed,3)
					laserlist.append(l)
					clientsocket.send(str(ship1_x-20)+":"+str(ship1_y)+':'+str(player)+':laser:3')


			elif event.type == KEYUP:
				if event.key == K_UP:
					ship1_Vmove = 0.
				if event.key == K_DOWN:
					ship1_Vmove = 0.
				if event.key == K_LEFT:
					ship1_Hmove = 0.
				if event.key == K_RIGHT:
					ship1_Hmove = 0.


		screen.blit(background,(0,0))
		screen.blit(ship1,(ship1_x,ship1_y))

		screen.blit(ship2,(ship2_x,ship2_y))


   		ship1_x += ship1_Hmove
		ship1_y += ship1_Vmove 
		
		clientsocket.send(str(ship1_x)+":"+str(ship1_y)+':'+str(player)+':move')


   		if ship1_x >= WINDOWWIDTH : ship1_x = WINDOWWIDTH
		if ship1_x <= 0 : ship1_x = 0

		if ship1_y >= WINDOWHEIGHT : ship1_y = WINDOWHEIGHT
		if ship1_y <= 0 : ship1_y = 0


		for x in laserlist:
			p = pygame.Surface((10,10))
			p1= p.convert()
			p1.fill((255,0,0))

			coord = x.getCoord()
			if coord[0] >= WINDOWWIDTH :
				laserlist.remove(x)
			else:
				xc = x.movex()
				yc = x.movey()

			if coord[0] <= 0 :
				laserlist.remove(x)
			else:
				xc = x.movex()
				yc = x.movey()
	
			if coord[1] >= WINDOWHEIGHT :
				laserlist.remove(x)
			else:
				xc = x.movex()
				yc = x.movey()
	
			if coord[1] <= 0 :
				laserlist.remove(x)
			else:
				xc = x.movex()
				yc = x.movey()

			x.setSpeedZero()


			if xc +10 > ship2_x and xc - 10 < ship2_x and yc + 10 > ship2_y and yc - 10 < ship2_y:
				laserlist.remove(x)
				score = score+1
				print 'SCORE: YOU= '+str(score)+' ENEMY= '+str(score_en)

			if xc +10 > ship1_x and xc - 10 < ship1_x and yc + 10 > ship1_y and yc - 10 < ship1_y:
				laserlist.remove(x)
				score_en +=1

				print 'SCORE: YOU= '+str(score)+' ENEMY= '+str(score_en)
				# if yc -2 < ship2_y and ship2_y < yc +2:
				# 	print "hit"
			screen.blit(p1,(xc,yc))

		pygame.display.update()

def listener(clientsocket):
	global ship2_x
	global ship2_y
	ship2_x = 220
	ship2_y = 620
	global laserlist
	while True:

		data = clientsocket.recv(1024)
		
		data2 = data.split(':')

		if data2[3] == 'laser':
			x = data2[4].split('.')
			y = data2[0].split('.')
			z = data2[1].split('.')
			l=laser(int(y[0]),int(z[0]),10,10,int(x[0]))
			laserlist.append(l)

		elif data2[3] == 'move':
			try:
				x = data2[0].split('.')
				y = data2[1].split('.')

				ship2_x = float(x[0])
				ship2_y = float(y[0])

			except ValueError:
				print "ValueError"
		

if __name__ == '__main__':

	print "waiting for connection"
	host = gethostbyname(gethostname())
 	port = 9999
 	addr = (host, port)
 	clientsocket = socket(AF_INET, SOCK_STREAM)
 	clientsocket.connect(addr)
 	 

 	data = clientsocket.recv(1024)
 	print str(data)
	player = data
	r_thread = threading.Thread(target = listener, args = (clientsocket,))
 	r_thread.start()
 	
 	start(player)