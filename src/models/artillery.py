from models.base_units import ArtilleryClass

class Artillery(ArtilleryClass):
    def __init__(self):
        super().__init__(attack=3, defense=3, name="Artillery", cost=4)

class SelfPropelledArtillery(ArtilleryClass):
    def __init__(self):
        super().__init__(attack=3, defense=3, name="Self-propelled Artillery", cost=5)

class AdvancedArtillery(ArtilleryClass):
    def __init__(self):
        super().__init__(attack=4, defense=4, name="Advanced Artillery", cost=4)

class AdvancedSelfPropelledArtillery(ArtilleryClass):
    def __init__(self):
        super().__init__(attack=4, defense=4, name="Advanced Self-propelled Artillery", cost=5)

class Katyusha(ArtilleryClass):
    def __init__(self):
        super().__init__(attack=5, defense=4, name="Katyusha", cost=5)

class AntiAircraftArtillery(ArtilleryClass):
    def __init__(self):
        super().__init__(attack=3, defense=3, name="Anti-Aircraft Artillery", cost=4)
