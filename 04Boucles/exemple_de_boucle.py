# Exemples de l'utilité de boucles
# David Crowley, crowlda@ecolecatholique.ca
# 2020-12-08


# Exemple 1. Calculer la somme des nombres entrés

sum = 0
num = "0"
# si la valeur num (qui reçoit le texte input()) est juste des nombres, on continue
while num.isdigit(): 
    # on peut convertir le texte dans num à int sans erreur, et ajouter la valeur à sum
    sum += int(num) 
        # cette ligne doit venir après la vérification .isdigit() et non après
        # le input() afin d'éviter les erreurs, et aussi pour savoir quand quitter...
        # si une lettre est entrée par l'utilisateur, on quitte la boucle sans tenter
        # d'ajouter la lettre à la somme

    print("Entrer un nombre entier.")
    print("\tTaper n'importe quel autre caractère pour quitter")
    num = input()

print("La somme est", sum)


