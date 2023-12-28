import models.artillery as artillery
import models.boat as boat
import models.infantry as infantry
import models.plane as plane
import models.vehicles as vehicles

import models.terrain as terrain

def test_infantry():
    inf = infantry.Infantry()
    assert inf.get_cost() == 3
    assert inf.get_attack() == 2
    assert inf.get_defense() == 4
    assert inf.health == 1
    assert inf.name == "Infantry"
    assert inf.unit_class == "Infantry"
    assert inf.blitz == None
    assert inf.bombard == None
    assert inf.first_strike == False
    assert inf.air_superiority == False

def test_vehicle():
    tank = vehicles.MediumTank()
    assert tank.get_cost() == 6
    assert tank.get_attack() == 6
    assert tank.get_defense() == 5
    assert tank.health == 1
    assert tank.name == "Medium Tank"
    assert tank.unit_class == "Vehicle"
    assert tank.blitz != None
    assert tank.bombard == None
    assert tank.first_strike == False
    assert tank.air_superiority == False

def test_artillery():
    art = artillery.Artillery()
    assert art.get_cost() == 4
    assert art.get_attack() == 3
    assert art.get_defense() == 3
    assert art.health == 1
    assert art.name == "Artillery"
    assert art.unit_class == "Artillery"
    assert art.blitz == None
    assert art.bombard == None
    assert art.first_strike == True
    assert art.air_superiority == False

def test_plane():
    fighter = plane.Fighter()
    assert fighter.get_cost() == 10
    assert fighter.get_attack() == 6
    assert fighter.get_defense() == 6
    assert fighter.health == 1
    assert fighter.name == "Fighter"
    assert fighter.unit_class == "Plane"
    assert fighter.blitz != None
    assert fighter.bombard == None
    assert fighter.first_strike == False
    assert fighter.air_superiority == True

def test_boat():
    battleship = boat.Battleship()
    assert battleship.get_cost() == 18
    assert battleship.cost == [6,6,6]
    assert battleship.get_attack() == 8
    assert battleship.get_defense() == 8
    assert battleship.health == 2
    assert battleship.name == "Battleship"
    assert battleship.unit_class == "Boat"
    assert battleship.blitz == None
    assert battleship.bombard == 4
    assert battleship.first_strike == False
    assert battleship.air_superiority == False

def test_terrain():
    inf = infantry.Infantry()
    assert inf.get_attack() == 2
    assert inf.get_attack(terrains=[terrain.Mountain()]) == 1

    assert inf.get_defense() == 4
    assert inf.get_defense(terrains=[terrain.Mountain()]) == 4
