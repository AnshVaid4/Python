import crypt
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
def testPass(cryptPass,dname):
    #salt=cryptPass[0:35]   for MD5 hash password
    salt=cryptPass[0:2]    #for crypt hash password
    dictFile=open(dname,"r")
    for word in dictFile.readlines():
        word=word.strip("\n")
        word=word.strip(" ")
        cryptWord=crypt.crypt(word,salt)
        if(cryptWord == cryptPass):
            print("[+] Password found " + word + "\n")
            return
    print("[-] Password not found \n")
    return

def Main():
    passFile=open("password.txt","r")
    for line in passFile.readlines():
        if ":" in line:
            user=line.split(":")[0]
            cryptPass=line.split(":")[1].strip(" ")
            cryptPass=cryptPass.strip("\n")
            print("[*] Password cracking started for userame " + user)
            testPass(cryptPass,"dictionary.txt")
Main()
