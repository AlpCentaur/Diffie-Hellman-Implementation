# Angriff auf den Diffie Hellman Schluesselaustausch

import hashlib
import ssl
from binascii import unhexlify, hexlify
import struct as struc
import math    
from multiprocessing import Pool



Prime = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF

Generator = 2


A = 0x10000
B = 0x10000000000000000000000000000000000000000000000000000000000000000

def GenerateSharedKey(e , pk_victim):
        
    sharedsecVictim = '{:x}'.format(pow(pk_victim , e, Prime))
    
    hashVictim = hashlib.sha512(sharedsecVictim.encode())
    
    keyVictim = hashVictim.hexdigest()
    
    return keyVictim


class DiffieHellAttack:
    
    def __init__(self):
        
        self.prime = Prime
        
        self.generator = Generator
        
    
    def BirthdayAttack(self, pk_victim1, pk_victim2 , numberCPUs, collisionnumber):
        
        
        
        # numberCPUs wird eingefuert fuer eventuelle parallelisierung, da dann jede nummer als einzelnes array berechnet werden kann, was bei einer großen
        # anzahl von rechnern zu schnelleren ergebnissen fuehren wird ansonsten geht natuerlich auch cpu_count()
        
        
        
        Iterationnumber = numberCPUs * 2
        
        def generatesharedkeypk1(x):
            return GenerateSharedKey(x,pk_victim1)
        
        def generatesharedkeypk2(x):
            return GenerateSharedKey(x,pk_victim2)
        
        def worker(ID):
            GLOBAL = 0
            z = True
            i = ID
            comparetable1 = []
            comparetable2 = []
            
            print('1')

            while z == True:
                
                i += Iterationnumber
                if ID == 0:
                    print(1)
                
                
                
                
                
                comparetable1.append(generatesharedkeypk1(i))
                comparetable2.append(generatesharedkeypk2(i+1))
                l = len(comparetable1)
                for n in range(l - 1):
                    if comparetable1[n][:collisionnumber] == comparetable2[l-1][:collisionnumber]:
                        out1 = comparetable1[n]
                        print('n', n)
                        print('l-1', l-1)
                        out2 = comparetable2[l-1]
                        print(out1, out2)
                        print(i, i+1)
                        print('ID', ID)
                        GLOBAL = 1
                        outnum1 = i
                        outnum2 = i+1
                        z = False
                for m in range(l - 1):
                    if comparetable2[m][:collisionnumber] == comparetable1[l - 1][:collisionnumber]:
                        out1 = comparetable1[l-1]
                        out2 = comparetable2[m]
                        print(out1, out2)
                        print(i, i+1)
                        print('m', m)
                        print('l-1', l-1)
                        print('ID', ID)
                        #print(comparetable2)
                        #print('compi1', comparetable1)
                        
                        outnum1 = i
                        outnum2 = i+1
                        GLOBAL = 1
                        z = False
                
            
            return GLOBAL
        
        
        IDlist = []
        for i in range(numberCPUs):
            IDlist.append(i * 2)
            
        worker(0)
        worker(1)
        
        
        
        
        # Hier ist der Part, den ich nicht zum laufen gebracht habe.. aber generell funktioniert das programm
        
        
        #pool = Pool(numberCPUs)
        
        #def check_terminate(GLOBAL):
            #G = GLOBAL
            
            #if G == 1:
                #pool.terminate()
        
        
        #IDlist = []
        #for i in range(numberCPUs):
            #IDlist.append(i * 2)
        
        #print(IDlist)
        
        #results = pool.(worker, IDlist, callback=check_terminate)
        #print('1')
        #pool = Pool(numberCPUs)
            
        #IDlist = []
        #for i in range(numberCPUs):
            #IDlist.append(i * 2)
        
        #def check_terminate(GLOBAL):
            #G = GLOBAL
            
            #if G == 1:
                #pool.terminate()
        
        
        
        ## Start up all of the processes
        #for i in IDlist:
            #print('1')
            #pool.apply_async(worker, (i,), callback=check_terminate)

        #pool.close()
        #pool.join()

        
        
if __name__ == '__main__':
    
    DHA = DiffieHellAttack()
    
    DHA.BirthdayAttack(A, B , 2 , 7)
    
    print(GenerateSharedKey(80 , A))
    print(GenerateSharedKey(81, B))
    
    
    
