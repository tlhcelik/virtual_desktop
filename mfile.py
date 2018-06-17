import pygame

class MFile(object):
    def __init__(self):
        print "Folder Create"
        self.rect = pygame.rect.Rect((20, 20, 30, 30))
        #self.rect.center = (20, 20)

        #print "x :{}, y: {}, bottomleft: {}, topright : {} ".format(self.rect.x,self.rect.y,self.rect.bottomleft[1], self.rect.topright[0])
    
    def update(self, surface):
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
