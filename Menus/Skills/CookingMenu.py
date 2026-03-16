import pygame


class CookingMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state):
        '''Initialize Cooking Menu'''
        self.player = player
        self.sidebar_width = sidebar_width
        self.window_width = window_width
        self.window_height = window_height
        self.game_state = game_state
        self.margin = 30
        self.font = pygame.font.Font(None, 130)

    def draw(self, screen):
        '''Draw the Cooking Menu elements on the screen'''
        screen.fill((40, 40, 40))
        text_surface = self.font.render("Coming Soon Cooking", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.left = self.sidebar_width + self.margin
        text_rect.centery = self.window_height // 2
        screen.blit(text_surface, text_rect)
