import pygame

from Entities.Hunting import *

class HuntingMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state):
        '''Initialize Hunting Menu'''
        self.margin = 30
        self.sidebar_width = sidebar_width
        self.player = player
        self.game_state = game_state 
        self.pending_hunt = False
        self.hunt_start_time = 0
        self.hunt_delay = 3000

        # Scavenging box dimensions
        self.box_x = self.sidebar_width + self.margin
        self.box_y = self.margin
        self.box_width = int(0.75 * window_width)
        self.box_height = int(0.4 * window_height)

        self.hunting_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)
    
    def draw(self, screen):
        '''Draw the Hunting Menu elements on the screen'''
        screen.fill((90, 90, 90))
        pygame.draw.rect(screen, (100, 100, 100), self.hunting_box)

    def handle_hunting_event(self, event):
        '''Handle events for the hunting_box to toggle hunting'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = event.pos
            if self.hunting_box.collidepoint(mouse_x, mouse_y):
                if hasattr(self.game_state, "scavenging") and getattr(self.game_state.scavenging, "is_scavenging", False):
                    self.game_state.scavenging.is_scavenging = False
                    print("Stopped Scavenging to start Hunting")
                if hasattr(self.game_state, "foraging") and getattr(self.game_state.foraging, "is_foraging", False):
                    self.game_state.foraging.is_foraging = False
                    print("Stopped Foraging to start Hunting")
                self.pending_hunt = True
                self.hunt_start_time = pygame.time.get_ticks()
                if not self.game_state.hunting.is_hunting:
                    print("Hunting will start after delay!")
                else:
                    print("Hunting will end after delay!")

    def update(self):
        '''Check if delay has passed and start hunting'''
        if hasattr(self, "pending_hunt") and self.pending_hunt:
            now = pygame.time.get_ticks()
            # self.hunt_delay is in seconds, pygame.time.get_ticks() is in ms
            if now - self.hunt_start_time >= getattr(self, "hunt_delay", 1000):
                self.pending_hunt = False
                self.game_state.hunting.toggle_hunting()
                if self.game_state.hunting.is_hunting:
                    print("Hunting started after delay!")
                else:
                    print("Hunting ended after delay!")
