import crypt
import optparse
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
def testPass(cryptPass,dname):
    salt=cryptPass[0:2]
    dictFile=open(dname,"r")
    for word in dictFile.readlines():
        word=word.strip("\n")
        cryptWord=crypt.crypt(word,salt)
        if(cryptWord == cryptPass):
            print("[+] Password is found\n[+] Password is: " + word + "\n")
            exit(0);
    print("[-] Password not found \n")
    return

def Main():
    parser=optparse.OptionParser("USAGE =>  [Program Name] " + "-f <password file>   -d <dictionary file>" + "\n\nThe dictionary and password file should be present in same directory")
    parser.add_option("-f", dest="pfile", type="string" ,help="Specify password file")
    parser.add_option("-d", dest="dfile", type="string" ,help="Specify dictionary file")
    (options,args)=parser.parse_args()
    if ((options.pfile == None) | (options.dfile == None)):
        print(parser.usage)
        exit(0);
    passwordFileName=options.pfile
    dictionaryFileName=options.dfile
    password=open(passwordFileName,"r")
    for line in password.readlines():
        if ":" in line:
            username=line.split(":")[0]
            cryptPass=line.split(":")[1].strip(" ")
            cryptPass=cryptPass.strip("\n")
            print("[*] Password cracking started for userame " + username + "\n")
            testPass(cryptPass,dictionaryFileName)
        else:
            username=line.split(" ")[0]
            cryptPass=line.split(" ")[1].strip(" ")
            cryptPass=cryptPass.strip("\n")
            print("[*] Password cracking started for userame " + username + "\n")
            testPass(cryptPass,dictionaryFileName)

Main()
