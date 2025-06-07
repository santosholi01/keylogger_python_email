import os
import socket
import platform
from requests import get

system_information="system_info.txt"
file_path= "D:\\CYBERSECURITY PROJECT(KEYLOGGER)\\project"

extend="\\" 

def computer_information():
    with open(file_path +extend +system_information, "a") as f:
        hostname=socket.gethostname()
        IPAddr=socket.gethostbyname(hostname)
        try:
            public_ip= get("https://api.ipify.org").text
            f.write("public ip address: " + public_ip +'\n')
        except Exception:
            f.write("coundn't get public ip address")
        
        f.write("Processor:" + (platform.processor()) + '\n')
        f.write("Systen: "+ platform.system() +" " +platform.version() + '\n')
        f.write("Machine: "+ platform.machine() + '\n')
        f.write("Hostname: "+ hostname +"\n")
        f.write("Private IP address: " + IPAddr + "\n")
        

computer_information()
