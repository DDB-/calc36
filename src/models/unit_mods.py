class Blitz:
    def __init__(self, ratio):
        self.ratio = ratio
        self.needs_pair = (ratio is None)

class OneRound:
    def __init__(self, sides, repeats):
        self.sides = sides
        self.repeats = repeats
