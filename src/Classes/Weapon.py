
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
        self.status_names_modded = []
        self.status_multipliers_modded = []

        self.weapon_effects = weapon_effects

        self.installed_mods = []

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
        
    # Installs all mods to the weapon
    def install_mods(self, mods):
        # Clear the installed mods
        self.installed_mods = []

        if len(mods) > 8:
            raise ValueError("Too many mods, max is 8")
        for mod in mods:
            self.install_mod(mod)
        
    # Installs a mod to the weapon, but does not apply it to the used stats
    def install_mod(self, mod):
        modified_stats = mod.get_modified_stats()
        modified_values = mod.get_modified_values()
        
        # Apply the mod to the applied modded multiplier sums
        for i in range(len(modified_stats)):
            stat_localized = modified_stats[i]
            attribute = self.localized_to_attribute(stat_localized)

            # Elements are handled separately
            if attribute == "status_multipliers":
                # If the element is already in the status_names_modded list, add it to the existing multiplier in status_multipliers_modded, otherwise add it to status_names_modded
                if stat_localized in self.status_names_modded:
                    self.status_multipliers_modded[self.status_names_modded.index(stat_localized)] += modified_values[i]
                else:
                    self.status_names_modded.append(stat_localized)
                    self.status_multipliers_modded.append(modified_values[i])



            # Non elements
            else:
                setattr(self, attribute, getattr(self, attribute) + modified_values[i])

        # Add the mod to the installed mods
        self.installed_mods.append(mod)

    def print_installed_mods(self):
        print("Mods installed on " + self.name + ":")
        index = 1
        for mod in self.installed_mods:
            print(f"Mod {index}: {mod.name}")
            index += 1
        

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
            
            # Apply modded element status multipliers
            # Example
            # Base elements of [Impact, Radiation] with damages [200, 300] and status_multipliers of [1, 1]
            # Applying status_names_modded [Toxin, Electric, Heat] with with status_multipliers_modded of [.6, .6, 1.6]
            # Final elements are [Impact, Radiation, Toxin, Electric, Heat] with damages [200*1, 300*1, 500*.6, 500*.6, 500*1.6]
            
            print(f"Status names modded: {self.status_names_modded}, Status multipliers modded: {self.status_multipliers_modded}")
            for i in range(len(self.status_names_modded)):
                if self.status_names_modded[i] in effect.status_names:
                    # Add the modded status multiplier to the existing status multiplier
                    effect.status_damages[effect.status_names.index(self.status_names_modded[i])] *= self.status_multipliers_modded[i]
                else:
                    # Add the base status damage multiplied by the modded status multiplier
                    # Add the element to the list of elements
                    effect.status_damages.append(effect.base_status_damages_sum * self.status_multipliers_modded[i])
                    effect.status_names.append(self.status_names_modded[i])
            
            # Apply Damage multiplier to all elements
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