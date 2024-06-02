import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class StatusEffect:
    def __init__(self, name, damage_percent, duration, proc_chance, effect_duration, stackable, max_stacks, refreshes_duration, tick_on_creation):
        # Properties
        self.name = name
        self.damage_percent = damage_percent
        self.duration = duration
        self.proc_chance = proc_chance
        self.effect_duration = effect_duration
        self.stackable = stackable
        self.max_stacks = max_stacks
        self.refreshes_duration = refreshes_duration
        self.tick_on_creation = tick_on_creation

    def tick(self):
        self.duration -= 1
        if self.duration == 0:
            self.damage_percent = 0

        # After ticking, if duration is 0, remove the status
        if self.duration <= 0:
            del self

    def __str__(self):
        return f"Status Name: {self.name}"