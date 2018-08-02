# Implementation of Diffie Hellman Key Exchange, runs with pypy


import hashlib
import ssl
from binascii import unhexlify, hexlify
import struct as struc
import math    


Prime = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF




Generator = 2

a = 0xca7693246391f9cc12e3a631ed2fb3fb0bf67538ef7c36ca9eb2df2430e50b3dca75a2033363e0a86c09ab348e21f4f93a3b88732531302d367fb7de51b63574d1e8b10206afccdbf2144e921a5736636273352c7065ade67b764a304e8b8178f75a983f79c3fad999aa5809810ef3473c65ddaa645ef4b8ce2e0ddb2eea17e4
b = 0xe4539485b7efb7d9d635088ffb6a85c88ca83431127057c3c641bf3de1f9b8eb3eecc367dbc80b7872466a91739c5e65f9c68a43c2980f2a585dce10cc475830300f17dd7306271e71f4ead016630b29d4e27007f86774ee816dfeae43bc58cb460b4b57c83ed77b113edc1a023e51ce43003e8423a1a4a66a9f8cb01a0f1cd0

import math



class DiffieHell:
    
    def __init__(self):
        
        self.prime = Prime
        self.generator = Generator
        self.privatekeyAlice = a
        self.privatekeyBob = b
        
    
    
    
    
    
    def generatepublickeys(self):
        self.publickeyAlice = pow(self.generator, self.privatekeyAlice, self.prime)
        self.publickeyBob = pow(self.generator, self.privatekeyBob, self.prime)
        
    
    
    def generatesharedsecret(self):
        self.sharedsecAlice = '{:x}'.format(pow(self.publickeyBob, self.privatekeyAlice, self.prime))
        self.sharedsecBob = '{:x}'.format(pow(self.publickeyAlice, self.privatekeyBob, self.prime))
        
    def sharedsecTOsha512(self):
        
        
        
        
        self.hashAlice = hashlib.sha512(self.sharedsecAlice.encode())
        self.hashBob = hashlib.sha512(self.sharedsecBob.encode())        
        
        
        self.keyAlice = self.hashAlice.hexdigest()
        self.keyBob = self.hashBob.hexdigest()
        
        
if __name__ == '__main__':
    
    Calc = DiffieHell()
    Calc.generatepublickeys()
    
    print('A',hex(Calc.publickeyAlice),'\n')
    print('B',hex(Calc.publickeyBob),'\n')
    
    
    Calc.generatesharedsecret()
    
    print('K',format(Calc.sharedsecAlice),'\n')
    print('K',Calc.sharedsecBob,'\n')
    
    
    Calc.sharedsecTOsha512()
    
    print('HashK',Calc.keyAlice,'\n')
    print('HashK',Calc.keyBob,'\n')
