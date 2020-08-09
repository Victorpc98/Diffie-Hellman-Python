

import random
class LinearCongruentialGenerator():
    

    def __init__(self,modulus,a):
        """
        Inits the LCG for the given modulus and a.
        """
        self.modulus = modulus
        self.a = a
        self.seed_range = {
            "start":1,
            "end":147483562
        }
        self.y = random.randrange(self.seed_range["start"],self.seed_range["end"])

    def next(self):
        """
        Returns the next random number between 0 and 1
        """
        return (self.a * self.y) % self.modulus


