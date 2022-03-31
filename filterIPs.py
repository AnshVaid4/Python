import ipaddress
f = open("Filtered_initialiPsDump.txt","a")
with open("Unique_initialiPsDump.txt") as file:
    lines=file.readlines()
    for line in lines:
        #print(line)
        try:
            line=line.replace("\n","")
            if ipaddress.ip_address(line):
                line=line+"\n"
                f.write(line)
                print(line)
        except:
            pass
f.close()
