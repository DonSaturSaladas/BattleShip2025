
from .view_constants import *

from .spritesheet import spritesheet
from .observers import Object_observer, Background_observer, Button_observer
class Menu_screen:
    
    def __init__(self, window, main_screen):
        self.window = window
        self.main_screen = main_screen
        self.menu_surface = pygame.Surface((BASE_SCREEN_WIDTH, BASE_SCREEN_HEIGHT), pygame.SRCALPHA).convert_alpha()
        self.scaled_cell_size = main_screen.scaled_cell_size
        self.buttons = []
        self.backgrounds = []
        self.objects_group = pygame.sprite.Group()
        self.setup_screen_objects()
              
        self.current_frame = 0
        self.animation_speed = 40
        self.last_update = pygame.time.get_ticks()
        self.wait_time = 2000 # 5 seconds(mili) de espera
        self.wait_start = 0 # Cuando comenzo la espera 
        self.animation_finished = False # Si esta esperando
    
    
    def setup_screen_objects(self):
        self.create_background_image()
        self.create_background_logo_image()  
        self.create_start_button()
        self.draw_background_image()
        
        
                
    def run(self):
        self.menu_surface.fill((0,0,0,0))
    
        
        
        if (self.animation_finished or self.main_screen.first_iteration ):
            self.draw_background_image()
        
        self.draw_buttons()
        self.animate_logo_background()
        
        
        self.window.blit(self.menu_surface, (0,0))
        pygame.display.flip()
        
        # Draw background image
        # Draw Buttons:
            # Start
            # Exit
            # Skins?
            # Options?
        
        
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_clicked(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.mouse_released(event)

    
    def mouse_clicked(self, event):
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
    
        self.handle_acept_button_clicked(mouse_x, mouse_y)
        
    def mouse_released(self, event):
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        
        self.handle_acept_button_released(mouse_x, mouse_y)
        
    
    
    def handle_acept_button_clicked(self, mouse_x, mouse_y):
        if self.buttons[0].get_rect().collidepoint(mouse_x, mouse_y): #If click acept button
            self.buttons[0].update(1)
            
    def handle_acept_button_released(self, mouse_x, mouse_y):
        if self.buttons[0].get_rect().collidepoint(mouse_x, mouse_y):
            self.buttons[0].update(0)
            
            self.main_screen.change_screen("Setup")
            
    
    
   
        
        
            
            

    def screen_size_changed(self): 
        width = BASE_SCREEN_WIDTH * self.main_screen.scale_factor
        height = BASE_SCREEN_HEIGHT *self.main_screen.scale_factor
        self.menu_surface = pygame.transform.scale(self.menu_surface,(width, height)).convert_alpha()
        
        #TODO: Actualizar los valores de father_surface de todas las superficies de la pantalla por el nuevo menu_surface 
    
    def animate_logo_background(self):
        
        
        background = self.backgrounds[1]
        current_time = pygame.time.get_ticks()
        total_frames = len(background.sprites)        
        if self.animation_finished:
            if current_time - self.wait_start >= self.wait_time:
                self.animation_finished = False
                self.wait_start = 0
            background.update(0)
            return
        
        if current_time - self.last_update  >self.animation_speed:
            self.last_update = current_time
            self.current_frame = (self.current_frame + 1) % total_frames
            
            if self.current_frame == 0:
                self.animation_finished = True
                self.wait_start = current_time
            
            background.update(self.current_frame) 
            
        
    
    def create_background_logo_image(self):
        height = BASE_SCREEN_HEIGHT* self.main_screen.scale_factor - 300
            
        background = Background_observer(MENU_BACKGROUND_LOGO_SPRITESHEET_PATH,self.main_screen,self.menu_surface,600, height = height)
        print(f"Has alpha: {background.sprites[0].get_alpha() is not None}")
        self.backgrounds.append(background)
        
        
    
    def create_background_image(self):
        height = BASE_SCREEN_HEIGHT * self.main_screen.scale_factor 
        
        background = Background_observer(MENU_BACKGROUND_IMAGE_PATH,self.main_screen,self.menu_surface,1080, height = height)
        self.backgrounds.append(background)
        
        
    
    def create_buttons(self):
        self.create_start_button()
        # create_exit_button()
        # create_options_button()
        # create_sound_slider_button()
    
    def draw_buttons(self):
        self.draw_start_button()
        self.draw_exit_button()
        # draw_options_button()
        # draw_sound_slider_button()
        
    def draw_start_button(self):
        self.buttons[0].draw()

        
    
    def create_start_button(self):
        
        width = (2 * CELL_SIZE)*2
        height = (CELL_SIZE)*2
        
        x = (BASE_SCREEN_WIDTH * self.main_screen.scale_factor / 2) 
        y = (BASE_SCREEN_HEIGHT * self.main_screen.scale_factor - 150) 
        
    
        button = Button_observer(ACCEPT_BUTTON_SPRITESHEET_PATH, x, y,self.main_screen, self.menu_surface, width= width, height= height)
        
        self.buttons.append(button)
        
        
        
    def draw_background_image(self):
        self.backgrounds[0].update(0)
        
        
  
    
        
        
        
    
    
    