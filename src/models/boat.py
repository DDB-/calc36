from models.base_unit import BoatClass

class TorpedoBoatDestroyer(BoatClass):
    def __init__(self):
        super().__init__(attack=2, defend=2, name="Torpedo Boat Destroyer", cost=0, movement=2)

class Destroyer(BoatClass):
    def __init__(self):
        super().__init__(attack=4, defend=4, name="Destroyer", cost=7, movement=3)

class CoastalDefenseShip(BoatClass):
    def __init__(self):
        # Cost is fake, is an approximation of what they provide
        super().__init__(attack=4, defend=6, name="Coastal Defense Ship", cost=0)
        self.bombard = 2

class LightCruiser(BoatClass):
    def __init__(self):
        super().__init__(attack=5, defend=5, name="Light Cruiser", cost=9, movement=3)

    def target_select(self, roll, side, pips):
        if roll =< min(pips, 3):
            return TargetSelection(target_type="Unit Class", targets=["Plane"])

class HeavyCruiser(BoatClass):
    def __init__(self):
        super().__init__(attack=6, defend=6, name="Heavy Cruiser", cost=[5,5], movement=3)
        self.bombard = 2

class Battlecruiser(BoatClass):
    def __init__(self):
        super().__init__(attack=7, defend=7, name="Battlecruiser", cost=[7,7], movement=3)
        self.bombard = 3

# Health can be set in case we want to initialize a damaged Battleship
class Battleship(BoatClass):
    def __init__(self, health=2):
        super().__init__(attack=8, defend=8, name="Battleship", cost=[6,6,6], movement=2)
        self.bombard = 4
        self.health = max(min(health, 2), 1) # Ensure health is between 1-2

    def health_adjustment(self):
        return (self.health - 2) * 2

# Health can be set in case we want to initialize a damaged Heavy Battleship
class HeavyBattleship(BoatClass):
    def __init__(self, health=3):
        super().__init__(attack=10, defend=10, name="Heavy Battleship", cost=[7,7,7], movement=3)
        self.bombard = 4
        self.health = max(min(health, 3), 1) # Ensure health is between 1-3

    def health_adjustment(self):
        return (self.health - 3) * 2

class LightCarrier(BoatClass):
    def __init__(self):
        super().__init__(attack=0, defend=1, name="Light Carrier", cost=[4,4], movement=3)

class FleetCarrier(BoatClass):
    def __init__(self, health=2):
        super().__init__(attack=0, defend=2, name="Fleet Carrier", cost=[5,5,5], movement=3)
        self.health = max(min(health, 2), 1) # Ensure health is between 1-2

    def health_movement_adjustment(self):
        return -2 if self.health < 2 else 0

class HeavyFleetCarrier(BoatClass):
    def __init__(self, health=2):
        super().__init__(attack=0, defend=2, name="Heavy Fleet Carrier", cost=[6,6,6], movement=3)
        self.health = max(min(health, 2), 1) # Ensure health is between 1-2

    def health_movement_adjustment(self):
        return -2 if self.health < 2 else 0

class CoastalSubmarine(BoatClass):
    def __init__(self):
        super().__init__(attack=2, defend=2, name="Coastal Submarine", cost=0, movement=1)

    def target_select(self, roll, side, pips):
        if roll == 1:
            return TargetSelection(target_type="Unit Name", targets=["Torpedo Boat Destroyer",
                "Destroyer", "Coastal Defense Ship", "Light Cruiser", "Heavy Cruiser",
                "Battlecruiser", "Battleship", "Heavy Battleship", "Light Carrier",
                "Fleet Carrier", "Heavy Fleet Carrier", "Naval Transport", "Attack Transport"])

class Submarine(BoatClass):
    def __init__(self):
        super().__init__(attack=3, defend=3, name="Submarine", cost=6, movement=3)

    def target_select(self, roll, side, pips):
        if roll == 1:
            return TargetSelection(target_type="Unit Name", targets=["Torpedo Boat Destroyer",
                "Destroyer", "Coastal Defense Ship", "Light Cruiser", "Heavy Cruiser",
                "Battlecruiser", "Battleship", "Heavy Battleship", "Light Carrier",
                "Fleet Carrier", "Heavy Fleet Carrier", "Naval Transport", "Attack Transport"])

class AdvancedSubmarine(BoatClass):
    def __init__(self):
        super().__init__(attack=4, defend=4, name="Advanced Submarine", cost=7, movement=3)

    def target_select(self, roll, side, pips):
        if roll == 1:
            return TargetSelection(target_type="Unit Name", targets=["Torpedo Boat Destroyer",
                "Destroyer", "Coastal Defense Ship", "Light Cruiser", "Heavy Cruiser",
                "Battlecruiser", "Battleship", "Heavy Battleship", "Light Carrier",
                "Fleet Carrier", "Heavy Fleet Carrier", "Naval Transport", "Attack Transport"])

class NavalTransport(BoatClass):
    def __init__(self):
        super().__init__(attack=0, defend=0, name="Naval Transport", cost=7, movement=2)

class AttackTransport(BoatClass):
    def __init__(self):
        super().__init__(attack=0, defend=1, name="Attack Transport", cost=7, movement=2)
