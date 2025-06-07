# README📗
##  Project Title: keylogger 
  This project is a Python-based keylogger  capturing different features and information
   1. logging keystrokes
   2. capturing clipboard data(copied data)
   3. taking screenshots
   4. recording system mircophone audio
   5. gathering system information

  ALl collected data is encrypted using symmetric cryptography(fernet) and sent via email for remote access.
  Decrypte encrypted data through private key 


  # Dependencies🪟
  ## pynput
   1. used to monitor and log keyboard events(keystrikes).
   2. primary library for the keylogger functionality
  ## cryptograpy.fernet
  1. Provides symmetric encryption to encrypt/decrypt the captured data securely.
  2. Fernet ensures confidentiality with AES encryption.

  ## win32clipboard(from pywin32)
   1. Accesses Windows clipboard to capture copied data.
   2. Essential for clipboard monitoring.

  ## sounddevice
   1. Records audio using the system's microphone.
   2. Captures environmental audio for surveillance.
  ## scipy.io.wavfile
   1. Used to save the recorded audio in .wav format.

  ## PIP.ImageGrab
   1. Captures a screenshot of the system screen.
   2. Used for visual monitoring.

  ## platform, socket, os, getpass, requests
   1. Gathers system information, such as IP, OS version, hostname, etc.
   2. requests fetches the public IP from an external service.

  ## smtplib, email.MIME(Various)
   1. For sending encrypted data via email.
   2. Handles email formatting and attachments.

  ## multiprocessing, time
   1. Helps manage parallel or delayed execution and wait times.

# Implementation
 ## Encrypt🔒
  1. All gathered files (keystrokes, system info, audio, clipboard, screenshot) are encrypted using a Fernet key.
  2. The encryption key is generated and stored in a file

  ## Email Sending📨
   1. Encrypted files are sent as email attachments.
   2. Uses Gmail’s SMTP with app password authentication.

  ## Decryption🔓
   1.  using the same Fernet key, files are decrypted back to readable format.


# use_case(cybersecurity)
  1. Demonstrates how threat actors can gather sensitive data from victim machines.
  2. Can be used to test detection systems, SIEM tools, and endpoint protection.
  3. Educates on how such threats work, aiding in the development of better defensive mechanisms.









    










