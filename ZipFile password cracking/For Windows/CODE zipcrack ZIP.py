#run with python3 command
import optparse
import pyzipper
import os
import time
def ExtractZip(zFile,password):
    try:
        with pyzipper.AESZipFile(zFile, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_file:
             zip_file.extractall(pwd=str.encode(password))
             print("[+] Password found: " + password + "\n[+] Files extracted" )
             time.sleep(15)
             os._exit(0)
    except:
        pass

def Main():
    #parser=optparse.OptionParser("Usage => -f <zip filename> -d <dictionary filename>\n")
    #parser.add_option("-d" , dest="dname", type="string" , help="Specify the name of dictionary file")
    #parser.add_option("-f" , dest="zname", type="string" , help="Specify the name of zip file")
    #(options,arg)=parser.parse_args()
    #if ((options.zname == None) | (options.dname == None)):
    #    print(parser.usage)
    #    time.sleep(15)
    #    exit(0)
    #else:
    zname=input("Enter the name of password protected zip file: ")
    dname=input("Enter the name of dictionary file: ")
    if((zname == "" ) | (dname== "")):
       print("[-] The above two values are required. Come back later")
       time.sleep(15)
       exit(0)
    try:
        password=open(dname,"r")

        for line in password.readlines():
            passwd=line.strip("\n")
            passwd=passwd.strip(" ")
            ExtractZip(zname,passwd)
        print("[-] Sorry no password found")
        time.sleep(15)
        exit(0)
    except:
        print("[-] Something went wrong")
        time.sleep(15)
        exit(0)

print("\n\n\n\n\n\n")
print("         //|      |         //         -------------                                         ")
print("        // |      |        //         ||                                                     ")
print("       //  |      |       //          ||                                                     ")
print("      //   |      |      //           ||                                                     ")
print("     //    |      |     //            ||                                                     ")
print("    //=====|      |    //             ||                                      __             ")
print("   //      |      |   //              ||             ||===     //|  ------ | /__             ")
print("  //       |      |  //               ||             ||__|    // | ||      |//               ")
print(" //        |  _   | //                ||             ||  \   //==| ||      |\                ")
print("//         | [_]  |//                 ||____________ ||   \ //   | ||_____ | \__             ")
print("__________________________________________________________________________________")
print("--------------------By: Ansh Vaid---------------v1.1------------------------------\n\n\n")
Main()

