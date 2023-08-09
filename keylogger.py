from pynput.keyboard import Listener,Key

def bas(key):

    try:
        print(key.char,type(key.char))
    except AttributeError:
        pass

def birak(key):
    print("Birakıldı")

with Listener(on_press=bas,on_release=birak) as Listener:

    Listener.join()
