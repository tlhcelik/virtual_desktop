import pygame

class MContextMenu(object):
    def __init__(self):
        pass
    def display_context_menu(self):
        print "Context Menu"
        
        self.new_screen = pygame.display.set_mode((50,100))
        
    def update(self):
        pygame.display.flip()
