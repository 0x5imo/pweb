import subprocess


def checkSource(flagInit, url):
    source = subprocess.run("curl " + url , shell=True).split(separator=" ")
    if "<! --" in source:
        print("comment found in source code, check for hints")
    if "<script>" in source:
        print("this site uses a script")
    for i in source:
        if "==" in i:
            print("potential base64 encrypted string found")
        if flagInit in i:
            print(flagInit + " found in source code, check for flag or hints")


    
