class ArmyResolver:
    def __init__(self, casualties, side, army, terrains, debug=False):
        self.casualties = casualties
        self.side = side
        self.army = army
        self.terrains = terrains
        self.debug = debug
        self.losses = []

    def bprint(self, string):
        if self.debug:
            print(string)

    # This method will remove losses using the specified strategy
    # return - remaining army
    def remove_losses():
        self.check_for_losses()
        self.handle_retreats()
        self.handle_strict_targets()
        self.handle_non_strict_targets()
        self.handle_standard_hits()
        return army

    def check_for_losses(self):
        # If no hits, return early
        if (self.casualties.hits + len(self.casualties.targets) +
                len(self.casualties.specific) + len(self.casualties.retreats)) == 0:
            return

        # If the total health available is less than the number of total hits, the army is done
        if sum([x.health for x in self.army.units]) <= (self.casualties.hits + \
                len([x for x in self.casualties.targets if x.strict is False]) + \
                len([x for x in self.casualties.specific if x.strict is False]) + \
                len(self.casualties.retreats)):
            self.army.units = []
            return 

    # This returns units who have > 1 max health in order of how damaged they are
    def get_multi_health_units(self):
        return sorted([x for x in self.army.units if x.name in ["Battleship", 
            "Heavy Battleship", "Fleet Carrier"]], key=lambda x: x.health)

    def get_single_health_units(self):
        return self.cost_sort(units=[x for x in self.army.units if x.health == 1])

    # Sorts units so that the most expensive is first in the list
    def cost_sort(self, units):
        return sorted(units, key=lambda x: x.get_cost(), reverse=True)

    def handle_standard_hits(self):
        pass

    ### Target Selection
    # 1. Handle attacker picked target selection
    # 2. Unit choice is Multi-Health Units, then weighted by battle pips + cost
    # 3. After that defender picked target selects are taken
    # 4. All hits that are unable to be applied are 
    def handle_non_strict_targets(self):
        targets = [x for x in self.casualties.targets if not x.strict]
        if len(targets) == 0:
            pass

        # Check to see if enough target selects exist to kill a multi-health
        # If they do, kill a multi-health unit, those are harder to do
        multi_health_units = self.get_multi_health_units()
        if len(multi_health_units) > 0 and len(targets) > 1:
            for mhu in multi_health_units:
                applies = [x for x in targets if x.applies(unit=mhu)]
                if len(applies) >= mhu.health:
                    self.losses.append(mhu)
                    for t in applies[:mhu.health]:
                        self.casualties.targets.remove(t)



    def handle_strict_targets(self):
        pass

    def handle_retreats(self):
        if len(self.casualties.retreats) == 0:
            return

        for retreat in self.casualties.retreats:
            self.bprint("{} ({}) retreats".format(self.side, retreat.name))
            self.army.units.remove(retreat)
