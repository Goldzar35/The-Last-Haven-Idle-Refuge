import pygame


class InventoryMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state):
        '''Initialize the Inventory Menu'''
        self.player = player
        self.sidebar_width = sidebar_width
        self.margin = 30
        self.game_state = game_state
        self.font = pygame.font.Font(None, 25)

    def draw(self, screen):
        '''Draw the Inventory Menu elements on the screen'''
        screen.fill((40, 40, 40))
        y = self.margin
        x = self.sidebar_width + 20
        col_width = 300
        screen_height = screen.get_height()
        for item, quantity in self.player.inventory.items():
            text_surf = self.font.render(f"{item}: {quantity}", True, (255, 255, 255))
            screen.blit(text_surf, (x, y))
            y += 30
            if y + 30 > screen_height - self.margin:
                y = self.margin
                x += col_width
