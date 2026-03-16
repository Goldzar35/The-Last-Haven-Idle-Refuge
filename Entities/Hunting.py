import random
import time

from Entities.Player import Player


class Hunting:
    def __init__(self, player, hunting_tick):
        '''Initialize Hunting entity with player reference and hunting parameters'''
        self.player = player
        self.is_hunting = False
        self.hunting_time = 0
        self.hunting_tick = hunting_tick
        self.items = {
            "Intact Infected Organ": 1,
            "Boar Tusk": 5,
            "Blood Sample": 10,
            "Eggs": 15,
            "Zombie Flesh": 25,
            "Animal Fat": 40,
            "Hide": 60,
            "Bones": 80,
            "Meat": 100,
        }

    def toggle_hunting(self):
        '''Toggle the hunting state'''
        self.is_hunting = not self.is_hunting
        print(f"Hunting {'started' if self.is_hunting else 'stopped'}")

    def hunting(self):
        '''Perform hunting action'''
        current_time = time.time()
        if self.is_hunting and current_time - self.hunting_time >= self.player.hunting_tick:
            self.hunting_time = current_time
            rand = random.uniform(1, 100)
            for item, chance in self.items.items():
                if rand <= chance:
                    self.player.add_inventory(item, 1)
                    print(f"Found 1 {item}")
                    break
