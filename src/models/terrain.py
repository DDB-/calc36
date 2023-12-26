class Terrain:
    def get_modifier(self, unit, combat_round, side):
        return 0

class Jungle(Terrain):
    def get_modifer(self, unit, combat_round, side):
        if side == "Attacker" and unit.name == "Gurkha":
            return 1
        elif unit.unit_class == "Vehicle":
            return -2

        return 0

class Desert(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Attacker":
            if unit.name == "Foreign Legion":
                return 1
            elif unit.unit_class == "Infantry" and unit.nation != "DAK":
                return -1

        return 0

class Marsh(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if unit.unit_class == "Vehicle":
            return -2

        return 0

class Mountain(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Attacker":
            if unit.unit_class == "Infantry" and  \
            (unit.name != "Mountain Infantry" or unit.name != "Foreign Legion"):
                return -1
        elif side == "Defender":
            if unit.name == "Mountain Infantry":
                return 1

        return 0

class River(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Attacker" and combat_round == 1:
            if unit.unit_class == "Infantry" or unit.unit_class == "Vehicle":
                if unit.name != "Marine" or unit.name != "Airborne Infantry" or unit.name != "Artillery" or unit.name != "Advanced Artillery":
                    return -1

        return 0

class City(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Defender" and unit.unit_class == "Infantry":
            # TODO: Also target selection on 1 against vehicle class
            return 1
        
        return 0

class SurroundedCity(Terrain):
    def get_modifier(self, unit, combat_round, side):
        if side == "Defender":
            return -1

        return 0
