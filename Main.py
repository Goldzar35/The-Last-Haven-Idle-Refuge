import pygame

from Entities.Player import Player
from Entities.Button import Button
from Entities.GameState import GameState

from Menus.Core.DefaultMenu import DefaultMenu 
from Menus.Core.InventoryMenu import InventoryMenu
from Menus.Core.ShopMenu import ShopMenu
from Menus.Skills.ScavengingMenu import *
from Menus.Skills.ForagingMenu import ForagingMenu
from Menus.Skills.HuntingMenu import HuntingMenu
from Menus.Skills.EngineeringMenu import EngineeringMenu
from Menus.Skills.MedicineMenu import MedicineMenu
from Menus.Skills.CookingMenu import CookingMenu
from Menus.Skills.FortificationMenu import FortificationMenu
from Menus.Skills.CommunityMenu import CommunityMenu
from Menus.Skills.LegacyMenu import LegacyMenu

# Initialize pygame
pygame.init()

# Initialize player
player = Player()

# Initialize GameState
game_state = GameState()

# Initial window size
info = pygame.display.Info()
window_width, window_height = 1280, 720

# Base Display
screen = pygame.display.set_mode((window_width, window_height))
screen.fill((40, 40, 40))

# Sidebar size and demension variables
sidebar_width = int(0.2 * window_width)
sidebar_height = window_height
button_count = 12
button_height = int(0.1 * window_height)
gap = int(0.01 * window_height)
font = pygame.font.SysFont(None, 36)

# Button names
sidebar_buttons = []
button_names = ["Default", "Inventory", "Shop", "Scavenging", "Foraging", "Hunting", "Engineering", "Medicine", "Cooking", "Fortification", "Community", "Legacy"]

# Calculate total height and max scroll
total_height = button_count * button_height + (button_count + 1) * gap
max_scroll = max(0, total_height - sidebar_height)
scroll_offset = 0
scroll_speed = 15 

# Draw the sidebar background
pygame.draw.rect(screen, (30, 30, 30), (0, 0, 200, 800)) 

# Initalize buttons
for i, name in enumerate(button_names):
    y = gap + i * (button_height + gap)
    btn = Button(0, y, sidebar_width, button_height, name, i) 
    sidebar_buttons.append(btn)

# Initialize Menus
menus = {
    0: DefaultMenu(game_state.player, sidebar_width, window_width, window_height),
    1: InventoryMenu(game_state.player, sidebar_width),
    2: ShopMenu(game_state.player),
    3: ScavengingMenu(game_state.player, game_state, sidebar_width, window_width, window_height),
    4: ForagingMenu(game_state.player, game_state, sidebar_width, window_width, window_height),
    5: HuntingMenu(game_state.player),
    6: EngineeringMenu(game_state.player),
    7: MedicineMenu(game_state.player),
    8: CookingMenu(game_state.player),
    9: FortificationMenu(game_state.player, sidebar_width, window_width, window_height),
    10: CommunityMenu(game_state.player),
    11: LegacyMenu(game_state.player)
}

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEWHEEL:
            scroll_offset -= event.y * scroll_speed
            scroll_offset = max(0, min(scroll_offset, max_scroll)) 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            mouse_x, mouse_y = event.pos
            for btn in sidebar_buttons:
                if btn.is_clicked((mouse_x, mouse_y)):
                    game_state.current_menu = btn.action
        # For Default Menu
        if game_state.current_menu in menus and hasattr(menus[game_state.current_menu], "handle_box_event"):
            menus[game_state.current_menu].handle_box_event(event)
        # For Foraging
        if game_state.current_menu in menus and hasattr(menus[game_state.current_menu], "handle_foraging_event"):
            menus[game_state.current_menu].handle_foraging_event(event)
        # For Scavenging
        if game_state.current_menu in menus and hasattr(menus[game_state.current_menu], "handle_scavenge_event"):
            menus[game_state.current_menu].handle_scavenge_event(event)
        # For Fortification
        if game_state.current_menu in menus and hasattr(menus[game_state.current_menu], "handle_fortification_event"):
            menus[game_state.current_menu].handle_fortification_event(event)

    # Update scavenging logic globally
    game_state.update_scavenging()
    game_state.update_foraging() 
    
    # Draw the current menu background
    if game_state.current_menu in menus and hasattr(menus[game_state.current_menu], "draw"):
        menus[game_state.current_menu].draw(screen)

    # Update buttons
    for i, btn in enumerate(sidebar_buttons):
        # Adjust button position for scrolling
        btn.rect.y = gap + i * (button_height + gap) - scroll_offset
        # Only draw buttons that are visible in the sidebar
        if -button_height < btn.rect.y < sidebar_height:
            btn.draw(screen, font)

    # Updates display
    pygame.display.flip() 

pygame.quit()

