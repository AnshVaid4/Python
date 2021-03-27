import bcrypt
import optparse
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
print(" --------------By: Ansh Vaid---------v1.2-------------------          ")
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
    #parser=optparse.OptionParser("USAGE =>  [Program Name] " + "-f <password file>   -d <dictionary file>" + "\n\nThe dictionary and password file should be present in same directory")
    #parser.add_option("-f", dest="pfile", type="string" ,help="Specify password file")
    #parser.add_option("-d", dest="dfile", type="string" ,help="Specify dictionary file")
    #(options,args)=parser.parse_args()
    #if ((options.pfile == None) | (options.dfile == None)):
    #    print(parser.usage)
    #    exit(0);
    passwordFileName=input("Enter name of file having username and hashes: ")
    dictionaryFileName=input("Enter name of file having list of passwords ")
    password=open(passwordFileName,"r")
    for line in password.readlines():
        if ":" in line:
            username=line.split(":")[0]
            cryptPass=line.split(":")[1].strip(" ")
            cryptPass=cryptPass.strip("\n")
            print("\n[*] Password cracking started for userame " + username)
            testPass(username,cryptPass,dictionaryFileName)
        elif " " in line:
            username=line.split(" ")[0]
            cryptPass=line.split(" ")[1].strip(" ")
            cryptPass=cryptPass.strip("\n")
            print("[*] Password cracking started for userame " + username + "\n")
            testPass(username,cryptPass,dictionaryFileName)

Main()
