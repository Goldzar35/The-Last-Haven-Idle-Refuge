import pygame
import random
import time 

from Entities.Player import forage_tick

class Foraging:
    def __init__(self, player):
        '''Initialize Foraging entity with player reference and foraging parameters'''
        self.player = player
        self.is_foraging = False
        self.foraging_time = 0
        self.items = {
            "Mirabelle Fruit": 1,    
            "Magic Artifact": 5,         
            "Medical Herbs": 15,         
            "Honey Comb": 25,   
            "Fresh Water": 35,
            "Berries": 45,         
            "Seeds": 55,   
            "Wild Vegetables": 65, 
            "Fish": 80,     
            "Dirty Water": 100   
        }
    #

    def toggle_foraging(self):
        '''Toggle the foraging state'''
        self.is_foraging = not self.is_foraging
        print(f"Foraging {'started' if self.is_foraging else 'stopped'}")

    def foraging(self):
        '''Perform foraging action'''
        current_time = time.time()
        if self.is_foraging and current_time - self.foraging_time >= forage_tick:
            self.foraging_time = current_time
            rand = random.uniform(1, 100) 
            for item, chance in self.items.items():
                if rand <= chance:
                    self.player.add_inventory(item, 1)
                    print(f"Found 1 {item}")
                    break
