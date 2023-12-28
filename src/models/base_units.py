from exceptions import InvalidPipsException, MissingCostException

class Unit:
    def __init__(self, attack, defense, cost=None, name=None, unit_class=None,
            modifiers=None, nation=None, movement=1):
        self.attack = attack
        self.defense = defense

        # TODO: Move validation into its own method at some point
        if self.attack > 12 or self.attack < 0:
            raise InvalidPipsException("Attack pips must be between 0 and 12")

        if self.defense > 12 or self.defense < 0:
            raise InvalidPipsException("Defense pips must be between 0 and 12")

        self.cost = cost
        self.name = name
        self.unit_class = unit_class
        self.modifiers = modifiers
        self.nation = nation
        self.movement = movement
        self.health = 1
        self.blitz = None
        self.first_strike = False
        self.air_superiority = False
        self.one_round = None
        self.eligible_casualties = None
        self.selection_priority = 0
        self.bombard = None

    def __eq__(self, other):
        return self.name == other.name

    def get_attack(self, terrains=[], combat_round=0):
        # First account for damage taken if it has health and still alive
        local_attack = self.attack + self.health_adjustment()

        # Next account for terrains, taking the best bonus
        # available, and the worst negative, and combining for final adjustment
        terrain_mod, tmax, tmin = 0, 0, 0
        if len(terrains) > 0:
            terrain_modifiers = [terrain.get_modifier(unit=self, combat_round=combat_round,
                side="Attacker") for terrain in terrains]
            tmax = max(0, max(terrain_modifiers))
            tmin = min(0, min(terrain_modifiers))
            terrain_mod = tmax + tmin

        return max(local_attack + terrain_mod, 1)

    def get_defense(self, terrains=[], facilities=[], combat_round=0):
        # First account for damage taken if it has health and still alive
        local_defense = self.defense + self.health_adjustment()

        # Next account for terrains, taking the best bonus
        # available, and the worst negative, and combining for final adjustment
        terrain_mod, tmax, tmin = 0, 0, 0
        if len(terrains) > 0:
            terrain_modifiers = [terrain.get_modifier(unit=self, combat_round=combat_round,
                side="Defender") for terrain in terrains]
            tmax = max(0, max(terrain_modifiers))
            tmin = min(0, min(terrain_modifiers))

        # Next account for facilities if they help at all, taking best combing with terrain
        if len(facilities) > 0:
            facility_modifiers = [facility.get_defense_bonus(unit=self, combat_round=combat_round)]
            tmax = max(tmax, max(facility_modifiers))

        terrain_mod = tmax + tmin
        return max(local_defense + terrain_mod, 1)

    def health_adjustment(self):
        return 0

    def health_movement_adjustment(self):
        return 0

    def get_total_pips(self):
        return self.defense + self.attack

    def get_cost(self):
        if self.cost is not None:
            if type(self.cost) is int:
                return self.cost
            elif type(self.cost) is list:
                return sum(self.cost)

        raise MissingCostException("Only specific Unit types have a cost, and this is a " +
                self.__class__.__name__)

    def get_weight(self, side, terrains=[], facilities=[]):
        weight = self.get_cost()
        if side == "Attacker":
            weight += self.get_attack(terrains=terrains)
        else:
            weight += self.get_defense(terrains=terrains, facilities=facilities)

        if self.first_strike:
            weight += 1

        if self.blitz is not None:
            weight += 1

        return weight

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
    def __init__(self, attack, defense, name=None, cost=None, nation=None, movement=1):
        super().__init__(attack=attack, defense=defense, unit_class="Infantry", 
                name=name, cost=cost, nation=nation, movement=movement)

class VehicleClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, nation=None, movement=1):
        super().__init__(attack=attack, defense=defense, unit_class="Vehicle",
                name=name, cost=cost, nation=nation, movement=movement)

class ArtilleryClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, nation=None, movement=1):
        super().__init__(attack=attack, defense=defense, unit_class="Artillery",
                name=name, cost=cost, nation=nation, movement=movement)
        self.first_strike = True

class BoatClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, nation=None, movement=1):
        super().__init__(attack=attack, defense=defense, unit_class="Boat",
                name=name, cost=cost, nation=nation, movement=movement)

class PlaneClass(Unit):
    def __init__(self, attack, defense, name=None, cost=None, nation=None, movement=1):
        super().__init__(attack=attack, defense=defense, unit_class="Plane",
                name=name, cost=cost, nation=nation, movement=movement)
