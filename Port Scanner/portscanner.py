#run it with python if send recv method is implemented
#run it with python3 if send recv method is not implemented
from socket import *
import optparse
def scan(targethost,targetport):
    try:
        sock=socket(AF_INET,SOCK_STREAM)
        sock.connect((targethost,targetport))
        sock.send("test\n")
        results=sock.recv(100)
        print("[+] Target port " + str(targetport) + " is open")
    except:
        print("[-] Target port " + str(targetport) + " is closed")
    finally:
        sock.close()

def initial(Thost,Tport):
    try:
        ip=gethostbyname(Thost)
    except:
        print("[-] Target host " + Thost+ " unknown")
        return

    try:
        name=gethostbyaddr(ip)
        print("[+] Scanning results for " + name[0])
    except:
        print("[+] Scanning results for " + ip)


    setdefaulttimeout(3)
    for port in Tport:
        #print(port+Thost)
        scan(Thost,int(port))
def Main():
    parser=optparse.OptionParser("Usage => -t for hostname -p for port number")
    parser.add_option("-t", dest="hname", type="string",help="Enter the hostname")
    parser.add_option("-p", dest="pname", type="string",help="Enter the port number")
    (options,args)=parser.parse_args()
    if ((options.hname == None) | (options.pname == None)):
        print(parser.usage)
        exit(0)
    else:
        target=options.hname
        port=str(options.pname).split(",")
        initial(target,port)
print("\n\n")
print("        ________                                        _______                                  ") 
print("       //       \                                      //      \                                 ") 
print("      //                                              //                                         ") 
print("      ||_________                                     ||________                                 ") 
print("                 \     ____     ____                             \      ____      // ||\    |    ") 
print("                  \   //   \  //    \  || //                      \   //    \    //| || \   |    ") 
print("                  || ||    || ||       ||//                       ||  ||        //=| ||  \  |    ") 
print("                 //  ||    || ||       ||\                       //   ||       //  | ||   \ |    ") 
print("        \_______//    \___//   \___//  || \_            \_______//     \___// //   | ||    \|    ") 
print("       ------------------------------------------------------------------------------------------")
print("       -----------------------By: Ansh Vaid----v1.1----------------------------------------------\n\n\n")
Main()



