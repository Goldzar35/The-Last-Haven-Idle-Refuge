import pygame

from Entities.Player import * 

class InventoryMenu:
    def __init__(self, player, sidebar_width):
        '''Initialize the Inventory Menu'''
        self.player = player
        self.sidebar_width = sidebar_width
        self.margin = 30

    def draw(self, screen):
        '''Draw the Inventory Menu elements on the screen'''
        screen.fill((50, 50, 50)) 
        font = pygame.font.Font(None, 25)
        y = self.margin
        # Temp inventory display logic
        for item, quantity in self.player.inventory.items():
            text = f"{item}: {quantity}"
            text_surf = font.render(text, True, (255, 255, 255))
            screen.blit(text_surf, (self.sidebar_width + 20, y))
            y += 30

    def add_inventory(self, item, quantity):
        '''Add items to the player's inventory'''
        self.player.add_inventory(item, quantity)

    def remove_inventory(self, item, quantity):
        '''Remove items from the player's inventory'''
        self.player.remove_from_inventory(item, quantity)