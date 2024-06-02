import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.Classes.Status import Status

class WeaponEffect:
    def __init__(self, name, status_damages, status_names, status_chance, crit_chance, crit_multiplier):
        self.name = name
        self.status_damages = status_damages
        status_objects = []
        for status_name in status_names:
            status_objects.append(Status.getStatusObject(status_name))
        self.status_objects = status_objects
        self.status_chance = status_chance

        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier

    def hit(self, enemy_object):
        # Calculate the damage
        damage = 0
        return damage

    def __str__(self):
        return f"{self.name} - Status Damages: {self.status_damages}, Crit Chance: {self.crit_chance}, Crit Multiplier: {self.crit_multiplier}"