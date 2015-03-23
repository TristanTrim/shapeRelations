
import pygame
import random
import math

# Window dimensions
width = 640
height = 400

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

rad=25
while running:

    for ii in range(360):
        screen.set_at([int(100+math.cos(ii)*rad),int(100+math.sin(ii)*rad)],(222,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(1000)
