import models.artillery as artillery
import models.boat as boat
import models.infantry as infantry
import models.plane as plane
import models.vehicles as vehicles

def get_unit_from_name(name):
    match name:
        case 'Militia':
            return infantry.Militia()
        case 'Infantry':
            return infantry.Infantry()
        case 'Airborne Infantry':
            return infantry.AirborneInfantry()
        case 'Elite Airborne Infantry':
            return infantry.EliteAirborneInfantry()
        case 'Marine':
            return infantry.Marine()
        case 'Mountain Infantry':
            return infantry.MountainInfantry()
        case 'Colonial Infantry':
            return infantry.ColonialInfantry()
        case 'Foreign Legion':
            return infantry.ForeignLegion()
        case 'Gurkha':
            return infantry.Gurkha()
        case 'Artillery':
            return artillery.Artillery()
        case 'Advanced Artillery':
            return artillery.AdvancedArtillery()
        case 'Self-propelled Artillery':
            return artillery.SelfPropelledArtillery()
        case 'Advanced Self-propelled Artillery':
            return artillery.AdvancedSelfPropelledArtillery()
        case 'Katyusha':
            return artillery.Katyusha()
        case 'Anti-Aircraft Artillery':
            return artillery.AntiAircraftArtillery()
        case 'Cavalry':
            return vehicles.Cavalry()
        case 'Motorized Infantry':
            return vehicles.MotorizedInfantry()
        case 'Mechanized Infantry':
            return vehicles.MechanizedInfantry()
        case 'Advanced Mechanized Infantry':
            return vehicles.AdvancedMechanizedInfantry()
        case 'Panzer-grenadier':
            return vehicles.PanzerGrenadier()
        case 'Tank Destroyer':
            return vehicles.TankDestroyer()
        case 'Light Tank':
            return vehicles.LightTank()
        case 'Medium Tank':
            return vehicles.MediumTank()
        case 'Heavy Tank':
            return vehicles.HeavyTank()
        case 'T-34':
            return vehicles.T34()
        case 'Tiger I':
            return vehicles.TigerI()
        case 'Fighter':
            return plane.Fighter()
        case 'Jet Fighter':
            return plane.JetFighter()
        case 'Tactical Bomber':
            return plane.TacticalBomber()
        case 'Medium Bomber':
            return plane.MediumBomber()
        case 'Strategic Bomber':
            return plane.StrategicBomber()
        case 'Heavy Strategic Bomber':
            return plane.HeavyStrategicBomber()
        case 'Seaplane':
            return plane.Seaplane()
        case 'Air Transport':
            return plane.AirTransport()
        case 'Heavy Air Transport':
            return plane.HeavyAirTransport()
        case 'Torpedo Boat Destroyer':
            return boat.TorpedoBoatDestroyer()
        case 'Destroyer':
            return boat.Destroyer()
        case 'Coastal Defense Ship':
            return boat.CoastalDefenseShip()
        case 'Light Cruiser':
            return boat.LightCruiser()
        case 'Heavy Cruiser':
            return boat.HeavyCruiser()
        case 'Battlecruiser':
            return boat.Battlecruiser()
        case 'Battleship':
            return boat.Battleship()
        case 'Heavy Battleship':
            return boat.HeavyBattleship()
        case 'Light Carrier':
            return boat.LightCarrier()
        case 'Fleet Carrier':
            return boat.FleetCarrier()
        case 'Heavy Fleet Carrier':
            return boat.HeavyFleetCarrier()
        case 'Coastal Submarine':
            return boat.CoastalSubmarine()
        case 'Submarine':
            return boat.Submarine()
        case 'Advanced Submarine':
            return boat.AdvancedSubmarine()
        case 'Naval Transport':
            return boat.NavalTransport()
        case 'Attack Transport':
            return boat.AttackTransport()
