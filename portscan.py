import os

def portscan(ip):
    response = os.system("nmap -sV -Pn  " + ip)
    print(response)


print(portscan("127.0.0.1"))
    