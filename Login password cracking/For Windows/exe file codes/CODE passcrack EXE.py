import bcrypt
import time
print("   ______                                                             ")
print(" //      \                                                            ")
print(" ||      ||                                                           ")
print(" ||      ||       ______     ______                 ______            ")
print(" ||-----//  //|  //     \   //     \  \   ||\   || ||     \           ")
print(" ||        // | ||_______   ||______   \  || \  || ||     ||          ")
print(" ||       //==|          \          \   \ ||  \ || ||     ||          ")
print(" ||      //   |  \______//   \_____//    \||   \|| ||____//           ")
print(" ___________________________________________________________          ")
print(" --------------By: Ansh Vaid---------v1.1-------------------          ")
print("\n\n")
def testPass(user,cryptPass,dname):
    try:
        #salt=cryptPass[0:35]   for MD5 hash password
        salt=cryptPass[0:29]    #for BCRYPT hash password
        dictFile=open(dname,"r")
        for word in dictFile.readlines():
            word=word.strip("\n")
            word=word.strip(" ")
            cryptWord=bcrypt.hashpw(bytes(word,'utf-8'),bytes(salt,'utf-8'))
            if(str(cryptWord.decode()) == cryptPass):
                print("[+] Password found " + word + "\n")
                print("[+] Confirming any other new line having BCRYPT hash")
                time.sleep(10)
                return
        print("[-] Password not found for "+user+"\n")
        return
    except:
        print("[-]BCRYPT hash found.\n[+]Confirming BCRYPT hash for next line if exists\n")
        time.sleep(10)
        return       

def Main():
    passFile=open("password.txt","r")
    for line in passFile.readlines():
        if ":" in line:
            user=line.split(":")[0]
            cryptPass=line.split(":")[1].strip(" ")
            cryptPass=cryptPass.strip("\n")
            print("\n[*] Password cracking started for userame " + user)
            testPass(user,cryptPass,"dictionary.txt")
Main()
