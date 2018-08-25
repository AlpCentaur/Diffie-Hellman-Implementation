# Angriff auf den Diffie Hellman Schluesselaustausch

import hashlib
import ssl
from binascii import unhexlify, hexlify
import struct as struc
import math    
from multiprocessing import Pool
import sys



Prime = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF

Generator = 2



#A = 0x10000
#B = 0x10000000000000000000000000000000000000000000000000000000000000000

A = int(sys.argv[1],16)
B = int(sys.argv[2],16)

#intA = int(sys.argv[1],16)
#intB = int(sys.argv[2],16)

#new_intA = intA + 0x200
#new_intB = intB + 0x200

#A = hex(new_intA)
#B = hex(new_intB)


def GenerateSharedKey(e , pk_victim):
        
    sharedsecVictim = '{:x}'.format(pow(pk_victim, e, Prime))
    
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
        
        
        z = True
        
        comparetable1 = []
        comparetable2 = []
        
        #print('1')
        i = 1
        while z == True:
            i += Iterationnumber
            
            #if i == 6:
                #print(comparetable1, comparetable2)
                #z = False
            
            
            
            comparetable1.append(generatesharedkeypk1(i))
            comparetable2.append(generatesharedkeypk2(i+1))
            l = len(comparetable2)
            #print('l', l)
            for n in range(l - 1):
                #print(n)
                if comparetable1[n][:collisionnumber] == comparetable2[l-1][:collisionnumber]:
                    out11 = comparetable1[n]
                    #print('n', n)
                    #print('l-1', l-1)
                    out12 = comparetable2[l-1]
                    #print(out11, out12)
                    #print(i, i+1)
                    #print('ID', ID)
                    #GLOBAL = 1
                    outnum1 = (n+1) * 2 + 1
                    outnum2 = (l ) * 2 + 2
                    
                    #print(outnum1, outnum2)
                    
                    z = False
            for m in range(l - 1):
                #print('m',m)
                if comparetable2[m][:collisionnumber] == comparetable1[l - 1][:collisionnumber]:
                    
                    out21 = comparetable1[l-1]
                    out22 = comparetable2[m]
                    #print(out21, out22)
                    #print(i, i+1)
                    #print('m', m)
                    #print('l-1', l-1)
                    #print('ID', ID)
                    #print(comparetable2)
                    #print('compi1', comparetable1)
                    outnum2 = (m+1) * 2  + 2
                    outnum1 = (l ) * 2 + 1
                    
                    #print(i,i+1)
                    #print(outnum1, outnum2)
                    
                    #GLOBAL = 1
                    z = False
            
        
        
        return outnum1, outnum2
        
        #IDlist = []
        #for i in range(numberCPUs):
            #IDlist.append(i * 2)
            
        #worker(0)
        #worker(1)
        
        
        
        
        # Hier ist der Versuch, das ganze zu parallelisieren
        
        
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
    
    print( )
    print( )
    
    print('Starting the Birthday Attack to get the first 7 characters equal..')
    print('If you would like to try more characters with a stronger machine..')
    print('Look in the __main__ function at the end of code and change according to the comment')
    DHA = DiffieHellAttack()
    
    outnum1, outnum2 = DHA.BirthdayAttack(A, B , 1 , 7)  # Change the last argument here to your prefered number!!
    print('The private key for the exchange with Alice:', hex(outnum1))
    print('The generated public key for Alice', GenerateSharedKey(outnum1 , A))
    print('The private key for the exchange with Bob:', hex(outnum2))
    print('The generated public key for Bob', GenerateSharedKey(outnum2, B))
    #print(generatesharedkeypk1(48))
    
    
    
