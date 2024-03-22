from fish import Pair


class Fish:
    def __init__(self, pair: Pair, quantity: int = 1):
        self.pair: Pair = pair
        self.quantity: int = quantity

    def __str__(self):
        return f"There are {self.quantity}\n of {self.pair.species}\n, both the age of {self.pair.age}\n in the jar"
