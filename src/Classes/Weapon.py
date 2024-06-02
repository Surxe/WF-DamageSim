
class Weapon:
    def __init__(self, name, fire_rate, magazine_size, reload_time, weapon_effects):
        self.name = name

        self.fire_rate = fire_rate
        self.magazine_size = magazine_size
        self.reload_time = reload_time

        self.multishot = 1

        self.weapon_effects = weapon_effects

    def hit(self, enemy_object, direct_or_aoe):
        # Total the damage
        damage = 0

        if direct_or_aoe == "Direct": # direct hits apply direct hit and radial hit
            for weapon_effect in self.weapon_effects:
                damage += weapon_effect.hit(enemy_object)

        elif direct_or_aoe == "AOE": # aoe hits only apply radial hit
            for weapon_effect in self.weapon_effects:
                if weapon_effect.name == "Radial": #assumes no falloff
                    damage += weapon_effect.hit_aoe(enemy_object)

        return damage


    def __str__(self):
        str = self.name + " Effects: "
        for weapon_effect in self.weapon_effects:
            str += weapon_effect.__str__() + ", "
        # Remove the last comma
        str = str[:-2]
        return str