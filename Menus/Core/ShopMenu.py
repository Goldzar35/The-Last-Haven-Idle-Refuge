import pygame

class ShopMenu:
    def __init__(self, player, sidebar_width, window_width, window_height):
        '''Initialize the Shop Menu'''
        self.player = player
        self.sidebar_width = sidebar_width
        self.window_width = window_width
        self.window_height = window_height

    def draw(self, screen):
        '''Draw the Shop Menu elements on the screen'''
        screen.fill((60, 60, 60)) 
