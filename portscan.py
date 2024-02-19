import os

def portscan(ip):
    response = os.system("nmap -sV -Pn  " + ip)
    print(response)



if __name__ == '__main__':
    portscan('127.0.0.1')
    