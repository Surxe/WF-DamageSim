import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.Classes.Weapon import Weapon
from src.Classes.WeaponEffect import WeaponEffect
from src.Classes.Status import Status
from src.Classes.Enemy import Enemy

# Create the statuses
statuses = [Status("Impact"),
            Status("Puncture"),
            Status("Slash"),
            Status("Heat"),
            Status("Toxin"),
            Status("Cold"),
            Status("Electric"),
            Status("Gas"),
            Status("Blast"),
            Status("Radiation"),
            Status("Viral"),
            Status("Corrosive"),
            Status("Magnetic")]

# Create an enemy
# Damage resistances not implemented due to being changed soon (Jade Shadows update), i.e. Cloned Flesh / Ferrite Armor
enemy1 = Enemy("Corrupted Heavy Gunner", 175, 97791.79, 0, 9791.1, "Steel Path")
print(enemy1)



# Create some sample weapons
weapon1 = Weapon("Lex Prime Incarnon Form", .667, 20, None, 
                 [WeaponEffect("Direct", [400, 800], ["Impact", "Radiation"], .44, .54, 3.4)])

weapon2 = Weapon("Laetum Incarnon Form", 6.67, 216, None,
                 [WeaponEffect("Direct", [100], ["Radiation"], .42, .12, 2.2),
                  WeaponEffect("Radial", [300], ["Radiation"], .42, .12, 2.2)])

# Hit the enemy with the weapon
weapon1.hit(enemy1, "Direct")

print(weapon2)