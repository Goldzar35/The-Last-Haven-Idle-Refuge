import pygame

from Entities.Foraging import *

class ForagingMenu:
    def __init__(self, player, game_state, sidebar_width, window_width, window_height):
        '''Initialize Foraging Menu'''
        self.margin = 30
        self.sidebar_width = sidebar_width
        self.player = player
        self.game_state = game_state 
        self.sidebar_width = sidebar_width
        self.foraging = Foraging(player) 

        # Scavenging box dimensions
        self.box_x = self.sidebar_width + self.margin
        self.box_y = self.margin
        self.box_width = int(0.75 * window_width)
        self.box_height = int(0.4 * window_height)

        self.foraging_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)
    
    def draw(self, screen):
        '''Draw the Foraging Menu elements on the screen'''
        screen.fill((80, 80, 80))
        pygame.draw.rect(screen, (100, 100, 100), self.foraging_box)

    def handle_foraging_event(self, event,):
        '''Handle events for the foraging_box to toggle foraging'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = event.pos
            if self.foraging_box.collidepoint(mouse_x, mouse_y):
                if hasattr(self.game_state, "scavenging") and getattr(self.game_state.scavenging, "is_scavenging", False):
                    self.game_state.scavenging.is_scavenging = False
                    print("Stopped Scavenging to start Foraging")
                self.game_state.foraging.toggle_foraging()
