import subprocess

def sqlicheck(url):

    sqlmap_command = "sqlmap -u" + url + "  --level 5 --risk 3 --batch"
    print(subprocess.run(sqlmap_command, shell=True))


if __name__ == '__main__':
    sqlicheck('google.com')









    
