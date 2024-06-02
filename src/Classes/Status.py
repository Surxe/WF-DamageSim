
# Valid statuses include 'Impact', 'Puncture', 'Slash', 'Heat', 'Toxin', 'Cold', 'Electric', 'Gas', 'Blast', 'Radiation', 'Viral', 'Corrosive', 'Magnetic'
# Impact: No effect
# Puncture The target receives 5% increased critical chance per proc up to 25% at 5 stacks, additive after mods, no effect on AoE or warframe abilities
# Slash: The target receives 35% of the damage dealt over 6 seconds and bypasses armor
# Heat: The target receives 50% of the damage dealt over 6 seconds, and lose all armor after 1s, refreshes duration

class Status:
    statuses_objects = []

    def __init__(self, name):
        self.name = name

        Status.statuses_objects.append(self)

    # From status name, return status object
    def getStatusObject(name):
        for status in Status.statuses_objects:
            if status.name == name:
                return status
        raise Exception(f"Status {name} not found")

    def tick(self):
        self.duration -= 1
        if self.duration == 0:
            self.damage_percent = 0

        # After ticking, if duration is 0, remove the status
        if self.duration <= 0:
            del self

    def __str__(self):
        return f"Status Name: {self.name}"
