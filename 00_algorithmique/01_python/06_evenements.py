""" # import d'une librerie destinee aux interfaces graphique qui nous permet de
# gerer different evenements (event en anglais)
import tkinter

# on cree une fonction qui prend notre evenement en parametre
def eventHandle(event):
    # on demande d'afficher dans le terminal l'etat et la touche qui est
    # pressee ou relachee
    print ("etat :",event.type, event.keysym)


# creation d'une instance de la classe TK, que l'on affecte à l'objet "root"
root = tkinter.Tk()

# exemple qui prend en compte toutes les touches pressee et relachee.
# on peut associer directement une touche particuliere en replacant
# par exemple "<KeyPress>" par "<Right>"
root.bind("<KeyPress>", eventHandle) # Touche pressee
root.bind("<KeyRelease>", eventHandle) # Touche relachee


root.mainloop() """

"""
from pynput import keyboard

# notre fonction de pression des touches du clavier
def presse(key):
    try:
        print("la touche",key.char, "a ete pressee")
        
    except AttributeError:
        print("la touche speciale",key,"a ete pressee")

# notre fonction de relachement  des touches du clavier
def relache(key):
    print("la touche",key,"a ete relachee")
    if key == keyboard.Key.esc:
        # Stop ecoute
        return False

# On Collecte les evenement jusqu'a l'appel de keyboard.Listener.stop ou
# si une de nos fonctions retourne False (ici, relache)
with keyboard.Listener(
        on_press=presse,
        on_release=relache) as listener:
    listener.join()

""" 

"""
import keyboard

keyboard.press_and_release('shift+s, space')

#keyboard.write('The quick brown fox jumps over the lazy dog.')

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Press PAGE UP then PAGE DOWN to type "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Blocks until you press esc.
keyboard.wait('esc')

# Record events until 'esc' is pressed.
recorded = keyboard.record(until='esc')
# Then replay back at three times the speed.
keyboard.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# Block forever, like `while True`.
keyboard.wait()
 """

import click

key = click.getchar()
continuer = True

while continuer:
        
        key = click.getchar()
        print (key)

        if key == "e":
                continuer = False

""" import readchar


continuer = True

while continuer:
        

        if readchar.readchar() == readchar.key.ESC:
                continuer = False

        else:
                print("ok") """