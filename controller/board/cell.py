import pygame


class Cell:
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.observer = None
        self.actualSprite = sprites[0]
        
        self.sprites = sprites
        self.hidden = False
        self.hasShip = False
        
    def registerObserver(self, observer):
        self.observer = observer
    
    def update(self):
        self.observer.update();
        
    def selected(self):
        if(self.hidden):
            self.hidden = False
            self.update()
            if(self.hasShip):
                self.sprite = self.sprites[2]

            
            
    
    
