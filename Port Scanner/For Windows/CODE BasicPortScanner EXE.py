#use python if send recv method is implemented
#use python3 if send recv method is not implemented
from socket import *
import optparse
import time
def scan(host,port):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((host,int(port)))
        print("[+] TCP Port " +str(port) + " is open")
        sock.close()
    except:
        print("[-] TCP Port " +str(port) + " is close")
        

def Main():
    #parser=optparse.OptionParser("Usage => -i for IP address and -p for port range")
    #parser.add_option("-i",dest="ipadd",type="string",help="Enter the IP address")
    #parser.add_option("-p",dest="ports",type="string",help="Enter port number")
    #(options,args)=parser.parse_args()
    
    
    setdefaulttimeout(1)
    ip=input("Enter the target IP address: ")
    ports=input("Enter the port numbe(s): ")
    if((ip == "") | (ports == "")):
        print("[-]Somethig went wrong")
        time.sleep(15)
        exit(0);
    print("[+] Scanning for "+ip+"\n")
    if "-" in ports:
        Ports=str(ports).split("-")
        portRange=range(int(Ports[0]),int(Ports[1]))
    elif "," in ports:
        portRange=str(ports).split(",")
    else:
        portRange=[]
        portRange.append(ports)
    for port in portRange:
        scan(ip,port)
    time.sleep(15)
    exit(0)
print("\n\n")
print("        ||======                                               _______                                  ") 
print("        ||      \                                             //      \                                 ") 
print("        ||      |                                            //                                         ") 
print("        ||=====/            ____                             ||________                                 ") 
print("        ||      \      //  //    \   ======    _____                   \      ____      // ||\    |    ") 
print("        ||       \    //| ||_____      ||     //    \                   \   //    \    //| || \   |    ") 
print("        ||        |  //=|        \     ||     ||                        ||  ||        //=| ||  \  |    ") 
print("        ||       /  //  |        ||    ||     ||                       //   ||       //  | ||   \ |    ") 
print("        ||======/  //   |  \____//  ========   \____/         \_______//     \___// //   | ||    \|    ") 
print("       ------------------------------------------------------------------------------------------")
print("       -----------------------By: Ansh Vaid----v1.1----------------------------------------------\n\n\n")
Main()
