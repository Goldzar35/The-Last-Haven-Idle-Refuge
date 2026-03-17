import pygame

from Utils import resource_path


class FortificationMenu:
    def __init__(self, player, fortification, sidebar_width, window_width, window_height, game_state):
        '''Initialize Fortification Menu'''
        self.player = player
        self.fortification = fortification
        self.margin = 30
        self.sidebar_width = sidebar_width
        self.backgrounds = [
            pygame.image.load(resource_path("Assets/Base_lvl_1.png")).convert(),
            pygame.image.load(resource_path("Assets/Base_lvl_2.png")).convert(),
            pygame.image.load(resource_path("Assets/Base_lvl_3.png")).convert(),
            pygame.image.load(resource_path("Assets/Base_lvl_4.png")).convert(),
            pygame.image.load(resource_path("Assets/Base_lvl_5.png")).convert(),
            pygame.image.load(resource_path("Assets/Base_lvl_6.png")).convert(),
        ]
        self.max_level = len(self.backgrounds) - 1

        # Fortification box dimensions
        self.box_width = int(0.50 * window_width)
        self.box_height = int(0.15 * window_height)
        self.box_x = self.sidebar_width + ((window_width - self.sidebar_width - self.box_width) // 2)
        self.box_y = window_height - self.box_height - self.margin
        self.fortification_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)

        self.button_font = pygame.font.Font(None, 25)
        self.button_text = self._button_text()

    # --- Helpers ---

    def _upgrade_cost(self):
        '''Define the cost for the next fortification level'''
        return {"Wood Planks": 5 + (self.fortification.background_index * 5)}

    def _button_text(self):
        '''Generate button text based on current level'''
        level = self.fortification.background_index + 1
        if self.fortification.background_index >= self.max_level:
            return f"Fortification Level {level}: MAXED"
        cost = self._upgrade_cost()
        cost_str = ", ".join([f"{item}: {qty}" for item, qty in cost.items()])
        return f"Fortify (Level {level}) | Cost: {cost_str}"

    def _can_afford(self):
        '''Check if the player can afford the upgrade'''
        return all(self.player.inventory.get(item, 0) >= qty for item, qty in self._upgrade_cost().items())

    def draw(self, screen):
        '''Draw the Fortification Menu elements on the screen'''
        screen.fill((0, 0, 0))
        screen_width, screen_height = screen.get_size()
        bg = self.backgrounds[self.fortification.background_index]
        bg_scaled = pygame.transform.smoothscale(bg, (screen_width, screen_height))
        screen.blit(bg_scaled, (0, 0))
        box_color = (70, 70, 70) if self.fortification.background_index >= self.max_level else (100, 100, 100)
        pygame.draw.rect(screen, box_color, self.fortification_box)
        text_surface = self.button_font.render(self.button_text, True, (255, 255, 255))
        screen.blit(text_surface, text_surface.get_rect(center=self.fortification_box.center))

    def handle_fortification_event(self, event):
        '''Handle events for the fortification_box to change background'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if self.fortification_box.collidepoint(mouse_x, mouse_y):
                if self.fortification.background_index >= self.max_level:
                    print("Fortification maxed")
                elif not self._can_afford():
                    print("Cannot afford fortification upgrade")
                else:
                    cost = self._upgrade_cost()
                    for item, qty in cost.items():
                        self.player.inventory[item] -= qty
                    self.fortification.background_index += 1
                    self.button_text = self._button_text()
                    print(f"Fortification upgraded to level {self.fortification.background_index + 1}")