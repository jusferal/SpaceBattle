from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import math
import random as rdn
import numpy as np
from algos import *
from charc import *
from Entidades import *	
def main():
	scale = 2
	#width, height = scale*300, scale*300
	width, height = 680, 400
	pygame.init()
	pygame.display.set_caption('Treasures')
	
	display_openGL(width, height, scale)
	jug=Jugador()
	enemigo=Enemy()
	planeta= Planet()
  
	scenario()
	jug.Draw()
	planeta.Draw()
	enemigo.Draw(1)
	x,y =width/2-49,-99
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		keys = pygame.key.get_pressed()
		jug.update(keys)
		ataque=0
		if abs(enemigo.x-jug.disparar.x)<=14: 
			ataque=1
			jug.disparar.activo=0
			jug.disparar.Kill()
			jug.disparar.x=-width
		enemigo.update(ataque)
		#pygame.display.flip()
if __name__ == '__main__':
	main()
