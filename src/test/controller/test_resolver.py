from controller.resolver import ArmyResolver
from models.army import Army
from models.battle import Casualties

import models.artillery as artillery
import models.boat as boat
import models.infantry as infantry
import models.plane as plane
import models.vehicles as vehicles

###############################
######## Standard Hits ########
###############################

def test_get_units_of_health():
    units = [infantry.Infantry(), infantry.Militia(), boat.Battleship()]
    army = Army(units=units) 
    casualties = Casualties()

    ar = ArmyResolver(casualties=casualties, side='Attacker', army=army, terrains=[])
    assert len(ar.get_single_health_units()) == 2
    assert len(ar.get_multi_health_units()) == 1

def test_empty_resolve():
    units = [infantry.Infantry(), infantry.Militia(), infantry.MountainInfantry()] 
    army = Army(units=units) 
    casualties = Casualties()

    ar = ArmyResolver(casualties=casualties, side='Attacker', army=army, terrains=[])
    new_army = ar.remove_losses()

    assert len(new_army.units) == 3

def test_single_hit_removed():
    units = [infantry.Infantry(), infantry.Militia(), infantry.MountainInfantry()] 
    army = Army(units=units) 
    casualties = Casualties()
    casualties.hits = 1

    ar = ArmyResolver(casualties=casualties, side='Attacker', army=army, terrains=[])
    new_army = ar.remove_losses()

    # One unit should be removed and it should be the Militia
    assert len(new_army.units) == 2
    assert new_army.units == [infantry.Infantry(), infantry.MountainInfantry()]
    assert ar.losses == [infantry.Militia()]

def test_multiple_hits_removed():
    units = [infantry.Infantry(), infantry.Infantry(), infantry.Militia(), 
        infantry.MountainInfantry()] 
    army = Army(units=units) 
    casualties = Casualties()
    casualties.hits = 3

    ar = ArmyResolver(casualties=casualties, side='Attacker', army=army, terrains=[])
    new_army = ar.remove_losses()
    assert len(new_army.units) == 1
    assert new_army.units == [infantry.MountainInfantry()]
    assert ar.cost_sort(units=ar.losses) == \
        ar.cost_sort(units=[infantry.Militia(), infantry.Infantry(), infantry.Infantry()])

def test_single_hit_with_multi_health_unit():
    units = [infantry.Infantry(), infantry.Militia(), boat.Battleship()]
    army = Army(units=units) 
    casualties = Casualties()
    casualties.hits = 1

    ar = ArmyResolver(casualties=casualties, side='Defender', army=army, terrains=[])
    army = ar.remove_losses()
    assert len(army.units) == 3
    assert len(ar.losses) == 0
    assert army.units[2].health == 1
    assert army.units[2].name == "Battleship"

def test_multi_hit_multi_health_units():
    units = [infantry.Infantry(), infantry.Militia(), boat.Battleship(),
        boat.HeavyBattleship(), boat.FleetCarrier()]
    army = Army(units=units) 
    casualties = Casualties()
    casualties.hits = 3

    ar = ArmyResolver(casualties=casualties, side='Defender', army=army, terrains=[])
    army = ar.remove_losses()
    # No losses, as with 3 hits, the HB should take 1, FC takes 1, and BS takes 1
    assert len(army.units) == 5
    assert len(ar.losses) == 0
    assert army.units[2].health == 1
    assert army.units[2].name == "Battleship"
    assert army.units[3].health == 2
    assert army.units[3].name == "Heavy Battleship"
    assert army.units[4].health == 1
    assert army.units[4].name == "Fleet Carrier"

def test_multi_hit_multi_health_casualties():
    units = [infantry.Infantry(), infantry.Militia(), boat.Battleship()]
    army = Army(units=units) 
    casualties = Casualties()
    casualties.hits = 2

    ar = ArmyResolver(casualties=casualties, side='Defender', army=army, terrains=[])
    army = ar.remove_losses()
    assert len(army.units) == 2
    assert len(ar.losses) == 1
    assert army.units[1].health == 1
    assert army.units[1].name == "Battleship"

def test_complex_army_resolve_normal_hits():
    units = [infantry.Infantry(), infantry.Infantry(), infantry.MountainInfantry(),
        artillery.Artillery(), artillery.Artillery(),
        vehicles.LightTank(), vehicles.MediumTank(),
        plane.Fighter()]
    army = Army(units=units) 
    casualties = Casualties()
    casualties.hits = 4

    ar = ArmyResolver(casualties=casualties, side='Defender', army=army, terrains=[])
    army = ar.remove_losses()
    assert len(army.units) == 4
    assert len(ar.losses) == 4

    expected_remaining = [artillery.Artillery(), infantry.MountainInfantry(), 
        vehicles.MediumTank(), plane.Fighter()]
    assert sorted(army.units, key=lambda x: x.name) == \
        sorted(expected_remaining, key=lambda x: x.name)
