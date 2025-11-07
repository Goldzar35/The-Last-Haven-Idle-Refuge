import pygame

scavenge_tick = 0.5

class Player:
    def __init__(self):
        ''' Initialize player with default attributes '''
        self.inventory = {
            "Wood Planks": 0,
            "Cement": 0,
            "Rope": 0,
            "Nails": 0,
            "Metal Scrap": 0,
            "Electronics": 0,
            "Fabric Scrap": 0,
            "Spare Parts": 0,
            "Gasoline": 0,
            "People": 0,
            "Batteries": 0
        }
        self.scavenging = False

    def add_inventory(self, items, quantity):
        ''' Add items to the player's inventory '''
        if items in self.inventory:
            self.inventory[items] += quantity
        else:
            self.inventory[items] = quantity

    def remove_inventory(self, item, quantity):
        ''' Remove items from the player's inventory '''
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
        else:
            pass

    def show_inventory(self):
        ''' Print the player's inventory to the console '''
        print(self.inventory)
        for item, quantity in self.inventory.items():
            print(f"  {item}: {quantity}")