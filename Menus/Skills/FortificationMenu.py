import pygame

from Entities.Fortification import *

class FortificationMenu:
    def __init__(self, player, fortification, sidebar_width, window_width, window_height):
        '''Initialize Fortification Menu'''
        self.player = player
        self.fortification = fortification
        self.margin = 30
        self.sidebar_width = sidebar_width
        self.backgrounds = [
            pygame.image.load("Assets/Base_lvl_1.png").convert(),
            pygame.image.load("Assets/Base_lvl_2.png").convert(),
            pygame.image.load("Assets/Base_lvl_3.png").convert(),
            pygame.image.load("Assets/Base_lvl_4.png").convert(),
            pygame.image.load("Assets/Base_lvl_5.png").convert(),
            pygame.image.load("Assets/Base_lvl_6.png").convert()
        ]
        

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
        screen.fill((0, 0, 0))
        screen_width, screen_height = screen.get_size()

        # Get the current background from the list
        bg = self.backgrounds[self.fortification.background_index]
        bg_scaled = pygame.transform.smoothscale(bg, (screen_width, screen_height))
        screen.blit(bg_scaled, (0, 0))

        pygame.draw.rect(screen, (100, 100, 100), self.fortification_box)
        text_surface = self.button_font.render(self.button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.fortification_box.center)
        screen.blit(text_surface, text_rect)

    def handle_fortification_event(self, event):
        '''Handle events for the fortification_box to change background'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = event.pos
            if self.fortification_box.collidepoint(mouse_x, mouse_y):
                self.fortification.change_background(len(self.backgrounds))
                print("Fortification box clicked!")
