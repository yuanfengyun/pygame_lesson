#!/bin/python
#coding=utf-8
import pygame
from pygame.locals import *

pygame.init()
font = pygame.font.SysFont("DejaVu",64)
text_surface = font.render("font test",
	True,		#抗锯齿
	(0,0,0),	#文字颜色	
	(255,255,255))  #背景颜色

pygame.image.save(text_surface, "name.png")
screen = pygame.display.set_mode((640,480),0,32)
screen.blit(text_surface,(0,0))
pygame.display.update()
