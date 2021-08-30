import binascii
import hashlib
def littleEndian(val):
    valstr=str(val)
    if(len(valstr)<=8):
        string=""
        val=hex(val)
        #print(val)
        val=val[2:]
        length=len(val)
        for i in range(0, 8-length):
            string="0"+string
        val=string + val
        #print(val)
        string=""
        #print(val)
        val=val[::-1]
        for i in range(0,len(val),2):
            string=string + val[i+1] + val[i]
        #print(string)
        return string
        
        

    else:
        string=""
        val=hex(val)
        #print(val)
        val=val[2:]
        #print(val)
        val=val[::-1]
        #print(val)
        for i in range(0,len(val),2):
            string=string + val[i+1] + val[i]
        #print(string)
        return string



def hex2Little(val):
    val=val[::-1]
    string=""
    for i in range(0,len(val),2):
            string=string + val[i+1] + val[i]
    #print(string)
    return string

version = littleEndian(541065220)
prevBlockHash = hex2Little('00000000000000000004a86037743d60211548c7970e07071a2d03663befd563')
rootHash = hex2Little('3a61855a5c3adc7786b14bb5fb51fc050b4e1f60846fffcb707e2d7c3a782dff')
time = littleEndian(1626630204)
bits = littleEndian(387225124)
nonce = littleEndian(365784241)

#print(version)
#print(prevBlockHash)
#print(rootHash)
#print(time)
#print(bits)
#print(nonce)

header=version + prevBlockHash +rootHash + time + bits + nonce
my_sha=hashlib.new("SHA256")
my_sha.update(binascii.unhexlify(header))
hash1=my_sha.hexdigest()

my_sha2=hashlib.new("SHA256")
my_sha2.update(binascii.unhexlify(hash1))
blockHash=my_sha2.hexdigest()
blockHash=hex2Little(blockHash)
print("Block hash is: "+blockHash)
