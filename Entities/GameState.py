import pygame

from Entities.Scavenging import Scavenging
from Entities.Foraging import Foraging
from Entities.Player import Player

class GameState:
    def __init__(self):
        '''Initialize the game state with default values'''
        self.player = Player()
        self.current_menu = 0
        self.scavenging = Scavenging(self.player)
        self.foraging = Foraging(self.player)

    def update_scavenging(self):
        '''Update the scavenging state if it's active'''
        if self.scavenging.is_scavenging:
            self.scavenging.scavenging()

    def update_foraging(self):
        '''Update the foraging state if it's active'''
        if hasattr(self, 'foraging') and self.foraging.is_foraging:
            self.foraging.foraging()

