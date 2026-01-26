import pygame


class EngineeringMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state, scavenging_menu, foraging_menu, hunting_menu):
        '''Initialize Engineering Menu'''
        self.player = player
        self.game_state = game_state
        self.sidebar_width = sidebar_width
        self.margin = 30
        self.scavenging_menu = scavenging_menu
        self.foraging_menu = foraging_menu
        self.hunting_menu = hunting_menu

        # Engineering scavenging box dimensions
        self.box_x_1 = self.sidebar_width + self.margin
        self.box_y_1 = self.margin
        self.box_width_1 = int(0.75 * window_width)
        self.box_height_1 = int(0.2 * window_height)

        self.engineering_scavenging_box = pygame.Rect(self.box_x_1, self.box_y_1, self.box_width_1, self.box_height_1)

        # Button for reducing scavenging delay
        self.button_rect = pygame.Rect(self.box_x_1 + 50, self.box_y_1 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.button_text = "Reduce Scavenge Delay"

        # Engineering foraging box dimensions
        self.box_x_2 = self.sidebar_width + self.margin
        self.box_y_2 = self.box_y_1 + self.box_height_1 
        self.box_width_2 = int(0.75 * window_width)
        self.box_height_2 = int(0.2 * window_height)

        self.engineering_foraging_box = pygame.Rect(self.box_x_2, self.box_y_2, self.box_width_2, self.box_height_2)

        # Button for reducing foraging delay
        self.foraging_button_rect = pygame.Rect(self.box_x_2 + 50, self.box_y_2 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.foraging_button_text = "Reduce Forage Delay"

        # Engineering hunting box dimensions
        self.box_x_3 = self.sidebar_width + self.margin
        self.box_y_3 = self.box_y_2 + self.box_height_2
        self.box_width_3 = int(0.75 * window_width)
        self.box_height_3 = int(0.2 * window_height)

        self.engineering_hunting_box = pygame.Rect(self.box_x_3, self.box_y_3, self.box_width_3, self.box_height_3)

        # Button for reducing hunting delay
        self.hunting_button_rect = pygame.Rect(self.box_x_3 + 50, self.box_y_3 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.hunting_button_text = "Reduce Hunt Delay"

    def draw(self, screen):
        '''Draw the Engineering Menu elements on the screen'''
        screen.fill((40, 40, 40)) 
        pygame.draw.rect(screen, (120, 120, 120), self.engineering_scavenging_box)
        pygame.draw.rect(screen, (150, 150, 150), self.engineering_foraging_box)
        pygame.draw.rect(screen, (180, 180, 180), self.engineering_hunting_box)
        # Engineering scavenging button
        pygame.draw.rect(screen, (120, 120, 120), self.button_rect)
        scavenge_text_surface = self.font.render(self.button_text, True, (255, 255, 255))
        scavenge_text_rect = scavenge_text_surface.get_rect(center=self.button_rect.center)
        screen.blit(scavenge_text_surface, scavenge_text_rect)
        # Engineering foraging button
        pygame.draw.rect(screen, (150, 150, 150), self.foraging_button_rect)
        forage_text_surface = self.font.render(self.foraging_button_text, True, (255, 255, 255))
        forage_text_rect = forage_text_surface.get_rect(center=self.foraging_button_rect.center)
        screen.blit(forage_text_surface, forage_text_rect)
        # Engineering hunting button
        pygame.draw.rect(screen, (180, 180, 180), self.hunting_button_rect)
        hunting_text_surface = self.font.render(self.hunting_button_text, True, (255, 255, 255))
        hunting_text_rect = hunting_text_surface.get_rect(center=self.hunting_button_rect.center)
        screen.blit(hunting_text_surface, hunting_text_rect)

    def handle_engineering_scavenging_event(self, event):
        '''Handle events for the engineering scavenging box'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = event.pos
            if self.engineering_scavenging_box.collidepoint(mouse_x, mouse_y):
                if self.player.inventory.get("Cement", 0) >= 1:
                    self.player.inventory["Cement"] -= 1
                    old_time = self.scavenging_menu.scavenge_delay
                    self.scavenging_menu.scavenge_delay = max(500, old_time - 500)
                    print(f"Used 1 Cement to purchase upgrade")
                    print(f"Scavenging start delay reduced to {self.scavenging_menu.scavenge_delay} ms")

    def handle_engineering_foraging_event(self, event):
        '''Handle events for the engineering foraging box'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.engineering_foraging_box.collidepoint(mouse_x, mouse_y):
                if self.player.inventory.get("Berries", 0) >= 1:
                    self.player.inventory["Berries"] -= 1
                    old_time = self.foraging_menu.forage_delay
                    self.foraging_menu.forage_delay = max(500, old_time - 500)
                    print(f"Used 1 Berries to purchase upgrade")
                    print(f"Foraging start delay reduced to {self.foraging_menu.forage_delay} ms")

    def handle_engineering_hunting_event(self, event):
        '''Handle events for the engineering hunting box'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.engineering_hunting_box.collidepoint(mouse_x, mouse_y):
                if self.player.inventory.get("Hide", 0) >= 1:
                    self.player.inventory["Hide"] -= 1
                    old_time = self.hunting_menu.hunt_delay
                    self.hunting_menu.hunt_delay = max(500, old_time - 500)
                    print(f"Used 1 Hide to purchase upgrade")
                    print(f"Hunting start delay reduced to {self.hunting_menu.hunt_delay} ms")
