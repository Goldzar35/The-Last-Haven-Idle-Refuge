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
        self.button_text = self._scavenge_button_text()

        # Engineering foraging box dimensions
        self.box_x_2 = self.sidebar_width + self.margin
        self.box_y_2 = self.box_y_1 + self.box_height_1
        self.box_width_2 = int(0.75 * window_width)
        self.box_height_2 = int(0.2 * window_height)

        self.engineering_foraging_box = pygame.Rect(self.box_x_2, self.box_y_2, self.box_width_2, self.box_height_2)

        # Button for reducing foraging delay
        self.foraging_button_rect = pygame.Rect(self.box_x_2 + 50, self.box_y_2 + 50, 200, 50)
        self.foraging_button_text = self._forage_button_text()

        # Engineering hunting box dimensions
        self.box_x_3 = self.sidebar_width + self.margin
        self.box_y_3 = self.box_y_2 + self.box_height_2
        self.box_width_3 = int(0.75 * window_width)
        self.box_height_3 = int(0.2 * window_height)

        self.engineering_hunting_box = pygame.Rect(self.box_x_3, self.box_y_3, self.box_width_3, self.box_height_3)

        # Button for reducing hunting delay
        self.hunting_button_rect = pygame.Rect(self.box_x_3 + 50, self.box_y_3 + 50, 200, 50)
        self.hunting_button_text = self._hunt_button_text()

    # --- Cost helpers (scale with number of upgrades purchased) ---

    def _scavenge_upgrade_count(self):
        return (3000 - self.scavenging_menu.scavenge_delay) // 500

    def _forage_upgrade_count(self):
        return (3000 - self.foraging_menu.forage_delay) // 500

    def _hunt_upgrade_count(self):
        return (3000 - self.hunting_menu.hunt_delay) // 500

    def _scavenge_eng_cost(self):
        return {"Cement": 1 + self._scavenge_upgrade_count()}

    def _forage_eng_cost(self):
        return {"Seeds": 1 + self._forage_upgrade_count()}

    def _hunt_eng_cost(self):
        return {"Bones": 1 + self._hunt_upgrade_count()}

    # --- Button text helpers ---

    def _scavenge_button_text(self):
        if self.scavenging_menu.scavenge_delay <= 500:
            return "Scavenge Delay: MAXED"
        cost = self._scavenge_eng_cost()
        cost_str = ", ".join([f"{item}: {qty}" for item, qty in cost.items()])
        return f"Reduce Scavenge Delay ({self.scavenging_menu.scavenge_delay}ms) | Cost: {cost_str}"

    def _forage_button_text(self):
        if self.foraging_menu.forage_delay <= 500:
            return "Forage Delay: MAXED"
        cost = self._forage_eng_cost()
        cost_str = ", ".join([f"{item}: {qty}" for item, qty in cost.items()])
        return f"Reduce Forage Delay ({self.foraging_menu.forage_delay}ms) | Cost: {cost_str}"

    def _hunt_button_text(self):
        if self.hunting_menu.hunt_delay <= 500:
            return "Hunt Delay: MAXED"
        cost = self._hunt_eng_cost()
        cost_str = ", ".join([f"{item}: {qty}" for item, qty in cost.items()])
        return f"Reduce Hunt Delay ({self.hunting_menu.hunt_delay}ms) | Cost: {cost_str}"

    def draw(self, screen):
        '''Draw the Engineering Menu elements on the screen'''
        screen.fill((40, 40, 40))

        # Dim boxes that are maxed out
        scav_color = (70, 70, 70) if self.scavenging_menu.scavenge_delay <= 500 else (120, 120, 120)
        forage_color = (70, 70, 70) if self.foraging_menu.forage_delay <= 500 else (150, 150, 150)
        hunt_color = (70, 70, 70) if self.hunting_menu.hunt_delay <= 500 else (180, 180, 180)

        pygame.draw.rect(screen, scav_color, self.engineering_scavenging_box)
        pygame.draw.rect(screen, forage_color, self.engineering_foraging_box)
        pygame.draw.rect(screen, hunt_color, self.engineering_hunting_box)

        # Engineering scavenging button
        pygame.draw.rect(screen, scav_color, self.button_rect)
        scavenge_text_surface = self.font.render(self.button_text, True, (255, 255, 255))
        scavenge_text_rect = scavenge_text_surface.get_rect(center=self.engineering_scavenging_box.center)
        screen.blit(scavenge_text_surface, scavenge_text_rect)

        # Engineering foraging button
        pygame.draw.rect(screen, forage_color, self.foraging_button_rect)
        forage_text_surface = self.font.render(self.foraging_button_text, True, (255, 255, 255))
        forage_text_rect = forage_text_surface.get_rect(center=self.engineering_foraging_box.center)
        screen.blit(forage_text_surface, forage_text_rect)

        # Engineering hunting button
        pygame.draw.rect(screen, hunt_color, self.hunting_button_rect)
        hunting_text_surface = self.font.render(self.hunting_button_text, True, (255, 255, 255))
        hunting_text_rect = hunting_text_surface.get_rect(center=self.engineering_hunting_box.center)
        screen.blit(hunting_text_surface, hunting_text_rect)

    def handle_engineering_scavenging_event(self, event):
        '''Handle events for the engineering scavenging box'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.engineering_scavenging_box.collidepoint(mouse_x, mouse_y):
                if self.scavenging_menu.scavenge_delay <= 500:
                    print("Scavenging delay maxed")
                else:
                    cost = self._scavenge_eng_cost()
                    if all(self.player.inventory.get(item, 0) >= qty for item, qty in cost.items()):
                        for item, qty in cost.items():
                            self.player.inventory[item] -= qty
                        self.scavenging_menu.scavenge_delay = max(500, self.scavenging_menu.scavenge_delay - 500)
                        self.button_text = self._scavenge_button_text()
                        print(f"Scavenging start delay reduced to {self.scavenging_menu.scavenge_delay}ms")
                    else:
                        print("Cannot afford scavenging engineering upgrade")

    def handle_engineering_foraging_event(self, event):
        '''Handle events for the engineering foraging box'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.engineering_foraging_box.collidepoint(mouse_x, mouse_y):
                if self.foraging_menu.forage_delay <= 500:
                    print("Foraging delay maxed")
                else:
                    cost = self._forage_eng_cost()
                    if all(self.player.inventory.get(item, 0) >= qty for item, qty in cost.items()):
                        for item, qty in cost.items():
                            self.player.inventory[item] -= qty
                        self.foraging_menu.forage_delay = max(500, self.foraging_menu.forage_delay - 500)
                        self.foraging_button_text = self._forage_button_text()
                        print(f"Foraging start delay reduced to {self.foraging_menu.forage_delay}ms")
                    else:
                        print("Cannot afford foraging engineering upgrade")

    def handle_engineering_hunting_event(self, event):
        '''Handle events for the engineering hunting box'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.engineering_hunting_box.collidepoint(mouse_x, mouse_y):
                if self.hunting_menu.hunt_delay <= 500:
                    print("Hunting delay maxed")
                else:
                    cost = self._hunt_eng_cost()
                    if all(self.player.inventory.get(item, 0) >= qty for item, qty in cost.items()):
                        for item, qty in cost.items():
                            self.player.inventory[item] -= qty
                        self.hunting_menu.hunt_delay = max(500, self.hunting_menu.hunt_delay - 500)
                        self.hunting_button_text = self._hunt_button_text()
                        print(f"Hunting start delay reduced to {self.hunting_menu.hunt_delay}ms")
                    else:
                        print("Cannot afford hunting engineering upgrade")