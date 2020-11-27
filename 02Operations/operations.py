
# Exemples des opérations de base en Python
# Par : David Crowley, crowlda@ecolecatholique.ca
# 2020/11/27

import math # ajouter les import immédiatement après l'en-tête

#------------------TESTER DES OPÉRATIONS--------------------#
#
# C'est pratique de tester des choses avant de
# les inclure directement dans notre programme. C'est
# possible grâce au shell python --> un mode d'utiliser
# python directement à la console.
# 
# Normalement, on passe un fichier (notre programme) à
# Python avec la commande à la console :
# 
# python <fichier>.py
# 
# Pour travailler directement avec Python sans fichier,
# il faut simplement écrire :
# 
# python
# 
# L'apparence de la console change et tu peux entrer des 
# déclarations Python un-par-un pour les tester.
# 
# Pour quitter le mode shell de python, tu passes la 
# commande :
# 
# quit()
# 
# ---AFFICHAGE---
# En mode shell, tu n'as pas besoin d'utiliser des print()
# pour afficher les résultats. Le but est de TOUT voir alors
# chaque résultat s'affiche automatiquement.
# 
# N'oublie pas d'ajouter des print() dans ton programme pour
# afficher des résultats. C'est un oubli classique quand on a
# travaillé dans le shell python et on revient pour écrire
# notre programme.


#################################################
# Pour afficher un résultat ci-dessous, entoure #
# l'opération par un print().                   #
#################################################


#---------OPERATIONS MATHÉMATIQUES-------------#
#
# +, -, /, *, module math
#

# Exemples d'opérations mathématiques valides
3 + 1 # 4

a = 5
a + 12 # 17

a * a # 25 (le carré de a)
a * a * a # 125 (le cube de a)

math.pow(a, 2) # 25.0 (a à la puissance ('power') 2)

# Noter que les fonctions de la module math produisent
# des résultats qui sont de type float (décimal)


#------------COMPARAISONS-------------#
#
# ==, >, <, >=, <=, !=
#

# ATTENTION!!! : == n'est pas la même chose que =
# 
# * == compare les deux valeurs, gauche par rapport à droite
# * = assigne la valeur à la droite à la variable à la gauche
#

# Exemples de comparaisons valides
5 == 5 # True - égale à
5 == 6 # False - pas égale à
5 < 6  # True - moins grand que
5 > 6  # False - plus grand que
5 <= 6 # True - moins grand que ou égale à
5 >= 6 # False - plus grand que ou égale à
5 != 6 # True - pas égale

5 == 5.0 # True
5 == 5.1 # False
5 == 5.000000000000001 # False
5 == 5.0000000000000001 # True

# Les ordis ont parfois des comportements bizarres avec les valeurs
# décimales.
# 
# Pour comparer des float, c'est souvent mieux de vérifier que la
# différence absolue (ignorant les signes) entre les deux est moins 
# qu'une valeur acceptable, par exemple :

precision_limit = 0.001
abs(5 - 5.000324) < precision_limit # True
# la fonction abs() enlève le signe négatif


#----------MANIPULATION DE TEXTE----------#
#
# .lower(), .upper() --> pour changer la case
# ord(), chr() --> pour des caractères individuels
#

# Exemples de valeurs saisies pour une réponse de "oui".
oui = "oui"
OUI = "OUI"
oUi = "oUi"
OUi = "OUi"

print(oui.lower(), OUI.lower(), oUi.lower(), OUi.lower())
print(oui.upper(), OUI.upper(), oUi.upper(), OUi.upper())

oui == "oui" # True
OUI == "oui" # False
OUI.lower() == "oui" # True

# L'avantage ici est d'avoir à écrire une seule comparaison qui
# donne le bon résultat même avec une multitude de réponses variées

print("oui ou non?")
choix = input()
choix.lower() == "oui"
choix.lower() == "non"


#---VALEURS DES CARACTÈRES---#
# Un ordinateur compare du texte en interprétant la valeur numérique
# de chaque caractère un par un.
# Valeur numérique??? Oui! Chaque caractère est associé à une position
# spécifique dans un tableau, comme le tableau ASCII ou le tableau
# Unicode

# Pour connaître la valeur numérique d'un caractère, on utilise
# la fonction ord()
ord('o') # 111
ord('O') # 79

# noter que les majuscules ont une plus petite valeur que les
# minuscules

# ASTUCE : la différence entre la valeur majuscule et minuscule est
#   toujours 32

# Pour connaître le caractère associé à une valeur dans le tableau,
# on utilise la fonction chr()
chr(79) # 'O'
chr(79 + 32) # 111 -> 'o' 
chr(65) # 'A'

