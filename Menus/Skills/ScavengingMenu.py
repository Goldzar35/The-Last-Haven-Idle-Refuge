import pygame

# From Entities
from Entities.Scavenging import *


class ScavengingMenu:
    def __init__(self, player, game_state, sidebar_width, window_width, window_height):
        '''Initialize the Scavenging Menu'''
        self.margin = 30
        self.sidebar_width = sidebar_width
        self.player = player
        self.game_state = game_state 
        self.sidebar_width = sidebar_width
        self.scavenging = Scavenging(player)  

        # Scavenging box dimensions
        self.box_x = self.sidebar_width + self.margin
        self.box_y = self.margin
        self.box_width = int(0.75 * window_width)
        self.box_height = int(0.4 * window_height)

        self.scavenge_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)

    def draw(self, screen):
        '''Draw the Scavenging Menu elements on the screen'''
        screen.fill((70, 70, 70))
        pygame.draw.rect(screen, (100, 100, 100), self.scavenge_box)  
        
    def handle_scavenge_event(self, event,):
        '''Handle events for the scavenge_box to toggle scavenging'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = event.pos
            if self.scavenge_box.collidepoint(mouse_x, mouse_y):
                self.game_state.scavenging.toggle_scavenging()





