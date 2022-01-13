string=input("Enter string: ")
rot=int(input("Enter number of rotations: "))

def encupper(asciiv):
    counter=1
    while counter <= rot:
        if(asciiv >=65 and asciiv <=90):
            asciiv +=1
        if asciiv == 91:
            asciiv=65
        counter+=1
    return int(asciiv)

def enclower(asciiv):
    counter=1
    while counter <= rot:
        if(asciiv >=97 and asciiv <=122):
            asciiv +=1
        if asciiv == 123:
            asciiv=97
        counter+=1
    return int(asciiv)

def decupper(asciiv):
    counter=1
    while counter <= rot:
        if(asciiv >=65 and asciiv <=90):
            asciiv -=1
        if asciiv == 64:
            asciiv=90
        counter+=1
    return int(asciiv)

def declower(asciiv):
    counter=1
    while counter <= rot:
        if(asciiv >=97 and asciiv <=122):
            asciiv -=1
        if asciiv == 96:
            asciiv=122
        counter+=1
    return int(asciiv)

def enc(string):
    for i in string:
        asciiv=ord(i)
        if(asciiv >=65 and asciiv <=90):
            char=encupper(asciiv)
        if(asciiv >=97 and asciiv <=122):
            char=enclower(asciiv)
        if i==" ":
            char=ord(i)
        print(chr(char),end="")
    print()

def dec(string):
    for i in string:
        asciiv=ord(i)
        if(asciiv >=65 and asciiv <=90):
            char=decupper(asciiv)
        if(asciiv >=97 and asciiv <=122):
            char=declower(asciiv)
        if i==" ":
            char=ord(" ")
        print(chr(char),end="")
    print()

enc(string)
dec(string)
    
