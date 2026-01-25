import pygame

from Entities.Scavenging import Scavenging
from Entities.Foraging import Foraging
from Entities.Hunting import Hunting
from Entities.Player import Player
from Entities.Fortification import Fortification

class GameState:
    def __init__(self):
        '''Initialize the game state with default values'''
        self.player = Player()
        self.current_menu = 0
        self.scavenging = Scavenging(self.player)
        self.foraging = Foraging(self.player)
        self.hunting = Hunting(self.player)
        self.fortification = Fortification(self.player)

    def update_scavenging(self):
        '''Update the scavenging state if it's active'''
        if self.scavenging.is_scavenging:
            self.scavenging.scavenging()

    def update_foraging(self):
        '''Update the foraging state if it's active'''
        if hasattr(self, 'foraging') and self.foraging.is_foraging:
            self.foraging.foraging()

    def update_hunting(self):
        '''Update the hunting state if it's active'''
        if hasattr(self, 'hunting') and self.hunting.is_hunting:
            self.hunting.hunting()

    # Exclusive starters: starting one stops the other
    def start_scavenging(self):
        '''Start scavenging and stop other activities'''
        self.foraging.is_foraging = False
        self.hunting.is_hunting = False
        self.scavenging.is_scavenging = True

    def start_foraging(self):
        '''Start foraging and stop other activities'''
        self.scavenging.is_scavenging = False
        self.hunting.is_hunting = False
        self.foraging.is_foraging = True

    def start_hunting(self):
        '''Start hunting and stop other activities'''
        self.scavenging.is_scavenging = False
        self.foraging.is_foraging = False
        self.hunting.is_hunting = True

    def stop_scavenging(self):
        '''Stop scavenging activity'''
        self.scavenging.is_scavenging = False

    def stop_foraging(self):
        '''Stop foraging activity'''
        self.foraging.is_foraging = False

    def stop_hunting(self):
        '''Stop hunting activity'''
        self.hunting.is_hunting = False

    
