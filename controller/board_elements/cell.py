import pygame


class Cell:
    
    '''Represents the cells of the board it can contain a ship or water,
       its internal status changes depending on whearever the player or the opponent clicks on the cell,
       The observer is in charge of printing and updating visually the object and his status
       it haves a coleccion of spirtes used to represent visualy the satus of the cell'''
       
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.observer = None
        self.sprites = sprites
        self.actualSprite = sprites[0]

        
        self.hidden = False
        self.hasShip = False

    def registerObserver(self, observer):
        self.observer = observer

    def update(self, left, top):
        ''''Arguments : left, top: especify the screen position of the board to print the observers 
            in the screen'''
        self.observer.update(left +1, top)

    def selected(self):
        if self.hidden:
            self.hidden = False
            self.update()
            if self.hasShip:
                self.sprite = self.sprites[2]
            
    def changeSprite(self, sprite):
        self.actualSprite = sprite
        
