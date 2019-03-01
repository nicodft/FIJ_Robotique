# Exemple 1 -----------------------------------

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # v_speed: the vertical speed (in m/s), can be negative.
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Vu que l'objet est en chutte libre, il n'avance pas mais recule
    # Sa vitesse verticale est du coup negative
    # On doit rester a une vitesse de chutte inferieure a -40
    # Donc tant que notre vitesse est superieure, inutile d'utiliser les propulseurs
    if v_speed > -40 : # on pourrait garder une marge de securite en mettant la valeur 38 plutot que 40
        # On envoit 2 entier
        # le 1er est l'inclinaison qu'on laisse a 0
        # Le second c'est la vitesse des propulseurs
        print ("0 0")
    
    else :
        print ("0 4")
    






# Exemple 2 -----------------------------------

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # v_speed: the vertical speed (in m/s), can be negative.
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Vu que l'objet est en chutte libre, il n'avance pas mais recule
    # Sa vitesse verticale est du coup negative
    # On doit rester a une vitesse de chutte inferieure a -40
    # Donc tant que notre vitesse est superieure, inutile d'utiliser les propulseurs
    if v_speed > -40: # on pourrait garder une marge de securite en mettant la valeur 38 plutot que 40
        speed=0
    else:
        speed=4

    # On envoit 2 entier
    # le 1er est l'inclinaison qu'on laisse a 0
    # Le second c'est la vitesse des propulseurs
    print("0",speed)