class TargetSelection:
    def __init__(self, target_type, targets, expensive=True, strict=False):
        self.target_type = target_type
        self.targets = targets

        # Operates as a target select when set
        # Goes for the cheapest unit when not
        self.expensive = expensive

        # If there are no units outside, no hit is registered
        self.strict = strict

class Casualties:
    def __init__(self):
        self.hits = 0

        # Specific Unit/Class, but no target select
        self.specific_hits = [] 

        # Generally will take most expensive from class
        self.targets = []
