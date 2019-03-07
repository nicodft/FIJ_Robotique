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

#

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




