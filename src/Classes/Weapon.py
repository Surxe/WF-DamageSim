
from src.Classes.Status import Status

class Weapon:
    def __init__(self, name, fire_rate, magazine_size, reload_time, weapon_effects):
        self.name = name

        # Stats of the weapon
        self.fire_rate = fire_rate
        self.magazine_size = magazine_size
        self.reload_time = reload_time

        # Sum of mods for each stat
        # Stats that apply to the weapon
        self.fire_rate_modded = 1
        self.magazine_size_modded = 1
        self.reload_speed_modded = 1
        # Stats that apply to all applicable weapon effects
        self.damage_modded = 1
        self.multishot_modded = 1 #modded only
        self.status_chance_modded = 1
        self.crit_chance_modded = 1
        self.crit_multiplier_modded = 1
        self.status_multipliers = [1] * len(Status.statuses_names) # starts empty, will be filled in install_mod

        self.weapon_effects = weapon_effects

    # Converts localized moddable stat to its respective attribute
    def localized_to_attribute(self, stat_localized):
        # Stats that apply to the weapon or to weapon effects
        localized_to_attribute = {"Fire Rate": "fire_rate_modded", 
                                  "Magazine Size": "magazine_size_modded", 
                                  "Reload Speed": "reload_speed_modded", 
                                  "Damage": "damage_modded", 
                                  "Multishot": "multishot_modded",
                                  "Status Chance": "status_chance_modded", 
                                  "Critical Chance": "crit_chance_modded", 
                                  "Critical Damage": "crit_multiplier_modded"}
        if stat_localized in localized_to_attribute:
            return localized_to_attribute[stat_localized]
        elif stat_localized in Status.statuses_names:
            return "status_multipliers"
        else:
            print(f"Invalid stat {stat_localized}")
            raise ValueError("Invalid stat")
        
    def install_mod(self, mod):
        modified_stats = mod.get_modified_stats()
        modified_values = mod.get_modified_values()
        
        # Apply the mod to the applied modded multiplier sums
        for i in range(len(modified_stats)):
            stat_localized = modified_stats[i]
            attribute = self.localized_to_attribute(stat_localized)

            # Elements are handled separately
            if attribute == "status_multipliers":
                self.status_multipliers[Status.statuses_names.index(stat_localized)] += modified_values[i]

            # Non elements
            else:
                setattr(self, attribute, getattr(self, attribute) + modified_values[i])

        # Print
        print(f"Mod {mod.name} installed on {self.name}")

    # Applies the modded sums to all applicable stats
    def apply_mods(self):
        self.fire_rate *= self.fire_rate_modded
        self.magazine_size *= self.magazine_size_modded

        if self.reload_time != None:
            self.reload_time /= self.reload_speed_modded

        for effect in self.weapon_effects:
            effect.crit_chance *= self.crit_chance_modded
            effect.crit_multiplier *= self.crit_multiplier_modded
            effect.status_chance *= self.status_chance_modded
            
            # Apply element status multipliers
            for i in range(len(Status.statuses_names)):
                if Status.statuses_names[i] in effect.status_names:
                    effect.status_damages[effect.status_names.index(Status.statuses_names[i])] *= self.status_multipliers[i]
            
            # Apply Damage
            for i in range(len(effect.status_damages)):
                effect.status_damages[i] *= self.damage_modded


    def print_stats(self):
        print(f"{self.name} - Fire Rate: {self.fire_rate}, Magazine Size: {self.magazine_size}, Reload Time: {self.reload_time}, Multishot: {self.multishot_modded}, Status Chance: {self.status_chance_modded}, Crit Chance: {self.crit_chance_modded}, Crit Multiplier: {self.crit_multiplier_modded}")
        for effect in self.weapon_effects:
            print(effect)
        

    def attack(self, direct_or_aoe):
        damage = 0

        if direct_or_aoe == "Direct": # direct hits apply direct hit and radial hit
            for weapon_effect in self.weapon_effects:
                damage += weapon_effect.hit()

        elif direct_or_aoe == "AOE": # aoe hits only apply radial hit
            for weapon_effect in self.weapon_effects:
                if weapon_effect.name == "Radial": #assumes no falloff
                    damage += weapon_effect.hit()

        return damage


    def __str__(self):
        str = self.name + " Effects: "
        for weapon_effect in self.weapon_effects:
            str += weapon_effect.__str__() + ", "
        # Remove the last comma
        str = str[:-2]
        return str