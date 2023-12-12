#!/usr/bin/env python3

import models.infantry as infantry
from models.army import Army
from models.terrain import Mountain
from controller.battle import Battle

print("Basic testing of ideas in this file, not to be the actual main")
army = Army()
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.add_unit(infantry.Infantry())
army.apply_nation(nation="KMT")

defense = Army()
defense.add_unit(infantry.Infantry())
defense.add_unit(infantry.Infantry())
defense.add_unit(infantry.Infantry())
defense.add_unit(infantry.Infantry())
defense.add_unit(infantry.Infantry())
defense.add_unit(infantry.Infantry())
defense.apply_nation(nation="CCP")

terrain = Mountain()

battle = Battle(attacker=army, defender=defense, terrain=terrain)
battle.do_battle()
