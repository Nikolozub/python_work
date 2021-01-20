#!/usr/bin/env python3

import pygame
from pygame.draw import *
from math import *
import numpy as np

def rotate_matrix( x, y, angle ):
	s = sin(angle)
	c = cos(angle)
	return np.array([	[c, 	s, 	0],
						[-s, 	c, 	0],
						[-x * (c - 1) + y * s, -y * (c - 1) - x * s, 1]
					])	

def trapez_matrix( center_X = 100, center_Y = 100, small_base = 50, big_base = 100, height = 50 ):
	return np.array([ (center_X - small_base / 2, center_Y - height / 2, 1),
						(center_X + small_base / 2, center_Y - height / 2, 1),
						(center_X + big_base / 2, center_Y + height / 2, 1),
						(center_X - big_base / 2, center_Y + height / 2, 1 )
					])
	
def matrix_to_points(matrix):
	matrix = matrix.tolist()
	for line in matrix:
		line.pop()
	return	matrix

	

pygame.init()

screen = pygame.display.set_mode((400, 400))

color = (255, 255, 255)
x = 100
y = 200
t_matrix = trapez_matrix(center_X = x, center_Y = y, height = 20)
rot_matrix = rotate_matrix(x,y, pi/3)

points = matrix_to_points( t_matrix.dot(rot_matrix) )
	
polygon(screen, color, points)


pygame.display.update()

finished = False

while not finished:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
			
pygame.quit()
