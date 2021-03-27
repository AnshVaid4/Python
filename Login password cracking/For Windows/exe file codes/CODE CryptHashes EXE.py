import bcrypt
import time
print("        //      //                                        				  ")
print("       //      //                                         				  ")
print("      //      //                                          				  ")
print("     //======//       _____                                                                ")
print("    //      // //|  //     \    //   //                                                    ")
print("   //      // // |  ||_____    //===//                                                     ")
print("  //      // //==|         \  //   //                                                      ")
print(" //      // //   |   \____// //   //                                                       ")
print("_____________________________________                                                      ")
print("------By: Ansh Vaid----v1.0----------                                                      ")
print("\n\n")
string=input("Enter the string you want to get bcrypt hashed: ")
ask=input("Do you want to enter BCRYPT salt? Y/N ")
if (ask=="Y"):
    salta=input("Enter a valid BCRYPT salt ")
    if "$2b$12$" in salta:
        salta=bytes(salta,'utf-8')
        print("Creating hash with "+str(salta.decode()))
        print("\nBCRYPT salt used in hashing is: " + str(salta.decode()))
        ########################################################
        print("---------------------------------------------------------------------------------------------")
        hasha=bcrypt.hashpw(bytes(string,'utf-8'),salta)
        print("BCRYPT hash with salt is: " +  str(hasha.decode()))
        time.sleep(15)
        exit(1)
    else:
        print("Invalid BCRYPT salt entered. Come again later!")
        time.sleep(10)
        exit(0)
if (ask=="N"):
    salta=bcrypt.gensalt()
else:
    exit(0)
print("\nBCRYPT salt used in hashing is: " + str(salta.decode()))
########################################################
print("---------------------------------------------------------------------------------------------")
hasha=bcrypt.hashpw(bytes(string,'utf-8'),salta)
print("BCRYPT hash with salt is: " +  str(hasha.decode()))
time.sleep(15)


