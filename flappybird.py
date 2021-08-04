#!/usr/bin/python3
#+ Autor:	Ran#
#+ Creado:	04/08/2021 20:01:46
#+ Editado:	04/08/2021 20:01:46

import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('carlistas.png').convert()
#bg_surface = pygame.transform.scale2x(bg_surface)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		screen.blit(bg_surface, (0,0))

	pygame.display.update()
	clock.tick(240)