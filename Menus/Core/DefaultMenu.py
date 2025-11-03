import pygame

class DefaultMenu:
    def __init__(self, player, sidebar_width, window_width, window_height):
        # Initialize anything specific to the Default Menu here
        self.player = player
        self.margin = 30
        self.sidebar_width = sidebar_width
        self.window_width = window_width
        self.window_height = window_height

        # Box dimensions
        self.box_x = self.sidebar_width + self.margin
        self.box_y = self.margin
        self.box_width = int(0.75 * window_width) - 2 * self.margin
        self.box_height = int(0.4 * window_height)

        self.idk_box = pygame.Rect(self.box_x, self.box_y, self.box_width, self.box_height)

        self.additional_boxes = [
            pygame.Rect(self.box_x, self.box_y + self.box_height + 20, self.box_width, 50),
            pygame.Rect(self.box_x, self.box_y + self.box_height + 90, self.box_width, 50),
            pygame.Rect(self.box_x, self.box_y + self.box_height + 160, self.box_width, 50),
            pygame.Rect(self.box_x, self.box_y + self.box_height + 230, self.box_width, 50),
        ]
        self.boxes_active = False 

    def draw(self, screen):
        screen.fill((40, 40, 40))  
        pygame.draw.rect(screen, (80, 80, 80), self.idk_box)

        if self.boxes_active:
            for box in self.additional_boxes:
                pygame.draw.rect(screen, (150, 150, 150), box)


    def toggle_additional_boxes(self):
        self.boxes_active = not self.boxes_active

    # When idk_box is clicked toggle additional boxes
    def handle_box_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_x, mouse_y = event.pos
            if self.idk_box.collidepoint(mouse_x, mouse_y):
                self.toggle_additional_boxes()
                print("idk_box clicked! Toggling additional boxes.")



