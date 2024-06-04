import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.Classes.Status import Status
import math
import random

class WeaponEffect:
    def __init__(self, name, status_damages, status_names, status_chance, crit_chance, crit_multiplier):
        self.name = name
        self.status_damages = status_damages
        self.base_status_damages_sum = sum(status_damages)
        status_objects = []
        self.status_names = status_names
        for status_name in status_names:
            status_objects.append(Status.getStatusObject(status_name))

        self.status_multipliers = [1 for i in range(len(status_names))]
        self.status_objects = status_objects
        self.status_chance = status_chance

        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier

    def hit(self):
        # Calculate the damage

        damage = sum(self.status_damages)

        # Calculate crit
        #print(f"Rolling crit, crit chance is {self.crit_chance}")
        min_crit_tier = math.floor(self.crit_chance)
        rolled_crit = random.random() < self.crit_chance-min_crit_tier #i.e. 1.7 crit chance is 70% chance for another crit tier
        crit_tier = min_crit_tier + 1*rolled_crit
        damage *= (1 + (self.crit_multiplier-1) * crit_tier) #i.e. crit tier of 4 (red+) with 3x cd is 9x damage (1 + (3-1) * 4)
        #print("Rolled a bonus crit?", rolled_crit, "Crit tier:", crit_tier)
        # if crit_tier == 0:
        #     print("No crit", end='')
        # elif crit_tier == 1:
        #     print("Yellow crit", end='')
        # elif crit_tier == 2:
        #     print("Orange crit", end='')
        # elif crit_tier == 3:
        #     print("Red crit", end='')
        # print(" for " + str(damage) + " damage")
        print("Damaged target for " + str(damage) + " damage, pre-mitigation")

        # Register status procs

        return damage

    def __str__(self):
        return f"{self.name} - Status Damages: {self.status_damages}, Status Names: {self.status_names}, Status Chance: {self.status_chance}, Crit Chance: {self.crit_chance}, Crit Multiplier: {self.crit_multiplier}"