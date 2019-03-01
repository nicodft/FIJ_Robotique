import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    # creer 2 variables, le maximum et notre cible
    max = 0
    cible = 0
    
    #parcourir "range" qui va de 0-7, index commence à 0
    for index in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        
        #comparer la hauteur de la montagne avec max
        if mountain_h > max :
            #si max est plus petit que la hauteur, on récupere
            # cette hauteur et on prend l'index pour cible
            max = mountain_h
            cible = index
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(cible)