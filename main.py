
from person import Person
if __name__ == "__main__":
    q = 353 # prime q
    pr = 3 # primite root for prime q

    # Create two instances of Person
    alice = Person(name="Alice")
    bob = Person(name="Bob")

    # Generate Key Pairs for the Diffie Hellman Algorithm.
    # Private key is generated using a CLCG 
    alice.generateKeyPairs(q,pr)
    bob.generateKeyPairs(q,pr)

    # Exchange public keys between users and generate symetric keys 
    # using each other public key. Both symetric keys should be equal. 
    alice.generateSymetricKey(bob)
    bob.generateSymetricKey(alice)

    # Alice sends an encrypted file to Bob 
    # using RC4 algorithm with the symetric key.
    alice.sendFile("input.txt",bob)

    # Bob recieves the encrypted file from Alice and decrypts it 
    # using RC4 algorithm with the symetric key.
    bob.decryptFile("encrypted.txt",alice)


