class Facility:
    def __init__(self):
        pass

    def get_defense_bonus(self, combat_round, unit):
        return 0

    def get_first_strike(self, combat_round):
        return None

    def get_bombardment_bonus(self):
        return 0

class Factory(Facility):
    def __init__(self, size="Minor"):
        super().__init__()
        self.size = size

class Base(Facility):
    def __init__(self, purpose="Air"):
        super().__init__()
        self.purpose = purpose

class Port(Facility):
    def __init__(self, size="Minor"):
        super().__init__()
        self.size = size

class Dockyard(Facility):
    def __init__(self, size="Minor"):
        super().__init__()
        self.size = size

class Shipyard(Facility):
    def __init__(self, size="Minor"):
        super().__init__()
        self.size = size

class Fortification(Facility):
    def __init__(self):
        super().__init__()

    def get_defense_bonus(self, combat_round, unit):
        if combat_round == 1 and unit.get_unit_class() == "Infantry":
            return 2
        return 0

    def get_first_strike(self, combat_round):
        return {"hit":5, "times":2}

    def get_bombardment_bonus(self):
        return -1
