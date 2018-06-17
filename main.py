import pygame
import os
import sys

from mfile import * # my file class file :)
from conf import * # my config file
        
pygame.init()
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("Virtual Desktop")
clock = pygame.time.Clock()

p = MFile()
#Game Loop
running = True
while running:
    # screen speed
    clock.tick(FPS)

    #Process input
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        running = False
        
    for event in pygame.event.get():
        #chech for closing the window
        if event.type == pygame.QUIT:
            running = False
            
        mouse_pos_x ,mouse_pos_y = pygame.mouse.get_pos()
        if mouse_pos_x >= p.rect.x and mouse_pos_x <=50:
            if mouse_pos_y >= p.rect.y and mouse_pos_y <= 50:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print "p1"

    #Update
    
    #Draw / render
    screen.fill(WHITE)
    p.update(screen)
    
    #Push the screen 
    pygame.display.flip()

pygame.quit()
