
from dh import DiffieHellman
from rc4 import RC4
from definitions import DATA_DIR,OUT_DIR

class Person():
    
    def __init__(self,name):
        self.name = name
        self.symetricKeys = {}
        self.privKey = 0
        self.pubKey = 0

    def generateKeyPairs(self,q,pr):
        """
        Generates Diffie Hellman Key Pair
        """
        self.dh = DiffieHellman(q,pr)
        self.privKey, self.pubKey = self.dh.getKeyPairs()
        print("[DIFFIE HELLMAN] Generating Diffie Hellman Key Pairs for " + self.name + "... " + "[Pub : " + str(self.pubKey) + " | PRIV : " + str(self.privKey) + "]")


    def generateSymetricKey(self,person):
        """
        Generates the Symmetric Key for a given Public Key of a person.
        """
        self.symetricKeys[person.name] = str(self.dh.computeSymetricKey(person.pubKey))
        print("[DIFFIE HELLMAN] Generating Symetric key for " + self.name + " with " + person.name + " Public Key... " + "[Symetric Key : " + self.symetricKeys[person.name] + "]")


    def sendFile(self,file,to):
        """
        Sends an encrypted file to someone by using the symmetric key they share.
        """ 
        print("["+self.name+"] Preparing to send file to " + to.name)
        print("["+self.name+"] Encrypting file using RC4 algorithm and the Symetric key [" + self.symetricKeys[to.name] + "]..." )
        rc4 = RC4(self.symetricKeys[to.name])
        f = open(DATA_DIR / file,"r",encoding="utf8")
        with open(OUT_DIR / "encrypted.txt","w+",encoding="utf8") as out:
            #a,b = self.tokenize(f.read())
            #out.write(a)
            out.write(rc4.encrypt(f.read()))
        
        print("["+self.name+"] Encrypted file written to " + str(OUT_DIR)  + "/encrypted.txt ...")

    def decryptFile(self,file,fro):
        """
        Decrypts a recieved file from someone by using the symmetric key they share.
        """ 
        print("["+self.name+"] Received an encrypted file from " + fro.name)
        print("["+self.name+"] Decrypting the file using RC4 algorithm and the Symetric key [" + self.symetricKeys[fro.name] + "]..." )
        rc4 = RC4(self.symetricKeys[fro.name])
        f = open(OUT_DIR / file,"r",encoding="utf8")
        with open(OUT_DIR / "decrypted.txt","w+",encoding="utf8") as out:
            #a,b = self.tokenize(f.read())
            #out.write(a)
            out.write(rc4.decrypt(f.read()))

        print("["+self.name+"] Decrypted file written to " + str(OUT_DIR) + "/decrypted.txt ...")


    def tokenize(self,text):
        return text[:-8], text[-8:]
