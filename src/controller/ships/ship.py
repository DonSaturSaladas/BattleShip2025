from abc import ABC, abstractmethod
from controller.board_elements.cell import Cell
from controller.factories.sprite import Sprite
from views.view_constants import *
from views.spritesheet import spritesheet

class Ship():
    
    def __init__(self, cells): 
        self.parts: list[Cell]  = cells
        self.status = "hidden"
        self.sunked = False
        self.init_ship_parts()
        self.hits = 0
        
        
    def init_ship_parts(self):
        ss = spritesheet(HITTED_SHIP_SPRITESHEET_PATH)
        sheet_width = int(ss.sheet.get_width())
        row_size = 16
        sheet_rows = (int) (sheet_width / row_size)
        sprites = []
        
        for i in range(sheet_rows):
            x = row_size * i
            sprites.append(ss.image_at((x, 0, 16, 16 )))

        #Cambiar skin de cada celda del barco
        for cell in self.parts:
            cell.hasShip = True
            cell.observer.add_sprite("Hitted", sprites)
        
        #Impementar sprites para cuando el barco este hundido
        
        self.init_ship_sprite(SHIP_TEST_PATH, 612, 612)
        
        # Implement The specific sprite for each class (Testing abstrac method)
    
    
    def init_ship_sprite(self, path, width, height):
        ss = spritesheet(path)
        sheet_width = int(ss.sheet.get_width())
        row_size = width
        sheet_rows = (int) (sheet_width / row_size)
        sprites = []
        
        for i in range(sheet_rows):
            x = row_size * i
            frame = ss.image_at((x, 0, width, height ))
            if self.get_orientation() == "V":
                frame = pygame.transform.rotate(frame, 270)
                
            sprites.append([frame])
        
        i = 0
        for cell in self.parts:
            cell.observer.add_sprite("Ship", sprites[i])
            if(len(sprites) > 1):
                i += 1
    
    
    def show_cells(self):
        for cell in self.parts:
            cell.observer.update(key = "Ship")
            
            
    def has_cell(self, cell):
        return cell in self.parts 

    def hit(self, cell):
        self.hits += 1
        if self.hits == len(self.parts):
            self.sunked = True
            print(f'Size {len(self.parts)} sunked')
            
    def get_length(self):
        return len(self.parts)
    
    def get_orientation(self):
        return "H" if self.parts[-1].y == self.parts[-2].y else "V"