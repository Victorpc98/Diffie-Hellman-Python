
import math
from lcg import LinearCongruentialGenerator

class CombinedLinearCongruentialGenerator():

    def __init__(self,k,modulus,a):
        """
        Inits the CLCG initializing k LCG for each modulus and a 
        """
        self.k = k
        self.modulus = modulus
        self.a = a
        self.lcg = [LinearCongruentialGenerator(m,a) for m,a in zip(modulus,a)]

    def next(self):
        """
        Returns the next random number between 0 and 1 with float decimals
        """
        x = [(math.pow(-1,i) * lcg.next()) for lcg,i in zip(self.lcg,[i for i in range(self.k)])]
        x = sum(x) % self.lcg[0].modulus
        r = x/self.lcg[0].modulus if x > 0 else ( x/self.lcg[0].modulus +1 if x < 0 else (self.lcg[0].modulus-1)/self.lcg[0].modulus)
        return r


