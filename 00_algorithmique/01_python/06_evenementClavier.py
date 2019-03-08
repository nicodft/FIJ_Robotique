#import de la librairie qui nous sert a recuperer les evenements lie au clavier
import click
#on defini notre flag qui sert a continuer la boucle tant que c'est VRAI
continuer = True

while continuer:
        
        key = click.getchar()
        print (key)
        
        if key == "e":
                continuer = False
