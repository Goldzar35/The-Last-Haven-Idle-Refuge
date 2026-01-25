import pygame

class Button:
    def __init__(self, x, y, width, height, text, action):
        '''Initialize a button with position, size, text, and action'''
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self, screen, font):
        '''Draw the button on the screen'''
        pygame.draw.rect(screen, (170, 170, 170), self.rect)  
        text_surf = font.render(self.text, True, (0, 0, 0))  
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, mouse_pos):
        '''Check if the button is clicked based on mouse position'''
        return self.rect.collidepoint(mouse_pos)