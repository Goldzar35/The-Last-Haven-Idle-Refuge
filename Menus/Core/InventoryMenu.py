import pygame

from Entities.Player import * 

class InventoryMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state):
        '''Initialize the Inventory Menu'''
        self.player = player
        self.sidebar_width = sidebar_width
        self.margin = 30
        self.game_state = game_state
        self.window_width = window_width
        self.window_height = window_height

    def draw(self, screen):
        '''Draw the Inventory Menu elements on the screen'''
        screen.fill((40, 40, 40)) 
        font = pygame.font.Font(None, 25)
        y = self.margin
        x = self.sidebar_width + 20
        col_width = 300
        screen_height = screen.get_height()
        # Temp inventory display logic
        for item, quantity in self.player.inventory.items():
            text = f"{item}: {quantity}"
            text_surf = font.render(text, True, (255, 255, 255))
            screen.blit(text_surf, (x, y))
            y += 30
            # Item list hits bottom of screen, move to next column
            if y + 30 > screen_height - self.margin:
                y = self.margin
                x += col_width

    def add_inventory(self, item, quantity):
        '''Add items to the player's inventory'''
        self.player.add_inventory(item, quantity)

    def remove_inventory(self, item, quantity):
        '''Remove items from the player's inventory'''
        self.player.remove_inventory(item, quantity)

    def remove_inventory_bulk(self, items_dict):
        '''Remove multiple items from the player's inventory'''
        self.player.remove_inventory_bulk(items_dict)