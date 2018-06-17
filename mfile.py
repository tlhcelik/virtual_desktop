import pygame
from conf import *

class MFile(object):
    def __init__(self ,x ,y ,name ,screen):
        print "Folder Create"
        self.screen = screen
        self.name = name
        self.x = x
        self.y = y
        
        self.label = LABEL_FONT.render(self.name, 1, RED)
        screen.blit(self.label, (self.x-15, self.y+30))
        
        self.rect = pygame.rect.Rect((self.x, self.y, 30, 30))
        #self.rect.center = (20, 20)

        #print "x :{}, y: {}, bottomleft: {}, topright : {} ".format(self.rect.x,self.rect.y,self.rect.bottomleft[1], self.rect.topright[0])
    def move(self,x,y):
        self.x = x
        self.y = y
        self.rect.center =(x ,y)
        
    def update(self, surface, is_drag = False):
        if is_drag:
            self.mouse_pos_x ,self.mouse_pos_y = pygame.mouse.get_pos()
            self.move(self.mouse_pos_x ,self.mouse_pos_y)
            
        self.screen = surface
        pygame.draw.rect(self.screen, (0, 0, 128), self.rect)

    def get_pos_x(self):
        return self.rect.x

    def get_pos_y(self):
        return self.rect.x

    def get_pos_topright_x(self):
        return self.rect.topright[0]

    def get_pos_bottomright_y(self):
        return self.rect.bottomright[1]

    
'''
if self.mouse_pos_x >= self.rect.x and self.mouse_pos_x <= self.rect.topright[0]:
            if self.mouse_pos_y >= self.rect.y and self.mouse_pos_y <= self.rect.bottomleft[1]:
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    print "Left Click"

'''
