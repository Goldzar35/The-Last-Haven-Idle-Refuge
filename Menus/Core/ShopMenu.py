import pygame

from Entities.Player import *

class ShopMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state, scavenge_tick, forage_tick, hunting_tick):
        '''Initialize the Shop Menu'''
        self.margin = 30
        self.player = player
        self.sidebar_width = sidebar_width
        self.window_width = window_width
        self.window_height = window_height
        self.game_state = game_state
        self.scavenge_tick = scavenge_tick
        self.forage_tick = forage_tick
        self.hunting_tick = hunting_tick

        # Shop button 1 box dimensions
        self.box_x_1 = self.sidebar_width + self.margin
        self.box_y_1 = self.margin
        self.box_width_1 = int(0.37 * window_width)
        self.box_height_1 = int(0.4 * window_height)

        self.shop_button_1 = pygame.Rect(self.box_x_1, self.box_y_1, self.box_width_1, self.box_height_1)

        # Button for shop button 1 text
        self.shop_button_1_rect = pygame.Rect(self.box_x_1 + 50, self.box_y_1 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.shop_button_1_text = "Test1"

        # Shop button 2 box dimensions
        self.box_x_2 = self.sidebar_width + self.margin + self.box_width_1 + self.margin
        self.box_y_2 = self.margin
        self.box_width_2 = int(0.37 * window_width)
        self.box_height_2 = int(0.4 * window_height)

        self.shop_button_2 = pygame.Rect(self.box_x_2, self.box_y_2, self.box_width_2, self.box_height_2)

        # Button for shop button 2 text
        self.shop_button_2_rect = pygame.Rect(self.box_x_2 + 50, self.box_y_2 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.shop_button_2_text = "Test2"

        # Shop button 3 box dimensions
        self.box_x_3 = self.sidebar_width + self.margin
        self.box_y_3 = self.margin + self.box_height_1 + self.margin
        self.box_width_3 = int(0.37 * window_width)
        self.box_height_3 = int(0.4 * window_height)

        self.shop_button_3 = pygame.Rect(self.box_x_3, self.box_y_3, self.box_width_3, self.box_height_3)

        # Button for shop button 3 text
        self.shop_button_3_rect = pygame.Rect(self.box_x_3 + 50, self.box_y_3 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.shop_button_3_text = "Test3"

        # Shop button 4 box dimensions
        self.box_x_4 = self.sidebar_width + self.margin + self.box_width_3 + self.margin
        self.box_y_4 = self.margin + self.box_height_2 + self.margin
        self.box_width_4 = int(0.37 * window_width)
        self.box_height_4 = int(0.4 * window_height)

        self.shop_button_4 = pygame.Rect(self.box_x_4, self.box_y_4, self.box_width_4, self.box_height_4)

        # Button for shop button 4 text
        self.shop_button_4_rect = pygame.Rect(self.box_x_4 + 50, self.box_y_4 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.shop_button_4_text = "Test4"

    def draw(self, screen):
        '''Draw the Shop Menu elements on the screen'''
        screen.fill((40, 40, 40)) 
        pygame.draw.rect(screen, (90, 90, 90), self.shop_button_1)
        shop_button_1_text_surface = self.font.render(self.shop_button_1_text, True, (255, 255, 255))
        shop_button_1_text_rect = shop_button_1_text_surface.get_rect(center=self.shop_button_1.center)
        screen.blit(shop_button_1_text_surface, shop_button_1_text_rect)
        pygame.draw.rect(screen, (90, 90, 90), self.shop_button_2)
        shop_button_2_text_surface = self.font.render(self.shop_button_2_text, True, (255, 255, 255))
        shop_button_2_text_rect = shop_button_2_text_surface.get_rect(center=self.shop_button_2.center)
        screen.blit(shop_button_2_text_surface, shop_button_2_text_rect)
        pygame.draw.rect(screen, (90, 90, 90), self.shop_button_3)
        shop_button_3_text_surface = self.font.render(self.shop_button_3_text, True, (255, 255, 255))
        shop_button_3_text_rect = shop_button_3_text_surface.get_rect(center=self.shop_button_3.center)
        screen.blit(shop_button_3_text_surface, shop_button_3_text_rect)
        pygame.draw.rect(screen, (90, 90, 90), self.shop_button_4)
        shop_button_4_text_surface = self.font.render(self.shop_button_4_text, True, (255, 255, 255))
        shop_button_4_text_rect = shop_button_4_text_surface.get_rect(center=self.shop_button_4.center)
        screen.blit(shop_button_4_text_surface, shop_button_4_text_rect)

    def handle_shop_button_1_event(self, event):
        '''Handle events for shop_button_1 to perform an action, this button will reduce the scavenge tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_1.collidepoint(mouse_x, mouse_y):
                if self.player.scavenge_tick > 0.1:
                    self.player.scavenge_tick = max(0.1, round(self.player.scavenge_tick - 0.1, 2))
                    print("Shop Button 1 clicked!")
                    print("New scavenge tick:", self.player.scavenge_tick)
                else:
                    print("Scavenge tick maxed")

    def handle_shop_button_2_event(self, event):
        '''Handle events for shop_button_2 to perform an action, this button will reduce the forage tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_2.collidepoint(mouse_x, mouse_y):
                if self.player.forage_tick > 0.1:
                    self.player.forage_tick = max(0.1, round(self.player.forage_tick - 0.1, 2))
                    print("Shop Button 2 clicked!")
                    print("New forage tick:", self.player.forage_tick)
                else:
                    print("Forage tick maxed")

    def handle_shop_button_3_event(self, event):
        '''Handle events for shop_button_3 to perform an action, this button will reduce the hunting tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_3.collidepoint(mouse_x, mouse_y):
                if self.player.hunting_tick > 0.1:
                    self.player.hunting_tick = max(0.1, round(self.player.hunting_tick - 0.1, 2))
                    print("Shop Button 3 clicked!")
                    print("New hunting tick:", self.player.hunting_tick)
                else:
                    print("Hunting tick maxed")

    def handle_shop_button_4_event(self, event):
        '''Handle events for shop_button_4 to perform an action'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_4.collidepoint(mouse_x, mouse_y):
                print("Shop Button 4 clicked!")
