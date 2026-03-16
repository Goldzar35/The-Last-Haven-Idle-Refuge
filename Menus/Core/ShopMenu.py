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
        cost = self.scavenge_upgrade_cost()
        scavenge_cost_str = ", ".join([f"{item}: {quantity}" for item, quantity in cost.items()])
        self.shop_button_1_text = f"Scavenging Knowledge Cost: {scavenge_cost_str}"

        # Shop button 2 box dimensions
        self.box_x_2 = self.sidebar_width + self.margin + self.box_width_1 + self.margin
        self.box_y_2 = self.margin
        self.box_width_2 = int(0.37 * window_width)
        self.box_height_2 = int(0.4 * window_height)

        self.shop_button_2 = pygame.Rect(self.box_x_2, self.box_y_2, self.box_width_2, self.box_height_2)

        # Button for shop button 2 text
        self.shop_button_2_rect = pygame.Rect(self.box_x_2 + 50, self.box_y_2 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        forage_cost = self.forage_upgrade_cost()
        forage_cost_str = ", ".join([f"{item}: {quantity}" for item, quantity in forage_cost.items()])
        self.shop_button_2_text = f"Foraging Knowledge Cost: {forage_cost_str}"

        # Shop button 3 box dimensions
        self.box_x_3 = self.sidebar_width + self.margin
        self.box_y_3 = self.margin + self.box_height_1 + self.margin
        self.box_width_3 = int(0.37 * window_width)
        self.box_height_3 = int(0.4 * window_height)

        self.shop_button_3 = pygame.Rect(self.box_x_3, self.box_y_3, self.box_width_3, self.box_height_3)

        # Button for shop button 3 text
        self.shop_button_3_rect = pygame.Rect(self.box_x_3 + 50, self.box_y_3 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        hunting_cost = self.hunting_upgrade_cost()
        hunting_cost_str = ", ".join([f"{item}: {quantity}" for item, quantity in hunting_cost.items()])
        self.shop_button_3_text = f"Hunting Knowledge Cost: {hunting_cost_str}"

        # Shop button 4 box dimensions
        self.box_x_4 = self.sidebar_width + self.margin + self.box_width_3 + self.margin
        self.box_y_4 = self.margin + self.box_height_2 + self.margin
        self.box_width_4 = int(0.37 * window_width)
        self.box_height_4 = int(0.4 * window_height)

        self.shop_button_4 = pygame.Rect(self.box_x_4, self.box_y_4, self.box_width_4, self.box_height_4)

        # Button for shop button 4 text
        self.shop_button_4_rect = pygame.Rect(self.box_x_4 + 50, self.box_y_4 + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.shop_button_4_text = "Coming Soon"

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

    def can_afford(self, scavenge_upgrade_cost):
        '''Check if the player can afford the scavenging upgrade'''
        for item, cost in scavenge_upgrade_cost.items():
            if self.player.inventory.get(item, 0) < cost:
                return False
        return True

    def scavenge_upgrade_cost(self):
        '''Define the cost for scavenging upgrade'''
        return {
            "Wood Planks": 1 + (self.player.scavenge_upgrade_count * 1),
        }

    def forage_upgrade_cost(self):
        '''Define the cost for foraging upgrade'''
        return {
            "Berries": 1 + (self.player.forage_upgrade_count * 1),
        }

    def hunting_upgrade_cost(self):
        '''Define the cost for hunting upgrade'''
        return {
            "Meat": 1 + (self.player.hunting_upgrade_count * 1),
        }

    def handle_shop_button_1_event(self, event):
        '''Handle events for shop_button_1 to perform an action, this button will reduce the scavenge tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_1.collidepoint(mouse_x, mouse_y):
                if self.player.scavenge_tick > 0.1 and self.can_afford(self.scavenge_upgrade_cost()):
                    self.player.remove_inventory_bulk(self.scavenge_upgrade_cost())
                    self.player.scavenge_upgrade_count += 1
                    self.player.scavenge_tick = max(0.1, round(self.player.scavenge_tick - 0.1, 2))
                    scavenge_cost = self.scavenge_upgrade_cost()
                    scavenge_cost_str = ", ".join([f"{item}: {quantity}" for item, quantity in scavenge_cost.items()])
                    self.shop_button_1_text = f"Scavenging Knowledge Cost: {scavenge_cost_str}"
                    print("Shop Button 1 clicked!")
                    print("Scavenge upgrades purchased:", self.player.scavenge_upgrade_count)
                    print("New scavenge tick:", self.player.scavenge_tick)
                elif self.player.scavenge_tick > 0.1 and not self.can_afford(self.scavenge_upgrade_cost()):
                    print("Cannot afford scavenging upgrade")
                else:
                    print("Scavenge tick maxed")

    def handle_shop_button_2_event(self, event):
        '''Handle events for shop_button_2 to perform an action, this button will reduce the forage tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_2.collidepoint(mouse_x, mouse_y):
                if self.player.forage_tick > 0.1 and self.can_afford(self.forage_upgrade_cost()):
                    self.player.remove_inventory_bulk(self.forage_upgrade_cost())
                    self.player.forage_upgrade_count += 1
                    self.player.forage_tick = max(0.1, round(self.player.forage_tick - 0.1, 2))
                    forage_cost = self.forage_upgrade_cost()
                    forage_cost_str = ", ".join([f"{item}: {quantity}" for item, quantity in forage_cost.items()])
                    self.shop_button_2_text = f"Foraging Knowledge Cost: {forage_cost_str}"
                    print("Shop Button 2 clicked!")
                    print("Forage upgrades purchased:", self.player.forage_upgrade_count)
                    print("New forage tick:", self.player.forage_tick)
                elif self.player.forage_tick > 0.1 and not self.can_afford(self.forage_upgrade_cost()):
                    print("Cannot afford foraging upgrade")
                else:
                    print("Forage tick maxed")

    def handle_shop_button_3_event(self, event):
        '''Handle events for shop_button_3 to perform an action, this button will reduce the hunting tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_3.collidepoint(mouse_x, mouse_y):
                if self.player.hunting_tick > 0.1 and self.can_afford(self.hunting_upgrade_cost()):
                    self.player.remove_inventory_bulk(self.hunting_upgrade_cost())
                    self.player.hunting_upgrade_count += 1
                    self.player.hunting_tick = max(0.1, round(self.player.hunting_tick - 0.1, 2))
                    hunting_cost = self.hunting_upgrade_cost()
                    hunting_cost_str = ", ".join([f"{item}: {quantity}" for item, quantity in hunting_cost.items()])
                    self.shop_button_3_text = f"Hunting Knowledge Cost: {hunting_cost_str}"
                    print("Shop Button 3 clicked!")
                    print("Hunting upgrades purchased:", self.player.hunting_upgrade_count)
                    print("New hunting tick:", self.player.hunting_tick)
                elif self.player.hunting_tick > 0.1 and not self.can_afford(self.hunting_upgrade_cost()):
                    print("Cannot afford hunting upgrade")
                else:
                    print("Hunting tick maxed")

    def handle_shop_button_4_event(self, event):
        '''Handle events for shop_button_4 to perform an action'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_4.collidepoint(mouse_x, mouse_y):
                print("Shop Button 4 clicked!")
