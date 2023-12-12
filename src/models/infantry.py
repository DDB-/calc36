from models.base_units import InfantryClass

class Militia(InfantryClass):
    def __init__(self):
        super().__init__(attack=1, defense=2, name="Militia", cost=2)

class Infantry(InfantryClass):
    def __init__(self):
        super().__init__(attack=2, defense=4, name="Infantry", cost=3)

    def does_retreat(self, side, roll):
        if self.nation is not None and side == "Attacker" and self.nation == "KMT" and roll >= 10:
            return True
        
        return False

class AirborneInfantry(InfantryClass):
    def __init__(self):
        super().__init__(attack=2, defense=2, name="Airborne Infantry", cost=3)

class EliteAirborneInfantry(InfantryClass):
    def __init__(self):
        super().__init__(attack=3, defense=3, name="Elite Airborne Infantry", cost=3)

class Marine(InfantryClass):
    def __init__(self):
        super().__init__(attack=2, defense=4, name="Marine", cost=4)

class MountainInfantry(InfantryClass):
    def __init__(self):
        super().__init__(attack=2, defense=4, name="Mountain Infantry", cost=4)

class ColonialInfantry(InfantryClass):
    def __init__(self):
        super().__init__(attack=2, defense=4, name="Colonial Infantry", cost=4)

class ForeignLegion(InfantryClass):
    def __init__(self):
        super().__init__(attack=2, defense=4, name="Foreign Legion", cost=4)

class Gurkha(InfantryClass):
    def __init__(self):
        super().__init__(attack=2, defense=4, name="Gurkha", cost=4)
