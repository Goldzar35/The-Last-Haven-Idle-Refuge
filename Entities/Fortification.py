import pygame

class Fortification:
    def __init__(self, player):
        self.player = player
        self.background_index = 0  # Start with the first background

    def change_background(self, backgrounds):
        self.background_index = (self.background_index + 1) % backgrounds