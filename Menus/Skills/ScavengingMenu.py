import pygame

from Entities.Scavenging import *


class ScavengingMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state):
        '''Initialize the Scavenging Menu'''
        self.margin = 30
        self.sidebar_width = sidebar_width
        self.player = player
        self.game_state = game_state 
        self.pending_scavenge = False
        self.scavenge_start_time = 0
        self.scavenge_delay = 3000  

        # Scavenging box dimensions
        self.box_x = self.sidebar_width + self.margin
        self.box_y = self.margin
        self.box_width = int(0.75 * window_width)
        self.box_height = int(0.4 * window_height)

        self.scavenge_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)

    def draw(self, screen):
        '''Draw the Scavenging Menu elements on the screen'''
        screen.fill((40, 40, 40))
        pygame.draw.rect(screen, (100, 100, 100), self.scavenge_box)  
        
    def handle_scavenge_event(self, event,):
        '''Handle events for the scavenge_box to toggle scavenging'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = event.pos
            if self.scavenge_box.collidepoint(mouse_x, mouse_y):
                if hasattr(self.game_state, "foraging") and getattr(self.game_state.foraging, "is_foraging", False):
                    self.game_state.foraging.is_foraging = False
                    print("Stopped Foraging to start Scavenging")
                if hasattr(self.game_state, "hunting") and getattr(self.game_state.hunting, "is_hunting", False):
                    self.game_state.hunting.is_hunting = False
                    print("Stopped Hunting to start Scavenging")
                self.pending_scavenge = True
                self.scavenge_start_time = pygame.time.get_ticks()
                if not self.game_state.scavenging.is_scavenging:
                    print("Scavenging will start after delay!")
                else:
                    print("Scavenging will end after delay!")

    def update(self):
        '''Check if delay has passed and start scavenging'''
        if hasattr(self, "pending_scavenge") and self.pending_scavenge:
            now = pygame.time.get_ticks()
            # self.scavenge_delay is in seconds, pygame.time.get_ticks() is in ms
            if now - self.scavenge_start_time >= getattr(self, "scavenge_delay", 1000):
                self.pending_scavenge = False
                self.game_state.scavenging.toggle_scavenging()
                if self.game_state.scavenging.is_scavenging:
                    print("Scavenging started after delay!")
                else:
                    print("Scavenging ended after delay!")





