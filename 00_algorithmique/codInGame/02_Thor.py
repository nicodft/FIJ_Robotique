#Exemple 1---------------------------------------------

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
lightX, lightY, thorX, thorY = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    # To debug: print("Debug messages...", file=sys.stderr)

    # Cette ligne nous permet de debuguer le programme en nous donnant la position de thor a chaque tours.
    print("thorX =", thorX, " thorY =",thorY, file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW

    # On verifie les combinaison de direction, 
    # si elles sont toutes fausses, on sait qu'on ira en ligne droite.
    if thorY > lightY and thorX < lightX:
        print("NE")
        thorY = thorY - 1
        thorX = thorX + 1
    
    elif thorY < lightY and thorX < lightX:
        print("SE")
        thorY = thorY + 1
        thorX = thorX + 1
    
    elif thorY > lightY and thorX > lightX:
        print("NW")
        thorY = thorY - 1
        thorX = thorX - 1
        
    
    elif thorY < lightY and thorX > lightX:
        print("SW")
        thorY = thorY + 1
        thorX = thorX - 1
    
    # On verifie les conditions pour aller en ligne droite
    if thorX > lightX:
        print("W")
        thorX = thorX - 1
        
    elif thorX < lightX:
        print("E")
        thorX = thorX + 1
        
    elif thorY > lightY:
        print("N")
        thorY = thorY - 1
        
    elif thorY < lightY:
        print("S")
        thorY = thorY + 1
        





#Exemple 2---------------------------------------------

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# lightX: the X position of the light of power
# lightY: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
lightX, lightY, thorX, thorY = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Cette ligne nous permet de debuguer le programme en nous donnant la position de thor a chaque tours.
    print("thorX =", thorX, " thorY =",thorY, file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW

    # Pour chaque direction, on a une combinaison de 2 elements
    # Par exemple, NE est la combinaison de Nord et de Est
    # Autre exemple, E est la combinaison de "rien" et de Est
    # Ou encore, S est la combinaison de Sud et de "rien"
    dir1="" 
    dir2=""
    
    # Pour notre 1ere direction
    if thorY > lightY: #North
        dir1="N"
        thorY = thorY - 1
        
    elif thorY < lightY: #South
        dir1="S"
        thorY = thorY + 1

    # Pour notre seconde direction
    if thorX > lightX: #West
        dir2="W"
        thorX = thorX - 1
        
    elif thorX < lightX: #Est
        dir2="E"
        thorX = thorX + 1
        
    
    print(dir1+dir2)
        
    