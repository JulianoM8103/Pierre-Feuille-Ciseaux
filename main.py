# Ce programme est un "Pierre, feuille, ciseaux" 
# Il y a un utilisateur et un ordinateur

# Le jeu continue à l'infini tant que l'utilisateur de l'arrête pas

# Les règles du jeu :
# Si les 2 signes sont les mêmes c'est une égalité
# La pierre gagne contre le ciseaux et perd contre la feuille
# Le ciseaux gagne contre la feuille et perd contre la pierre
# La feuille gagne contre la pierre et perd contre le ciseaux

# Importation du module "random"
from random import randint

# Options
jeu  = ["pierre", "feuille", "ciseaux"]

#Attribuer une option aléatoire à l'ordinateur
ordinateur = jeu[randint(0,2)]

#Gardez le compte des points
PointsJoueur = 0
PointsOrdinateur = 0

jouer = True

# La boucle continue tant que la variable "jouer" est "True"
while(jouer):
    # Choix joueur
    joueur = input("pierre, feuille, ciseaux? Tapez Fin si vous voulez arrêter le jeu!\n")
    
    # Scénarios
    if(joueur == 'Fin'):
        continuer = False
    elif(joueur == ordinateur):
        print("Egalité!")
    elif(joueur == "pierre"):
        if(ordinateur == "feuille"):
            print("Perdu!", ordinateur, "recouvre", joueur)
            Pointsordinateur = PointsOrdinateur + 1 
        else:
            print("Gagné!", joueur, "écrase", ordinateur)
            Pointsjoueur = PointsJoueur + 1
    elif(joueur == "feuille"):
        if(ordinateur == "ciseaux"):
            print("Perdu!", ordinateur, "coupe", joueur)
            Pointsordinateur = PointsOrdinateur + 1
        else:
            print("You win!", joueur, "recouvre", ordinateur)
            Pointsjoueur = PointsJoueur + 1
    elif(joueur == "ciseaux"):
        if(ordinateur == "pierre"):
            print("Perdu...", ordinateur, "écrase", joueur)
            Pointsordinateur = PointsOrdinateur + 1
        else:
            print("Gagné!", joueur, "coupe", ordinateur)
            Pointsjoueur = PointsJoueur + 1
    else:
        print("Votre choix n'est pas correct, vérifiez l'orthographe!")
    #Attribuer une option aléatoire à l'ordinateur
    ordinateur = jeu[randint(0,2)]
    print('********Tour suivant********')

#Impression des points
print("********Points********")
print("joueur: ", Pointsjoueur)
print("ordinateur: ", Pointsordinateur)