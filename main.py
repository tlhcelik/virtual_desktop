import pygame
import os
import sys
import time

from mfile import * # my file class file :)
from conf import * # my config file
from desktop import * #get desktop elements class
from context_menu import MContextMenu

screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption("Virtual Desktop")
clock = pygame.time.Clock()

desk = Desktop()

current_file_name_list = []
file_list = []

def get_files(path = "."):
    x = 20
    y = 20
    for root, dirs, files in os.walk(".", topdown=True):
       for name in files:
          current_file_name_list.append(os.path.join(root, name))
       for name in dirs:
          current_file_name_list.append(os.path.join(root, name))

    print current_file_name_list

    for i in range(len(current_file_name_list)): # create sizeof current_file_name_list file object
        file_list.append(MFile(x, y ,current_file_name_list[i] ,screen))
        y += 50
        if y >= HEIGHT - 50:
            y = 20
            x += 112
    

def __loop__():
    context_menu = MContextMenu()
    running = True
    while running:
        # screen speed
        clock.tick(FPS)

        #Process input
        pressed = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
     
        if pressed[pygame.K_ESCAPE]:
            running = False
            
        for event in pygame.event.get():
            #chech for closing the window
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                print "rigt mouse clicked"
                context_menu.display_context_menu()
                
            mouse_pos_x ,mouse_pos_y = pygame.mouse.get_pos() # click event create
            for p in file_list:
                if mouse_pos_x >= p.rect.x and mouse_pos_x <= p.rect.topright[0]:
                    if mouse_pos_y >= p.rect.y and mouse_pos_y <= p.rect.bottomright[1]:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            print current_file_name_list[file_list.index(p)]

        #Update
        context_menu.update()                    
        for i in file_list:
            i.update(screen)
        
        #Push the screen 
        pygame.display.flip()
        
    pygame.quit()
    
if __name__=="__main__":
    get_files()
    __loop__()
