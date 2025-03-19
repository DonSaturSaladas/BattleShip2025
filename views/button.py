import pygame




class Button(pygame.sprite.Sprite):
    # x and y represent left and top
    
    def __init__(self, sprites, left, top, width, height, win ):
        super().__init__()
        
        self.screen = win
        self.sprites = sprites
        
        self.left = left 
        self.top = top
        
        self.relative_left = None
        self.relative_top = None
        
        
        self.width = width
        self.height = height
        self.image = sprites[0]
        
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
        
        self.screen.window.blit(self.image, (self.relative_left , self.relative_top))
        
    def get_rect(self):
        return self.rect
    
    def update(self,frame):
        self.image = self.sprites[frame]
        self.draw()
        
    def scale_img(self):
        
        self.rect = self.image.get_rect()  # Obtiene el rect de la surface
        self.rect.x = int(self.left)  # Establece la posición x
        self.rect.y = int(self.top)
        
        width = self.width * self.screen.scale_factor
        height = self.height * self.screen.scale_factor
        self.relative_left = (int) (self.left * self.screen.scale_factor)
        self.relative_top = (int) (self.top * self.screen.scale_factor)
        self.image = pygame.transform.scale(self.image,(width, height))
        
        self.rect = self.image.get_rect(topleft=(self.relative_left, self.relative_top))
    
        
    
        
        
    
        