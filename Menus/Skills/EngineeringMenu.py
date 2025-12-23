import pygame


class EngineeringMenu:
    def __init__(self, player, sidebar_width, window_width, window_height, game_state, scavenging_menu):
        '''Initialize Engineering Menu'''
        self.player = player
        self.game_state = game_state
        self.sidebar_width = sidebar_width
        self.margin = 30
        self.scavenging_menu = scavenging_menu

        # Engineering box dimensions
        self.box_x = self.sidebar_width + self.margin
        self.box_y = self.margin
        self.box_width = int(0.75 * window_width)
        self.box_height = int(0.4 * window_height)

        self.engineering_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)

        # Button for reducing scavenging delay
        self.button_rect = pygame.Rect(self.box_x + 50, self.box_y + 50, 200, 50)
        self.font = pygame.font.Font(None, 32)
        self.button_text = "Reduce Scavenge Delay"


    def draw(self, screen):
        '''Draw the Engineering Menu elements on the screen'''
        screen.fill((100, 100, 100)) 
        pygame.draw.rect(screen, (120, 120, 120), self.engineering_box)
        text_surface = self.font.render(self.button_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.button_rect.center)
        screen.blit(text_surface, text_rect)

    def handle_engineering_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_x, mouse_y = event.pos
            if self.engineering_box.collidepoint(mouse_x, mouse_y):
                old_time = self.scavenging_menu.scavenge_delay
                self.scavenging_menu.scavenge_delay = max(500, old_time - 500)
                print(f"Scavenging start delay reduced to {self.scavenging_menu.scavenge_delay} ms")
