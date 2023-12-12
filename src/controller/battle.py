from copy import deepcopy
from random import randint

from exceptions import InvalidArmyException
from models.army import Army
from models.stats import CombatStats, CombatResult
from models.terrain import Terrain

class Battle:
    def __init__(self, attacker, defender, terrain=None):
        if attacker is None or len(attacker.units) < 1:
            raise InvalidArmyException("Attacking army is None or contains no units!")
        if defender is None or len(defender.units) < 1:
            raise InvalidArmyException("Defending army is None or contains no units!")
        if terrain is None:
            self.terrain = Terrain() 
        else:
            self.terrain = terrain

        self.stats = CombatStats()
        self.log = False

        self.starting_attacker = self.sorted_units(units=attacker.units)
        self.starting_defender = self.sorted_units(units=defender.units)


    def do_battle(self):
        for i in range(1,10000):
            self.setup()
            while not self.finished():
                self.roll_dice()
                self.handle_retreats()
                self.handle_losses()
                self.advance_round()
                self.cleanup()

        self.stats.print_summary()

    def setup(self):
        self.combat_round = 1
        self.attacker_losses = 0
        self.defender_losses = 0

        # Target selections should be a list of Units or Unit Classes to take the most valubale of
        self.attacker_target_selections = []
        self.defender_target_selections = []

        # Only the attacker can be forced to retreat via rules
        self.total_retreats = []
        self.attacker_retreats = []

        self.attacker = deepcopy(self.starting_attacker)
        self.defender = deepcopy(self.starting_defender)

    def roll_dice(self):
        self.bprint("===============================")
        self.bprint("Beginning Round " + str(self.combat_round))
        self.bprint("===============================")
        self.bprint("Simulating attacking units")
        for au in self.attacker:
            self.roll_unit_with_modifiers(unit=au, side="Attacker")

        self.bprint("--------------------------")
        self.bprint("Simulating defending units")
        for au in self.defender:
            self.roll_unit_with_modifiers(unit=au, side="Defender")

    def handle_retreats(self):
        if len(self.attacker_retreats) > 0:
            self.total_retreats.extend(self.attacker_retreats)
            self.bprint("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for unit in self.attacker_retreats:
                self.bprint("Attacker retreats: " + unit.get_name())
                self.attacker.remove(unit)

        # Always reset the retreats each round no matter what to be consistent
        self.attacker_retreats = []

    def handle_losses(self):
        if (self.attacker_losses > 0):
            self.bprint("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for unit in self.attacker[0:self.attacker_losses]:
                self.bprint("Attacker loses: " + unit.get_name())
            self.attacker = self.attacker[self.attacker_losses:]

        if (self.defender_losses > 0):
            self.bprint("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for unit in self.defender[0:self.defender_losses]:
                self.bprint("Defender loses: " + unit.get_name())
            self.defender = self.defender[self.defender_losses:]

    def roll_unit_with_modifiers(self, unit, side):
        if side == "Attacker":
            pips = unit.get_attack(terrain=self.terrain, combat_round=self.combat_round)
        else:
            pips = unit.get_defense(terrain=self.terrain, combat_round=self.combat_round)

        roll = randint(1,12)
        if roll <= pips:
            word = " hits "
            target_select = unit.target_select(roll=roll, pips=pips, side=side):
            if side == "Attacker":
                if target_select is not None:
                    self.defender_target_selections.append(target_select)
                else:
                    self.defender_losses += 1
            else:
                if target_select is not None:
                    self.attacker_target_selections.append(target_select)
                else:
                    self.attacker_losses += 1
        else:
            word = " misses "
            if unit.does_retreat(side=side, roll=roll):
                word += "and retreats "
                self.attacker_retreats.append(unit)

        self.bprint(side + " " + unit.get_name() + word + "with a roll of " + str(roll) +
                " (needed " + str(pips) + " or less to hit)")

    def cleanup(self):
        self.attacker_losses = 0
        self.defender_losses = 0

    def advance_round(self):
        self.combat_round += 1

    def finished(self):
        if len(self.attacker) == 0 or len(self.defender) == 0:
            self.bprint("-=-=-=-=-=-=-=-=-=-=-=-")
            if len(self.attacker) == 0:
                self.bprint("Defender Wins with " + str(len(self.defender)) + " troops remaining")
                self.record_stats(winner="Defender")
            else:
                self.bprint("Attacker Wins with " + str(len(self.attacker)) + " troops remaining")
                self.record_stats(winner="Attacker")
            return True
        else:
            return False

    def record_stats(self, winner):
        if winner == "Attacker":
            ipp_killed = sum([x.get_cost() for x in self.starting_defender])
            ipp_lost = sum([x.get_cost() for x in self.starting_attacker 
                if x not in self.attacker or self.attacker.remove(x)])
        else:
            ipp_killed = sum([x.get_cost() for x in self.starting_attacker
                if x not in self.total_retreats or self.total_retreats.remove(x)])
            ipp_lost = sum([x.get_cost() for x in self.starting_defender 
                if x not in self.defender or self.defender.remove(x)])

        result = CombatResult(winner=winner, ipp_killed=ipp_killed, ipp_lost=ipp_lost)
        self.stats.add_result(result=result)


    def sorted_units(self, units):
        return sorted(units, key = lambda x: (x.get_total_pips(), x.get_cost()))

    def bprint(self, s):
        if self.log == True:
            print(s)

