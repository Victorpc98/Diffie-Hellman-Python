
class RC4():

    def __init__(self, key):
        self.K = [ord(char) for char in key] # convert key to ASCII code
        self.S = self.sbox()
        self.i = 0
        self.j = 0

    def sbox(self):
        """
        Returns the S box
        """
        S = [i for i in range(256)]
        j = 0
        for i in range(256):
            j = ( j + S[i] + self.K[i % len(self.K)]) % 256
            S[i], S[j] = S[j], S[i]

        return S

    def newByteStream(self):
        """
        Generates a new Byte Stream between 0 and 255 ( ASCII code )
        """
        self.i = (self.i + 1) % 256
        self.j = (self.j + self.S[self.i]) % 256
        self.S[self.i], self.S[self.j] = self.S[self.j], self.S[self.i]
        return self.S[((self.S[self.i] + self.S[self.j]) % 256)]

    def encrypt(self,plaintext):
        """
        Encrypts a given plaintext 
        """
        cipher_chars = []
        for char in plaintext:
            byte = ord(char) # get char representation in byte ( ASCII )
            cipher_byte = byte ^ self.newByteStream() # xor both ASCII codes
            cipher_chars.append(chr(cipher_byte)) # reconvert ASCII respresentation to character
        return ''.join(cipher_chars)

    def decrypt(self,ciphertext):
        """
        Decrypts a given ciphertext.
        """
        cipher_chars = []
        for char in ciphertext:
            byte = ord(char) # get char representation in byte ( ASCII )
            cipher_byte = byte ^ self.newByteStream() # xor both ASCII codes
            cipher_chars.append(chr(cipher_byte)) # reconvert ASCII respresentation to character
        return ''.join(cipher_chars)
