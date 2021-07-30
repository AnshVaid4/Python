import sys
import json
import time
from socket import *
import requests
flag=1
def grabber(host):
    try:
        req=requests.get("https://"+host)
        print("[+] "+str(req.headers))
        ip=gethostbyname(host)
        print("[+] IP address is "+ip)
        details=requests.get("https://ipinfo.io/"+ip+"/json")
        detailsjson=json.loads(details.text)
        try:
            print("[+] Hostname is "+detailsjson["hostname"])
            print("[+] City is "+detailsjson["city"])
            print("[+] Country is "+detailsjson["country"])
            print("[+] Geo location is "+detailsjson["loc"])
            print("[+] Organization is "+detailsjson["org"])
            print("[+] Timezone is "+detailsjson["timezone"])
            return 1
        except:
            print("[+] City is "+detailsjson["city"])
            print("[+] Country is "+detailsjson["country"])
            print("[+] Geo location is "+detailsjson["loc"])
            print("[+] Organization is "+detailsjson["org"])
            print("[+] Timezone is "+detailsjson["timezone"])
            exit(0)
    except:
        req=requests.get("http://"+host)
        print("[+] "+str(req.headers))
        ip=gethostbyname(host)
        print("[+] IP address is "+ip)
        details=requests.get("https://ipinfo.io/"+ip+"/json")
        detailsjson=json.loads(details.text)
        try:
            print("[+] Hostname is "+detailsjson["hostname"])
            print("[+] City is "+detailsjson["city"])
            print("[+] Country is "+detailsjson["country"])
            print("[+] Geo location is "+detailsjson["loc"])
            print("[+] Organization is "+detailsjson["org"])
            print("[+] Timezone is "+detailsjson["timezone"])
            return 1
        except:
            print("[+] City is "+detailsjson["city"])
            print("[+] Country is "+detailsjson["country"])
            print("[+] Geo location is "+detailsjson["loc"])
            print("[+] Organization is "+detailsjson["org"])
            print("[+] Timezone is "+detailsjson["timezone"])
            exit(0)



def Main():
    hname=input("Enter the host name: ")
    if (hname== ""):
        print("Hostname can't be empty")
        time.sleep(10)
        exit(0)
    else:
        print("[+] Scanning for "+hname)
        if(grabber(hname)):
            time.sleep(15)
            exit(0)
    if(flag==1):
        print("[-] Sorry unable to fetch details")
        time.sleep(15)
        exit(0)
print("\n")
print("        ___________                                                          ")
print("       //          \                                                         ")
print("      //            \                                                        ")
print("     //                                                                      ")
print("    //                                                                       ")
print("   ||                                                                        ")
print("   ||         --------|| ||====       //  ||===   ||===   |=====  ||====     ")
print("    \                 || ||    \     //|  ||   \  ||   \  ||      ||    \    ")
print("     \               //  ||====/    //=|  ||==/   ||==/   ||--    ||====/    ")
print("      \             //   ||    \   //  |  ||   \  ||   \  ||      ||    \    ")
print("       \___________//    ||     \ //   |  ||___/  ||===/  ||====  ||     \   ")
print("  ---------------------------------------------------------------------------")
print("  -------------------By: Ansh Vaid-------v1.1--------------------------------")
print("\n\n\n")

Main()
