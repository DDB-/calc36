from models.base_units import VehicleClass
from models.battle import TargetSelection
from models.unit_mods import Blitz

class Cavalary(VehicleClass):
    def __init__(self):
        super().__init__(attack=3, defense=2, name="Cavalry", cost=3)

class MotorizedInfantry(VehicleClass):
    def __init__(self):
        super().__init__(attack=2, defense=4, name="Motorized Infantry", cost=4)

class MechanizedInfantry(VehicleClass):
    def __init__(self):
        super().__init__(attack=3, defense=4, name="Mechanized Infantry", cost=4)
        self.blitz = Blitz(ratio=1)

class AdvancedMechanizedInfantry(VehicleClass):
    def __init__(self):
        super().__init__(attack=4, defense=5, name="Advanced Mechanized Infantry", cost=4)
        self.blitz = Blitz(ratio=2)

class PanzerGrenadier(VehicleClass):
    def __init__(self):
        super().__init__(attack=4, defense=5, name="Panzer-grenadier", cost=4)
        self.blitz = Blitz(ratio=None)

class TankDestroyer(VehicleClass):
    def __init__(self):
        super().__init__(attack=3, defense=4, name="Tank Destroyer", cost=5)

    def target_select(self, roll, side, pips):
        if roll <= min(pips, 3):
            return TargetSelection(target_type="Unit Class", targets=["Vehicle"])

class LightTank(VehicleClass):
    def __init__(self):
        super().__init__(attack=3, defense=1, name="Light Tank", cost=4)
        self.blitz = Blitz(ratio=None)

class MediumTank(VehicleClass):
    def __init__(self):
        super().__init__(attack=6, defense=5, name="Medium Tank", cost=6)
        self.blitz = Blitz(ratio=None)

class T34(VehicleClass):
    def __init__(self):
        super().__init__(attack=6, defense=5, name="T-34", cost=5)
        self.blitz = Blitz(ratio=None)

    def target_select(self, roll, side, pips):
        if roll == 1:
            return TargetSelection(target_type="Unit Class", targets=["Vehicle"])

class HeavyTank(VehicleClass):
    def __init__(self):
        super().__init__(attack=8, defense=7, name="Heavy Tank", cost=7)
        self.blitz = Blitz(ratio=None)

    def target_select(self, roll, side, pips):
        if roll == 1:
            return TargetSelection(target_type="Unit Class", targets=["Vehicle"])

class TigerI(VehicleClass):
    def __init__(self):
        super().__init__(attack=8, defense=7, name="Tiger I", cost=7)
        self.blitz = Blitz(ratio=None)

    def target_select(self, roll, side, pips):
        if roll <= 3:
            return TargetSelection(target_type="Unit Class", targets=["Vehicle"])
