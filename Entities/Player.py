import pygame

class Player:
    def __init__(self):
        ''' Initialize player with default attributes '''
        self.inventory = {
            "Gasoline": 0,    
            "People": 0,         
            "Canned Food": 0,         
            "Electronics": 0,   
            "Spare Parts": 0,
            "Nails": 0,         
            "Metal Scrap": 0,    
            "Rope": 0,   
            "Fabric Scrap": 0,   
            "Cement": 0,     
            "Wood Planks": 0,
            "Mirabelle Fruit": 0,    
            "Magic Artifact": 0,         
            "Medical Herbs": 0,         
            "Honey Comb": 0,   
            "Fresh Water": 0,
            "Berries": 0,         
            "Seeds": 0,   
            "Wild Vegetables": 0, 
            "Fish": 0,     
            "Dirty Water": 0, 
            "Intact Infected Organ": 0,    
            "Boar Tusk": 0,         
            "Blood Sample": 0,         
            "Eggs": 0,
            "Zombie Flesh": 0,
            "Animal Fat": 0,
            "Hide": 0,
            "Bones": 0,
            "Meat": 0
        }
        self.scavenging = False
        self.foraging = False
        self.hunting = False
        self.scavenge_tick = 2.0
        self.forage_tick = 2.0
        self.hunting_tick = 2.0

        self.scavenge_upgrade_count = 0
        self.forage_upgrade_count = 0
        self.hunting_upgrade_count = 0

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

    def remove_inventory_bulk(self, items_dict):
        ''' Remove multiple items from the player's inventory '''
        for item, quantity in items_dict.items():
            if item in self.inventory and self.inventory[item] >= quantity:
                self.inventory[item] -= quantity

    def show_inventory(self):
        ''' Print the player's inventory to the console '''
        for item, quantity in self.inventory.items():
            print(f"  {item}: {quantity}")