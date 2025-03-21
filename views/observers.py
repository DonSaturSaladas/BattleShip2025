import pygame
from .spritesheet import spritesheet
from .view_constants import *


class Object_observer(pygame.sprite.Sprite):
    # x and y represent left and top
    
    def __init__(self, sprites, left, top, width, height, main_screen, father_surface ):
        super().__init__()
        
        self.father_surface = father_surface
        self.screen = main_screen
        self.sprites = sprites
        
        self.left = left 
        self.top = top
        
        self.relative_left = None
        self.relative_top = None
        
        
        self.width = width
        self.height = height
        self.image = sprites[0]
        
        # For object colissions and collidepoints
        
        self.rect = self.image.get_rect()  # Obtiene el rect de la surface
        self.rect.x = int(left)  # Establece la posición x
        self.rect.y = int(top)
        
        self.scale_img()
        
        
    def draw(self):
        self.scale_img()
        #print(self.image.get_rect().x)
        """print(f"Button position: ({self.relative_left}, {self.relative_top})")
        print(f"Button size: {self.image.get_size()}")
        print(f"Window size: {self.screen.window.get_size()}")"""
        
        self.father_surface.blit(self.image, (self.relative_left , self.relative_top))
        
    def get_rect(self):
        return self.rect
    
    def update(self,frame):
        self.image = self.sprites[frame]
        self.draw()
        
    def scale_img(self):
        
        self.rect = self.image.get_rect()  
        self.rect.x = int(self.left) 
        self.rect.y = int(self.top)
        
        width = self.width * self.screen.scale_factor
        height = self.height * self.screen.scale_factor
        self.relative_left = (int) (self.left * self.screen.scale_factor)
        self.relative_top = (int) (self.top * self.screen.scale_factor)
        self.image = pygame.transform.scale(self.image,(width, height)).convert_alpha()
        
        self.rect = self.image.get_rect(topleft=(self.relative_left, self.relative_top))
    
    def get_surface(self):
        return self.image
    
        
class Button_observer(Object_observer):
    
    def __init__(self, path, left, top, main_screen,father_surface, width = (2 * CELL_SIZE), height = (CELL_SIZE)):
        
        ss = spritesheet(path)
        sheet_width = int(ss.sheet.get_width())
        row_size = 345
        sheet_rows = (int) (sheet_width / row_size)
        sprites = []
        
        for i in range(sheet_rows):
            x = row_size * i
            sprites.append(ss.image_at((x, 0, 345, 208 )))
            
        
        
        super().__init__(sprites, left -(width/2), top, width, height, main_screen, father_surface)
    
        
    

class Background_observer(Object_observer):
    
    def __init__(self, path, main_screen, father_surface,row_heigth, width = BASE_SCREEN_WIDTH, height = BASE_SCREEN_HEIGHT, left = 0, top = 0):
        
        ss = spritesheet(path)
        sheet_width = int(ss.sheet.get_width())
        row_size = 1920
        sheet_rows = (int) (sheet_width / row_size)
        sprites = []
        
        for i in range(sheet_rows):
            x = row_size * i
            sprites.append(ss.image_at((x, 0, 1920, row_heigth )))
        
        super().__init__(sprites, left, top, width, height, main_screen, father_surface)


        