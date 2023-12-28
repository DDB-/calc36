class ArmyResolver:
    def __init__(self, casualties, side, army, terrains=[], debug=False):
        self.casualties = casualties
        self.side = side
        self.army = army
        self.terrains = terrains
        self.debug = debug
        self.losses = []
        self.total_losses = []

    def bprint(self, string):
        if self.debug:
            print(string)

    # This method will remove losses using the specified strategy
    # return - remaining army
    def remove_losses(self):
        state = self.check_for_losses()
        if state == 0:
            self.handle_retreats()
            self.handle_strict_targets()
            self.handle_non_strict_targets()
            self.handle_standard_hits()
        elif state == -1:
            self.bprint("No hits this round")
        elif state == 1:
            self.bprint("All units destroyed")

        return self.army

    def do_removal(self):
        for unit in self.losses:
            self.bprint("{} ({}) is killed".format(self.side, unit.name))
            self.army.units.remove(unit)

        # Record total losses and then reset -- allows this function to be called multiple times
        self.total_losses.extend(self.losses)
        self.losses = []

    def check_for_losses(self):
        # If no hits, return early
        if (self.casualties.hits + len(self.casualties.targets) +
                len(self.casualties.specific) + len(self.casualties.retreats)) == 0:
            return -1

        # If the total health available is less than the number of total hits, the army is done
        if sum([x.health for x in self.army.units]) <= (self.casualties.hits + \
                len([x for x in self.casualties.targets if x.strict is False]) + \
                len([x for x in self.casualties.specific if x.strict is False]) + \
                len(self.casualties.retreats)):
            self.army.losses = self.army.units
            self.army.units = []
            return 1

        return 0

    # This returns units who have > 1 max health in order of how damaged they are
    def get_multi_health_units(self):
        return sorted([x for x in self.army.units if x.health > 1], reverse=True, 
            key=lambda x: (x.health, -x.get_cost()))

    def get_single_health_units(self):
        return sorted([x for x in self.army.units if x.health == 1], reverse=True,
            key=lambda x: (x.get_weight(side=self.side, terrains=self.terrains)))

    # Sorts units so that the most expensive is first in the list
    def cost_sort(self, units):
        return sorted(units, key=lambda x: x.get_cost(), reverse=True)

    def handle_standard_hits(self):
        if self.casualties.hits == 0:
            return

        multi = self.get_multi_health_units()
        while len(multi) > 0 and self.casualties.hits > 0:
            multi[0].health -= 1
            self.casualties.hits -= 1
            multi = self.get_multi_health_units()

        if self.casualties.hits == 0:
            return

        # This is sorted so that the worst units are at the end
        units = self.get_single_health_units()
        self.losses.extend(units[-self.casualties.hits:])
        self.do_removal()

    ### Target Selection
    # 1. Handle attacker picked target selection
    # 2. Unit choice is Multi-Health Units, then weighted by battle pips + cost
    # 3. After that defender picked target selects are taken
    # 4. All hits that are unable to be applied are 
    def handle_non_strict_targets(self):
        targets = [x for x in self.casualties.targets if not x.strict]
        if len(targets) == 0:
            return

        # Check to see if enough target selects exist to kill a multi-health
        # If they do, kill a multi-health unit, those are harder to do
        #multi_health_units = self.get_multi_health_units()
        #if len(multi_health_units) > 0 and len(targets) > 1:
        #    for mhu in multi_health_units:
        #        applies = [x for x in targets if x.applies(unit=mhu)]
        #        if len(applies) >= mhu.health:
        #            self.losses.append(mhu)
        #            for t in applies[:mhu.health]:
        #                self.casualties.targets.remove(t)

        # Handle target selections one at a time, and do the removal immediately
        for target in targets:
            applies = sorted([x for x in self.army.units if target.applies(unit=x)], reverse=True,
                key=lambda x: (x.get_weight(side=self.side, terrains=self.terrains)))
            if len(applies) > 0:
                # True target selects hit highest weight else specific hits target lowest weight
                index = 0 if target.expensive else -1
                self.losses.append(applies[index])
                # Immediately process the removal so that the next applies doesn't consider it
                self.do_removal()
            else:
                # If there are no valid targets, it gets downgraded to a normal hit
                # Normal hits are handled last before final cleanup
                self.casualties.hits += 1

    def handle_strict_targets(self):
        pass

    def handle_retreats(self):
        if len(self.casualties.retreats) == 0:
            return

        for retreat in self.casualties.retreats:
            self.bprint("{} ({}) retreats".format(self.side, retreat.name))
            self.army.units.remove(retreat)
