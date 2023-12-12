from exceptions import MissingCostException

class Army:
    def __init__(self, units=None):
        if units is None:
            self.units = []
        else:
            self.units = units

    def add_unit(self, unit):
        try:
            unit.get_cost()
            self.units.append(unit)
        except MissingCostException:
            print("Ignoring unit: '" + unit.get_name() + "'")

    # This gets you the least expensive units first
    def sorted_units(self):
        sorted_units = sorted(self.units, key = lambda x: (x.get_total_pips(), x.get_cost()))
        return sorted_units

    def apply_nation(self, nation, exclude=None):
        # [u for u in self.nation if not u in exclude or exclude.remove(u)]
        for unit in self.units:
            unit.nation = nation
