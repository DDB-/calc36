from exceptions import InvalidPipsException, MissingCostException

class Unit:
    def __init__(self, attack, defense, cost=None, name=None, 
            unit_class=None, modifiers=None, health=1, nation=None):
        self.attack = attack
        self.defense = defense
        if self.attack > 12 or self.attack < 0:
            raise InvalidPipsException("Attack pips must be between 0 and 12")

        if self.defense > 12 or self.defense < 0:
            raise InvalidPipsException("Defense pips must be between 0 and 12")

        self.cost = cost
        self.name = name
        self.unit_class = unit_class
        self.modifiers = modifiers
        self.health = health
        self.nation = nation
        self.blitz = None
        self.first_strike = False
        self.air_superiority = False
        self.one_round = None
        self.eligible_casualties = None
        self.selection_priority = 0

    def __eq__(self, other):
        return self.name == other.name

    def get_attack(self, terrain, combat_round):
        if terrain is not None:
            return max(self.attack + terrain.get_modifier(unit=self, 
                    combat_round=combat_round, side="Attacker"), 1)

        return self.attack

    def get_defense(self, terrain, combat_round):
        if terrain is not None:
            return max(self.defense + terrain.get_modifier(unit=self, 
                    combat_round=combat_round, side="Defense"), 1)

        return self.defense

    def get_total_pips(self):
        return self.defense + self.attack

    def get_name(self):
        if self.name is not None:
            return self.name

        return "Base Class: " + self.__class__.__name__

    def get_unit_class(self):
        if self.unit_class is not None:
            return self.unit_class

        return "Base Unit (Did you return this in error?)"

    def get_cost(self):
        if self.cost is not None:
            return self.cost

        raise MissingCostException("Only specific Unit types have a cost, and this is a " +
                self.__class__.__name__)

    def does_retreat(self, side, roll):
        return False

    def target_select(self, roll, side, pips):
        return None



# Four main types of units:
#   * Infantry (anything that walks around)
#   * Vehicle (anything with wheels on the ground)
#   * Artillery (anything that can first strike)
#   * Boat (anything in the water)
#   * Plane (anything in the air)
class InfantryClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, nation=None):
        super().__init__(attack=attack, defense=defense, unit_class="Infantry", 
                name=name, cost=cost, nation=nation)

class VehicleClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, nation=None):
        super().__init__(attack=attack, defense=defense, unit_class="Vehicle",
                name=name, cost=cost, nation=nation)

class ArtilleryClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, nation=None):
        super().__init__(attack=attack, defense=defense, unit_class="Artillery",
                name=name, cost=cost, nation=nation)
        self.first_strike = True

class BoatClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, health=1, nation=None):
        super().__init__(attack=attack, defense=defense, unit_class="Boat",
                name=name, cost=cost, health=health, nation=nation)

class PlaneClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, nation=None):
        super().__init__(attack=attack, defense=defense, unit_class="Plane",
                name=name, cost=cost, nation=nation)
