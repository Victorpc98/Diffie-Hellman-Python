
from clcg import CombinedLinearCongruentialGenerator

class DiffieHellman():

    def __init__(self,q,pr):
        """
        Inits the Diffie-Hellman protocol by creating the public and private key for que given 
        prime number (q) and the primite root of q (pr). 
        The private key is a random number between 0 and (q-1)
        The public key is [ (pr) ^ privkey mod q ]
        """
        self.q = q
        self.pr = pr
        self.clcg = CombinedLinearCongruentialGenerator(k=2,modulus=[2147483642,2147483423],a=[450,234])
        self.privKey = round((self.q-1) * self.clcg.next())
        self.publicKey = pow(self.pr,self.privKey) % self.q

    def getKeyPairs(self):
        """
        Returns key pairs
        """
        return (self.privKey,self.publicKey)
        
    def computeSymetricKey(self,pk):
        """
        Returns the symetric key resulting when using the given public key 
        SymetricKey = pk^privkey % mod q
        """
        return pow(pk,self.privKey) % self.q
