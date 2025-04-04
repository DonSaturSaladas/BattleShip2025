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
    
    def set_father_surface(self, surface):
        self.father_surface = surface
    
        
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



class Cell_Observer(Object_observer):
    
    def __init__(self,main_screen,cell):
        self.win = main_screen
        self.cell = cell

        
        
        
        ss_water = spritesheet(WATER_PATH)
        water_sprite = []
        water_sprite.append(ss_water.image_at((0,0,1216,1216)))
        
        ss_water_hitted = spritesheet(WATER_HITTED_PATH)
        water_hitted_sprite = []
        water_hitted_sprite.append(ss_water_hitted.image_at((0,0,1216,1216)))
        
        
        
        
        
        # Todo elemento del diccionario debera de ser un arreglo independientemente de si solamente contiene una imagen 
        self.sprites_dict = {"Water": water_sprite, 
                   "Ship" : None,
                   "Hitted" : water_hitted_sprite}
        
        
        self.current_sprite = self.sprites_dict.get("Water")
        
        self.animation_interval = 50  # milisegundos entre frames (ajusta según necesidad)
        self.animation_last_time = pygame.time.get_ticks()
        self.animation_frame_index = 0
        
        
        super().__init__(self.sprites_dict["Water"], 0, 0, CELL_SIZE -3 , CELL_SIZE -1, main_screen, main_screen.window)
        
        self.relative_left = self.cell.x
        self.relative_top = self.cell.y
        
        self.calcPos()
        
        self.image = self.current_sprite[0]

    def set_pos(self, left, top):
        self.left = left +3 
        self.top = top

    def add_sprite(self, key, sprite):
        self.sprites_dict[key] =  sprite

    def calcPos(self):
        self.relative_left = self.win.scaled_cell_size * self.cell.x + self.left
        self.relative_top = self.win.scaled_cell_size * self.cell.y + self.top 
    
    def scale_img(self):
            
            self.rect = self.image.get_rect()  
            self.rect.x = int(self.left) 
            self.rect.y = int(self.top)
            
            width = self.width * self.screen.scale_factor
            height = self.height * self.screen.scale_factor
            self.relative_left = self.win.scaled_cell_size * self.cell.x + self.left
            self.relative_top = self.win.scaled_cell_size * self.cell.y + self.top 
            self.image = pygame.transform.scale(self.image,(width, height)).convert_alpha()
            
            self.rect = self.image.get_rect(topleft=(self.relative_left, self.relative_top))
            
        
    def update(self,key = None):
        if key is not None:
            self.current_sprite = self.sprites_dict.get(key)
            self.image = self.current_sprite[0]
        
        if len(self.current_sprite) > 1 :
            self.animate_sprite()
            
        self.draw()
        
    def animate_sprite(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_last_time > self.animation_interval:
            self.animation_frame_index = (self.animation_frame_index + 1) % len(self.sprites_dict["Hitted"])
            self.animation_last_time = current_time
        self.image = self.sprites_dict["Hitted"][self.animation_frame_index]