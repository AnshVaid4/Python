#run it with python and not with python3
from socket import *
import optparse
import nmap

def scan(targethost,targetport):
    n=nmap.PortScanner()
    n.scan(targethost,targetport)
    state=n[targethost]['tcp'][int(targetport)]['state']
    print("[+] "+targethost+ " port "+str(targetport)+" "+state) 
    

 
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
        print("[+] Starting scan for "+target+"\n")
        if "." in target:
            #name,alias,addresslist = lookup(target)
            try:
                hostName=gethostbyaddr(target)
                print("[+] Host name resolved to "+hostName[0])
            except:
                hostName="Not Resolved"
                print("[-] Host name  "+hostName)
            finally:
                if '-' in options.pname:
                    portRange=options.pname.split("-")
                    portRange=range(int(portRange[0]),int(portRange[1]))
                else:
                    portRange=str(options.pname).split(",") 
                for port in portRange:
                     port=str(port)
                     scan(target,port)
        else:
            target=gethostbyname(target)
            print("[+] Target IP found "+target)
            if '-' in options.pname:
                portRange=options.pname.split("-")
                portRange=range(int(portRange[0]),int(portRange[1]))
            else:
                portRange=str(options.pname).split(",") 
            for port in portRange:
                port=str(port)
                scan(target,port)
            
print("\n\n")
print("||\          |                                                                                               ")
print("|| \         |                                                                                               ")
print("||  \        |                                                                                               ")
print("||   \       |                                                                                               ")
print("||    \      |                                                                                               ")
print("||     \     |\          /||======  ||=====                                                                  ")
print("||      \    | \        / ||     || ||    ||                                                                 ")
print("||       \   |  \      /  ||     || ||    ||                                                                 ")
print("||        \  |   \    /   ||=====|| ||=====                                                                  ")
print("||         \ |    \  /    ||     || ||                                                                       ")
print("||          \|     \/     ||     || ||                                                                       ")
print("-------------------------------------------")
print("-----------By: Ansh Vaid----v1.1-----------\n\n\n")

Main()
