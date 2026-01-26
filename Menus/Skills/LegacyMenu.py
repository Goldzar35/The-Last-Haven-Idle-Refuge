import pygame

class LegacyMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state):
        '''Initialize Legacy Menu'''
        self.player = player
        self.sidebar_width = sidebar_width
        self.window_width = window_width
        self.window_height = window_height
        self.game_state = game_state
        self.margin = 30

    def draw(self, screen):
        '''Draw the Legacy Menu elements on the screen'''
        screen.fill((40, 40, 40))
        # Coming soon text
        font = pygame.font.Font(None, 130)
        text_surface = font.render("Coming Soon Legacy", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.left = self.sidebar_width + self.margin
        text_rect.centery = self.window_height // 2
        screen.blit(text_surface, text_rect)
