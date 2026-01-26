import pygame
import random
import time 

from Entities.Player import * 


class Scavenging:
    def __init__(self, player, scavenge_tick):
        '''Initialize Scavenging entity with player reference and scavenging parameters'''
        self.player = player
        self.is_scavenging = False
        self.scavenge_time = 0
        self.scavenge_tick = scavenge_tick
        self.items = {
            "Gasoline": 1,    
            "People": 5,         
            "Canned Food": 20,         
            "Electronics": 30,   
            "Spare Parts": 40,
            "Nails": 50,         
            "Metal Scrap": 60,    
            "Rope": 70,   
            "Fabric Scrap": 80,   
            "Cement": 90,     
            "Wood Planks": 100
        }
    
    def toggle_scavenging(self):
        '''Toggle the scavenging state'''
        self.is_scavenging = not self.is_scavenging
        print(f"Scavenging {'started' if self.is_scavenging else 'stopped'}")

    def scavenging(self):
        '''Perform scavenging action'''
        current_time = time.time()
        if self.is_scavenging and current_time - self.scavenge_time >= self.player.scavenge_tick:
            self.scavenge_time = current_time
            rand = random.uniform(1, 100) 
            for item, chance in self.items.items():
                if rand <= chance:
                    self.player.add_inventory(item, 1)
                    print(f"Found 1 {item}")
                    break
