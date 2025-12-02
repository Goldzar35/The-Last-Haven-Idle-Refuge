import pygame

class FortificationMenu:
    def __init__(self, player, sidebar_width, window_width, window_height):
        '''Initialize Fortification Menu'''
        self.player = player
        self.margin = 30
        self.sidebar_width = sidebar_width  
        self.background = pygame.image.load("Assets/ChatGPT Image Dec 1, 2025, 09_56_25 PM.png").convert()

        # Fortification box dimensions
        self.box_width = int(0.50 * window_width)
        self.box_height = int(0.15 * window_height)
        self.box_x = self.sidebar_width + ((window_width - self.sidebar_width - self.box_width) // 2)
        self.box_y = window_height - self.box_height - self.margin
        self.button_font = pygame.font.Font(None, 25)
        self.button_text = "Fortify"

        self.fortification_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)

    def draw(self, screen):
        '''Draw the Fortification Menu elements on the screen'''
        screen.blit(self.background, (0, 0))

        pygame.draw.rect(screen, (100, 100, 100), self.fortification_box)
        text_surface = self.button_font.render(self.button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.fortification_box.center)
        screen.blit(text_surface, text_rect)
    
    def handle_fortification_event(self, event):
        '''Handle events for the fortification_box to toggle fortification'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = event.pos
            if self.fortification_box.collidepoint(mouse_x, mouse_y):
                print("Fortification box clicked! Toggling fortification.")
