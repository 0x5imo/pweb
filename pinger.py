import os

def statuscheck(url):
    response = os.system("ping -c 1 " + url)
    if response == 0:
        print(f"{url} is up!")
    else:
        print(f"{url} is down!")




if __name__ == "__main__":
    statuscheck('127.0.0.1')













