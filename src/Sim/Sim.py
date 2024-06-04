import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.Classes.Weapon import Weapon
from src.Classes.WeaponEffect import WeaponEffect
from src.Classes.Status import Status
from src.Classes.Enemy import Enemy
from src.Classes.Mod import Mod

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
print("Enemy before hit")
print(enemy1)
print()

# Create some sample weapons
weapon2 = Weapon("Lex Prime Incarnon Form", .667, 20, None, 
                 [WeaponEffect("Direct", [400, 800], ["Impact", "Radiation"], .44, .54, 3.4)])

weapon1 = Weapon("Laetum Incarnon Form", 6.67, 216, None,
                 [WeaponEffect("Direct", [100], ["Radiation"], .42, .12, 2.2),
                  WeaponEffect("Radial", [300], ["Radiation"], .42, .12, 2.2)])

# Print the weapon stats
print("Stats before modding")
weapon1.print_stats()
print()

# Create some sample mods
mods = [#Mod("Riven", ["Damage"], [1.65]),
        Mod("Lethal Torrent", ["Fire Rate", "Multishot"], [.6, .6]),
        Mod("Pistol Pestilence", ["Toxin", "Status Chance"], [.6, .6]),
        Mod("Creeping Bullseye", ["Critical Chance", "Fire Rate"], [2, -.2]),

        Mod("Barrel Diffusion", ["Multishot"], [1.1]),
        Mod("Hornet Strike", ["Damage"], [2.2]),
        Mod("Jolt", ["Electric", "Status Chance"], [.6, .6]),
        Mod("Primed Heated Charge", ["Heat"], [1.65])
        ]


# Install mods
weapon1.install_mods(mods)

# Print the installed mods
weapon1.print_installed_mods()
print()

# Apply them all to see the modded sums (like an invisible save button in Arsenal)
weapon1.apply_mods()

# Print the modded stats
print("Stats after modding")
weapon1.print_stats()
print()

# Hit the enemy with the weapon
enemy1.hit_by(weapon1, "Direct")


print("Enemy after hit")
print(enemy1)
print()

