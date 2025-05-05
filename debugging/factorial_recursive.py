#!/usr/bin/python3
import sys

# Fonction : factorial
# Description : Cette fonction calcule la factorielle d'un nombre entier n en utilisant la récursion.
#               La factorielle d'un nombre entier n (notée n!) est le produit de tous les entiers
#               de 1 à n. Par exemple, la factorielle de 5 est 5! = 5 * 4 * 3 * 2 * 1 = 120.
#
# Paramètres :
#    - n (int) : Le nombre entier dont la factorielle doit être calculée.
#
# Retour :
#    - int : La factorielle de n. Si n est 0, la fonction retourne 1 (car 0! = 1).

def factorial(n):
    # Si n est égal à 0, retourner 1 (condition de base pour la récursion)
    if n == 0:
        return 1
    else:
        # Sinon, calculer la factorielle de n en appelant la fonction récursivement pour n-1
        return n * factorial(n-1)

# Récupérer l'argument de ligne de commande (sys.argv[1]), le convertir en entier, et calculer la factorielle
f = factorial(int(sys.argv[1]))

# Afficher le résultat de la factorielle calculée
print(f)

