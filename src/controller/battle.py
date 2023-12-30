from copy import deepcopy
from random import randint

from exceptions import InvalidArmyException
from controller.resolver import ArmyResolver
from models.army import Army
from models.battle import Casualties
from models.stats import CombatStats, CombatResult
from models.terrain import Terrain

class Battle:
    def __init__(self, attacker, defender, terrains=[], log=False):
        if attacker is None or len(attacker.units) < 1:
            raise InvalidArmyException("Attacking army is None or contains no units!")
        if defender is None or len(defender.units) < 1:
            raise InvalidArmyException("Defending army is None or contains no units!")

        self.terrains = terrains
        self.stats = CombatStats()
        self.log = log
        self.runs = 1 if log else 1000

        self.starting_attacker = attacker
        self.starting_defender = defender

        # We keep these so we can filter them out of the stats
        self.total_retreats = []

    def do_battle(self):
        for i in range(0,self.runs):
            self.setup()
            self.first_strike()
            while not self.finished():
                self.roll_dice()
                self.handle_casualties()
                self.advance_round()
                self.cleanup()

        self.stats.print_summary()

    def setup(self):
        self.combat_round = 1
        self.attacker_casualties = Casualties()
        self.defender_casualties = Casualties()

        self.attacker = deepcopy(self.starting_attacker)
        self.defender = deepcopy(self.starting_defender)

    # This should eventually handle bombardments when we add those in
    def first_strike(self):
        attacker_first_strikes = [x for x in self.attacker.units if x.first_strike]
        defender_first_strikes = [x for x in self.defender.units if x.first_strike]

        if len(attacker_first_strikes) == 0 and len(defender_first_strikes) == 0:
            return

        self.bprint('===============================')
        self.bprint('First Strikes!')
        self.bprint('===============================')
        self.bprint('Simulating attacking units')
        for au in attacker_first_strikes:
            self.roll_unit_with_modifiers(unit=au, side='Attacker')

        self.bprint('--------------------------')
        self.bprint('Simulating defending units')
        for au in defender_first_strikes:
            self.roll_unit_with_modifiers(unit=au, side='Defender')

        # We immediately handle casualties so that they don't participate in combat
        # Also do cleanup to reset casualties so the units are not removed twice
        self.handle_casualties()
        self.cleanup()

    def get_valid_combat_units(self, side):
        if side == 'Attacker':
            return [x for x in self.attacker.units if self.combat_round != 1 or not x.first_strike]
        else:
            return [x for x in self.defender.units if self.combat_round != 1 or not x.first_strike]

    def roll_dice(self):
        self.bprint('===============================')
        self.bprint('Beginning Round ' + str(self.combat_round))
        self.bprint('===============================')
        self.bprint('Simulating attacking units')
        for au in self.get_valid_combat_units(side='Attacker'):
            self.roll_unit_with_modifiers(unit=au, side='Attacker')

        self.bprint('--------------------------')
        self.bprint('Simulating defending units')
        for au in self.get_valid_combat_units(side='Defender'):
            self.roll_unit_with_modifiers(unit=au, side='Defender')

    def roll_unit(self, unit, side, facilities):
        if side == "Attacker":
            pips = unit.get_attack(terrains=self.terrain, combat_round=self.combat_round,
                    facilities=facilities)
            casualties = self.attacker_casualties
        else:
            pips = unit.get_defense(terrains=self.terrain, combat_round=self.combat_round,
                    facilities=facilities)
            casualties = self.defender_casualties

        roll = randint(1,12)


    def roll_unit_with_modifiers(self, unit, side):
        if side == 'Attacker':
            pips = unit.get_attack(terrains=self.terrains, combat_round=self.combat_round)
        else:
            pips = unit.get_defense(terrains=self.terrains, combat_round=self.combat_round)

        roll = randint(1,12)
        if roll <= pips:
            word = ' hits '
            target_select = unit.target_select(roll=roll, pips=pips, side=side)
            if side == 'Attacker':
                if target_select is not None:
                    self.defender_casualties.add_target(target=target_select)
                else:
                    self.defender_casualties.hits += 1
            else:
                if target_select is not None:
                    self.attacker_casualties.add_target(target=target_select)
                else:
                    self.attacker_casualties.hits += 1
        else:
            word = ' misses '
            if unit.does_retreat(side=side, roll=roll):
                word += 'and retreats '
                self.total_retreats.append(unit)
                self.attacker_casualties.retreats.append(unit)

        self.bprint(side + ' ' + unit.name + word + 'with a roll of ' + str(roll) +
                ' (needed ' + str(pips) + ' or less to hit)')

    def handle_casualties(self):
        defense_resolver = ArmyResolver(casualties=self.defender_casualties,
            side='Defender', army=self.defender, terrains=self.terrains)
        attack_resolver = ArmyResolver(casualties=self.attacker_casualties,
            side='Attack', army=self.attacker, terrains=self.terrains)

        self.attacker = attack_resolver.remove_losses()
        self.defender = defense_resolver.remove_losses()

    def cleanup(self):
        self.attacker_casualties = Casualties()
        self.defender_casualties = Casualties()

    def advance_round(self):
        self.combat_round += 1

    def finished(self):
        if len(self.attacker.units) == 0 or len(self.defender.units) == 0:
            self.bprint('-=-=-=-=-=-=-=-=-=-=-=-')
            if len(self.attacker.units) == 0:
                self.bprint('Defender Wins with ' + str(len(self.defender.units)) + ' troops remaining')
                self.record_stats(winner='Defender')
            else:
                self.bprint('Attacker Wins with ' + str(len(self.attacker.units)) + ' troops remaining')
                self.record_stats(winner='Attacker')
            return True
        else:
            return False

    def record_stats(self, winner):
        if winner == 'Attacker':
            ipp_killed = sum([x.get_cost() for x in self.starting_defender.units])
            ipp_lost = sum([x.get_cost() for x in self.starting_attacker.units 
                if x not in self.attacker.units or self.attacker.units.remove(x)])
        else:
            ipp_killed = sum([x.get_cost() for x in self.starting_attacker.units
                if x not in self.total_retreats or self.total_retreats.remove(x)])
            ipp_lost = sum([x.get_cost() for x in self.starting_defender.units 
                if x not in self.defender.units or self.defender.units.remove(x)])

        result = CombatResult(winner=winner, ipp_killed=ipp_killed, ipp_lost=ipp_lost)
        self.stats.add_result(result=result)

    def sorted_units(self, units):
        return sorted(units, key = lambda x: (x.get_total_pips(), x.get_cost()))

    def bprint(self, s):
        if self.log == True:
            print(s)

