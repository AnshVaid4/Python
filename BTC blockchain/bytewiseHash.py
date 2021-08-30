import binascii
import hashlib
def hexStringToByte(content):
 return(binascii.unhexlify(content))  #hex decode and converting to bytes
def hashHex(algorithm, content):
 sha = hashlib.new(algorithm)
 sha.update(hexStringToByte(content))
 print(sha.hexdigest())
pubkey="03FFB6F0C3ED3CA16D84DC8C09AA380BD28C47BAB3F9FD2BB94ED5E7B0360B1D7E"
hashHex("SHA256",pubkey)
