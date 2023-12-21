from models.base_units import PlaneClass
from models.unit_mods import Blitz, OneRound

class Fighter(PlaneClass):
    def __init__(self):
        super().__init__(attack=6, defense=6, name="Fighter", cost=10)
        self.air_superiority = True
        self.blitz = Blitz(ratio=1)

class JetFighter(PlaneClass):
    def __init__(self):
        super().__init__(attack=8, defense=8, name="Jet Fighter", cost=12)
        self.air_superiority = True
        self.blitz = Blitz(ratio=1)

class TacticalBomber(PlaneClass):
    def __init__(self):
        super().__init__(attack=7, defense=5, name="Tactical Bomber", cost=11)
        self.blitz = Blitz(ratio=1)

    def target_select(self, roll, side, pips):
        if roll <= min(pips, 3):
            return TargetSelection(target_type="Unit Class", targets=["Vehicle",
                "Infantry", "Artillery", "Boat"])

class MediumBomber(PlaneClass):
    def __init__(self):
        super().__init__(attack=7, defense=4, name="Medium Bomber", cost=11)

class StrategicBomber(PlaneClass):
    def __init__(self):
        super().__init__(attack=2, defense=2, name="Strategic Bomber", cost=12)
        self.one_round = OneRound(repeat=3, sides=["Attacker"])

class HeavyStrategicBomber(PlaneClass):
    def __init__(self):
        super().__init__(attack=2, defense=3, name="Heavy Strategic Bomber", cost=13)
        self.one_round = OneRound(repeat=5, sides=["Attacker"])

class Seaplane(PlaneClass):
    def __init__(self):
        super().__init__(attack=3, defense=3, name="Seaplane", cost=7)
        self.eligible_casualties = ["Naval Transport", "Attack Transport", "Submarine", "Coastal Submarine"]

class AirTransport(PlaneClass):
    def __init__(self):
        super().__init__(attack=0, defense=0, name="Air Transport", cost=8)
        self.selection_priority = -999

class HeavyAirTransport(PlaneClass):
    def __init__(self):
        super().__init__(attack=0, defense=0, name="Heavy Air Transport", cost=10)
        self.selection_priority = -999
