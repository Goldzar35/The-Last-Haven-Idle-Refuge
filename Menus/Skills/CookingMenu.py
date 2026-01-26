import pygame

class CookingMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state):
        '''Initialize Cooking Menu'''
        self.player = player
        self.sidebar_width = sidebar_width
        self.window_width = window_width
        self.window_height = window_height
        self.game_state = game_state

    def draw(self, screen):
        '''Draw the Cooking Menu elements on the screen'''
        screen.fill((40, 40, 40))
        # Coming soon text
        font = pygame.font.Font(None, 200)
        text_surface = font.render("Coming Soon", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.window_width // 2, self.window_height // 2))
        screen.blit(text_surface, text_rect)
