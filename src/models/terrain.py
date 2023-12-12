class Terrain:
    def get_modifier(self, unit, combat_round, side):
        return 0

class Jungle(Terrain):
    def get_modifer(self, unit, combat_round, side):
        if side == "Attacker" and unit.get_name() == "Gurkha":
            return 1
        elif unit.get_unit_class() == "Vehicle":
            return -2

        return 0

class Desert(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Attacker":
            if unit.get_name() == "Foreign Legion":
                return 1
            elif unit.get_unit_class() == "Infantry" and unit.nation != "DAK":
                return -1

        return 0

class Marsh(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if unit.get_unit_class() == "Vehicle":
            return -2

        return 0

class Mountain(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Attacker":
            if unit.get_unit_class() == "Infantry" and  \
            (unit.get_name() != "Mountain Infantry" \
                    or unit.get_name() != "Foreign Legion"):
                return -1
        elif side == "Defender":
            if unit.get_name() == "Mountain Infantry":
                return 1

        return 0

class River(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Attacker" and combat_round == 1:
            if unit.get_unit_class() == "Infantry" or unit.get_unit_class() == "Vehicle":
                unit_name = unit.get_name()
                if unit_name != "Marine" or unit_name != "Airborne Infantry" or unit_name != "Artillery" or unit_name != "Advanced Artillery":
                    return -1

        return 0

class City(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Defender" and unit.get_unit_class() == "Infantry":
            # TODO: Also target selection on 1 against vehicle class
            return 1
        
        return 0

class SurroundedCity(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Defender":
            return -1

        return 0
