import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Mod:
    def __init__(self, name, modified_stats, modified_values):
        self.name = name
        self.modified_stats = modified_stats
        self.modified_values = modified_values
        

    def __str__(self):
        return f"{self.name}"
    
    def get_modified_stats(self):
        return self.modified_stats
    def get_modified_values(self):
        return self.modified_values