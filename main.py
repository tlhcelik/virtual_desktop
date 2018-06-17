import pygame
import os
import sys

from mfile import * # my file class file :)
from conf import * # my config file
        
pygame.init()
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("Virtual Desktop")
clock = pygame.time.Clock()

file_list = []
x = 20
y = 20

for i in range(5):
    file_list.append(MFile(x, y)) 
    y += 50
    
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
        for p in file_list:
            if mouse_pos_x >= p.rect.x and mouse_pos_x <= p.rect.topright[0]:
                if mouse_pos_y >= p.rect.y and mouse_pos_y <= p.rect.bottomright[1]:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print file_list.index(p)
                        
                    
    #Update
    
    #Draw / render
    screen.fill(WHITE)
    p.update(screen ,is_drag = False)
    for i in file_list:
        i.update(screen)
    
    #Push the screen 
    pygame.display.flip()

pygame.quit()
