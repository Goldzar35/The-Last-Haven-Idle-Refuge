import pygame

class Fortification:
    def __init__(self, player):
        self.player = player
        self.use_alternate_background = False

    def change_background(self):
        self.use_alternate_background = not self.use_alternate_background