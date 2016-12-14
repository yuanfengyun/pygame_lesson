import pygame
from pygame.locals import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((640,480),0,32)
  pygame.display.set_caption("hello")
  background = pygame.image.load("sushiplate.jpg").convert()
  cursor = pygame.image.load("fugu.png").convert_alpha()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        exit()
    screen.blit(background,(0,0))
    x,y = pygame.mouse.get_pos()
    x -= cursor.get_width() / 2
    y -= cursor.get_height() / 2
    screen.blit(cursor,(x,y))
    pygame.display.update()

main()
