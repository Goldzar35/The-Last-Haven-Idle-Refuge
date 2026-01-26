import pygame

class ShopMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state, scavenging_menu, foraging_menu, hunting_menu):
        '''Initialize the Shop Menu'''
        self.margin = 30
        self.player = player
        self.sidebar_width = sidebar_width
        self.window_width = window_width
        self.window_height = window_height
        self.game_state = game_state
        self.scavenging_menu = scavenging_menu
        self.foraging_menu = foraging_menu
        self.hunting_menu = hunting_menu

        # Shop button 1 box dimensions
        self.box_x_1 = self.sidebar_width + self.margin
        self.box_y_1 = self.margin
        self.box_width_1 = int(0.30 * window_width)
        self.box_height_1 = int(0.4 * window_height)

        self.shop_button_1 = pygame.Rect(self.box_x_1, self.box_y_1, self.box_width_1, self.box_height_1)

        # Button for shop button 1 delay
        self.shop_button_1_rect = pygame.Rect(self.box_x_1 + 50, self.box_y_1 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.shop_button_1_text = "Test1"

        # Shop button 2 box dimensions
        self.box_x_2 = self.sidebar_width + self.margin + self.box_width_1 + self.margin
        self.box_y_2 = self.margin
        self.box_width_2 = int(0.30 * window_width)
        self.box_height_2 = int(0.4 * window_height)

        self.shop_button_2 = pygame.Rect(self.box_x_2, self.box_y_2, self.box_width_2, self.box_height_2)

        # Button for shop button 2 delay
        self.shop_button_2_rect = pygame.Rect(self.box_x_2 + 50, self.box_y_2 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.shop_button_2_text = "Test2"

    def draw(self, screen):
        '''Draw the Shop Menu elements on the screen'''
        screen.fill((60, 60, 60)) 
        pygame.draw.rect(screen, (90, 90, 90), self.shop_button_1)
        shop_button_1_text_surface = self.font.render(self.shop_button_1_text, True, (255, 255, 255))
        shop_button_1_text_rect = shop_button_1_text_surface.get_rect(center=self.shop_button_1.center)
        screen.blit(shop_button_1_text_surface, shop_button_1_text_rect)
        pygame.draw.rect(screen, (90, 90, 90), self.shop_button_2)
        shop_button_2_text_surface = self.font.render(self.shop_button_2_text, True, (255, 255, 255))
        shop_button_2_text_rect = shop_button_2_text_surface.get_rect(center=self.shop_button_2.center)
        screen.blit(shop_button_2_text_surface, shop_button_2_text_rect)
