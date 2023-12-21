class TargetSelection:
    def __init__(self, target_type, targets, expensive=True, strict=False):
        self.target_type = target_type
        self.targets = targets

        # Operates as a target select when set
        # Goes for the cheapest unit when not
        self.expensive = expensive

        # If there are no units outside, no hit is registered
        self.strict = strict

    def applies(self, unit):
        if self.target_type == "Unit Class":
            return unit.unit_class in self.targets
        elif self.target_type == "Unit Name":
            return unit.name in self.targets
        return False

    def __eq__(self, other):
        return (self.target_type == other.target_type and \
                set(self.targets) == set(other.targets) and \
                self.expensive == other.expensive and \
                self.strict == other.strict)

class Casualties:
    def __init__(self):
        self.hits = 0

        # Specific Unit/Class, but no target select
        self.specific = [] 

        # Generally will take most expensive from class
        self.targets = []

        # Retreats are really only relevant for KMT
        self.retreats = []

    def add_target(self, target):
        if target is not None:
            if target.expensive == True:
                self.targets.append(target)
            else:
                self.specific.append(target)
