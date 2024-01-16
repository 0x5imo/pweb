import subprocess


def xsscheck(url):
    parameters = [""," --path"," --json", " --crawl"]
    command = "python3 xsstrike.py -u " + url
    for i in parameters:
        print(subprocess.run(command + i, shell=True))


if __name__=="__main__":
    xsscheck("google.com")
 

