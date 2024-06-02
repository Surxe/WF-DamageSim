

class Enemy:
    valid_paths = ["Regular", "Steel Path"]

    def __init__(self, name, level, health_points, shield_points, armor, path):
        self.name = name
        self.level = level #unused
        self.health_points = health_points
        self.shield_points = shield_points
        self.armor = armor
        self.damage_reduction = 0
        self.update_damage_reduction()
        self.status_effects = []

        if path not in Enemy.valid_paths:
            raise ValueError("Invalid path, must be in " + str(Enemy.valid_paths) + ".")
        
        self.path = path
        if path == "Steel Path":
            self.health_points *= 2.5
            self.shield_points *= 6.25
            if "Eximus" in self.name:
                self.shield_points *= 2.5
            self.armor *= 2.5
            self.update_damage_reduction()

    def update_damage_reduction(self):
        self.damage_reduction = self.armor/(self.armor+300)

    def take_damage(self, damage):
        self.health_points -= damage * (1 - self.damage_reduction)
        if self.health_points < 0:
            self.health_points = 0
            print("Enemy has died")
            del self

    def set_armor(self, armor):
        self.armor = armor
        self.update_damage_reduction()

    def add_status_effect(self, status_name):
        self.statuses.append(status_name)

    # On deletion, also remove all status effects
    def __del__(self):
        if len(self.status_effects) > 0:
            for status in self.status_effects:
                del status

    def __str__(self):
        return f"{self.name} - Level: {self.level}, Health Points: {self.health_points}, Armor: {self.armor}, EHP: {self.health_points/(1-self.damage_reduction)}"