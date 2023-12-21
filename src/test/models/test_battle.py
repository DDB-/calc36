from models.battle import TargetSelection

import models.artillery as artillery
import models.boat as boat
import models.infantry as infantry
import models.plane as plane
import models.vehicles as vehicles

def test_target_hits():
    target = TargetSelection(target_type="Unit Class", targets=["Infantry"])

    assert target.applies(unit=infantry.Infantry())
    assert not target.applies(unit=vehicles.MediumTank())
    assert not target.applies(unit=plane.AirTransport())
    assert not target.applies(unit=boat.Destroyer())
    assert not target.applies(unit=artillery.Artillery())

def test_multi_target():
    target = TargetSelection(target_type="Unit Class", targets=["Infantry", "Vehicle", "Artillery"])

    assert target.applies(unit=infantry.Infantry())
    assert target.applies(unit=vehicles.MediumTank())
    assert not target.applies(unit=plane.AirTransport())
    assert not target.applies(unit=boat.Destroyer())
    assert target.applies(unit=artillery.Artillery())

def test_specific_unit():
    target = TargetSelection(target_type="Unit Name", targets=["Infantry", "Militia", "Fighter"])

    assert target.applies(unit=infantry.Infantry())
    assert target.applies(unit=infantry.Militia())
    assert not target.applies(unit=infantry.MountainInfantry())
    assert not target.applies(unit=plane.AirTransport())
    assert target.applies(unit=plane.Fighter())
    assert not target.applies(unit=artillery.Artillery())
