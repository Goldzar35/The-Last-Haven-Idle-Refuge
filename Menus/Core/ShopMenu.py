import pygame


class ShopMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state):
        '''Initialize the Shop Menu'''
        self.margin = 30
        self.player = player
        self.sidebar_width = sidebar_width
        self.window_width = window_width
        self.window_height = window_height
        self.game_state = game_state
        self.font = pygame.font.Font(None, 32)

        # Shop button 1 — Scavenging
        self.box_x_1 = self.sidebar_width + self.margin
        self.box_y_1 = self.margin
        self.box_width_1 = int(0.37 * window_width)
        self.box_height_1 = int(0.4 * window_height)
        self.shop_button_1 = pygame.Rect(self.box_x_1, self.box_y_1, self.box_width_1, self.box_height_1)
        self.shop_button_1_rect = pygame.Rect(self.box_x_1 + 50, self.box_y_1 + 50, 200, 50)
        self.shop_button_1_text = self._scavenge_button_text()

        # Shop button 2 — Foraging
        self.box_x_2 = self.sidebar_width + self.margin + self.box_width_1 + self.margin
        self.box_y_2 = self.margin
        self.box_width_2 = int(0.37 * window_width)
        self.box_height_2 = int(0.4 * window_height)
        self.shop_button_2 = pygame.Rect(self.box_x_2, self.box_y_2, self.box_width_2, self.box_height_2)
        self.shop_button_2_rect = pygame.Rect(self.box_x_2 + 50, self.box_y_2 + 50, 200, 50)
        self.shop_button_2_text = self._forage_button_text()

        # Shop button 3 — Hunting
        self.box_x_3 = self.sidebar_width + self.margin
        self.box_y_3 = self.margin + self.box_height_1 + self.margin
        self.box_width_3 = int(0.37 * window_width)
        self.box_height_3 = int(0.4 * window_height)
        self.shop_button_3 = pygame.Rect(self.box_x_3, self.box_y_3, self.box_width_3, self.box_height_3)
        self.shop_button_3_rect = pygame.Rect(self.box_x_3 + 50, self.box_y_3 + 50, 200, 50)
        self.shop_button_3_text = self._hunt_button_text()

        # Shop button 4 — Coming Soon
        self.box_x_4 = self.sidebar_width + self.margin + self.box_width_3 + self.margin
        self.box_y_4 = self.margin + self.box_height_2 + self.margin
        self.box_width_4 = int(0.37 * window_width)
        self.box_height_4 = int(0.4 * window_height)
        self.shop_button_4 = pygame.Rect(self.box_x_4, self.box_y_4, self.box_width_4, self.box_height_4)
        self.shop_button_4_rect = pygame.Rect(self.box_x_4 + 50, self.box_y_4 + 50, 200, 50)
        self.shop_button_4_text = "Coming Soon"

    # --- Button text helpers ---

    def _scavenge_button_text(self):
        if self.player.scavenge_tick <= 0.1:
            return "Scavenging Knowledge: MAXED"
        cost = self.scavenge_upgrade_cost()
        cost_str = ", ".join([f"{item}: {qty}" for item, qty in cost.items()])
        return f"Scavenging Knowledge Cost: {cost_str}"

    def _forage_button_text(self):
        if self.player.forage_tick <= 0.1:
            return "Foraging Knowledge: MAXED"
        cost = self.forage_upgrade_cost()
        cost_str = ", ".join([f"{item}: {qty}" for item, qty in cost.items()])
        return f"Foraging Knowledge Cost: {cost_str}"

    def _hunt_button_text(self):
        if self.player.hunting_tick <= 0.1:
            return "Hunting Knowledge: MAXED"
        cost = self.hunting_upgrade_cost()
        cost_str = ", ".join([f"{item}: {qty}" for item, qty in cost.items()])
        return f"Hunting Knowledge Cost: {cost_str}"

    # --- Cost definitions ---

    def scavenge_upgrade_cost(self):
        '''Define the cost for scavenging upgrade'''
        return {"Wood Planks": 1 + self.player.scavenge_upgrade_count}

    def forage_upgrade_cost(self):
        '''Define the cost for foraging upgrade'''
        return {"Berries": 1 + self.player.forage_upgrade_count}

    def hunting_upgrade_cost(self):
        '''Define the cost for hunting upgrade'''
        return {"Meat": 1 + self.player.hunting_upgrade_count}

    def can_afford(self, cost):
        '''Check if the player can afford a given cost dict'''
        return all(self.player.inventory.get(item, 0) >= qty for item, qty in cost.items())

    def draw(self, screen):
        '''Draw the Shop Menu elements on the screen'''
        screen.fill((40, 40, 40))
        for btn, text in [
            (self.shop_button_1, self.shop_button_1_text),
            (self.shop_button_2, self.shop_button_2_text),
            (self.shop_button_3, self.shop_button_3_text),
            (self.shop_button_4, self.shop_button_4_text),
        ]:
            pygame.draw.rect(screen, (90, 90, 90), btn)
            text_surface = self.font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, text_surface.get_rect(center=btn.center))

    def handle_shop_button_1_event(self, event):
        '''Handle events for shop_button_1 — reduces scavenge tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_1.collidepoint(mouse_x, mouse_y):
                if self.player.scavenge_tick <= 0.1:
                    print("Scavenge tick maxed")
                elif not self.can_afford(self.scavenge_upgrade_cost()):
                    print("Cannot afford scavenging upgrade")
                else:
                    self.player.remove_inventory_bulk(self.scavenge_upgrade_cost())
                    self.player.scavenge_upgrade_count += 1
                    self.player.scavenge_tick = max(0.1, round(self.player.scavenge_tick - 0.1, 2))
                    self.shop_button_1_text = self._scavenge_button_text()
                    print(f"Scavenge upgrades: {self.player.scavenge_upgrade_count}, tick: {self.player.scavenge_tick}")

    def handle_shop_button_2_event(self, event):
        '''Handle events for shop_button_2 — reduces forage tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_2.collidepoint(mouse_x, mouse_y):
                if self.player.forage_tick <= 0.1:
                    print("Forage tick maxed")
                elif not self.can_afford(self.forage_upgrade_cost()):
                    print("Cannot afford foraging upgrade")
                else:
                    self.player.remove_inventory_bulk(self.forage_upgrade_cost())
                    self.player.forage_upgrade_count += 1
                    self.player.forage_tick = max(0.1, round(self.player.forage_tick - 0.1, 2))
                    self.shop_button_2_text = self._forage_button_text()
                    print(f"Forage upgrades: {self.player.forage_upgrade_count}, tick: {self.player.forage_tick}")

    def handle_shop_button_3_event(self, event):
        '''Handle events for shop_button_3 — reduces hunting tick speed'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_3.collidepoint(mouse_x, mouse_y):
                if self.player.hunting_tick <= 0.1:
                    print("Hunting tick maxed")
                elif not self.can_afford(self.hunting_upgrade_cost()):
                    print("Cannot afford hunting upgrade")
                else:
                    self.player.remove_inventory_bulk(self.hunting_upgrade_cost())
                    self.player.hunting_upgrade_count += 1
                    self.player.hunting_tick = max(0.1, round(self.player.hunting_tick - 0.1, 2))
                    self.shop_button_3_text = self._hunt_button_text()
                    print(f"Hunting upgrades: {self.player.hunting_upgrade_count}, tick: {self.player.hunting_tick}")

    def handle_shop_button_4_event(self, event):
        '''Handle events for shop_button_4'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.shop_button_4.collidepoint(mouse_x, mouse_y):
                print("Shop Button 4 clicked!")
