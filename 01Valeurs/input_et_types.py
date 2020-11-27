# Toujours inclure un en-tête à vos fichiers python comme :

# Programme qui montre comment prendre les données de l'utilisateur
# via la console
#
# Par : David Crowley, crowlda@ecolecatholique.ca
# 2020-11-24

# ASTUCE : PYTHON TUTOR
#
# Copier et coller le code ci-dessous dans le site
# https://pythontutor.com pour voir l'exécution étape-par-étape
# et voir ce que Python fait (qui est normalement caché quand on
# exécute les programmes via une console normale).
# --> ce n'est pas nécessaire de copier-coller les commentaires.
#



#------------VARIABLES--------------#
#
# Les variables sont utilisées pour contenir de l'information qu'on
# peut utiliser plus tard dans le programme.
#
# STRUCTURE
#
# <nom_de_variable_sans_espaces> = <valeur>
#
# * <nom_de_variable_sans_espaces> --> le nom de variable devrait 
#   expliquer ce qu'elle contient ou ce qu'elle fait
# * = --> ce symbole en programmation veut dire "associer la valeur
#   qui se trouve à la droite avec le nom qui se trouve à la gauche"
# * <valeur> --> la valeur (un nombre, du texte, etc.) qu'on veut
#   assignée à un nom
#

#--------------TYPES-----------------#
#
# Les valeurs de base en Python sont regroupés en trois types :
# * 'int' (nombre entier) --> utilisé pour compter
# * 'str' (texte) --> usage général
# * 'float' (nombre décimal) --> utilisé pour calculer ou pour saisir des nombres à la console
#

# On assigne une valeur de chaque type à trois variables différentes
num = 6  
texte = "6" 
decimal = 6.0 

# Python détermine automatiquement le type de valeur, mais c'est caché
# On peut utiliser la fonction type() pour voir le type des valeurs ou des variables
print("num =", type(num), "texte =", type(texte), "decimal = ", type(decimal))


#---------------ENTRÉES AVEC INPUT()-------------------#
#
# Pour saisir une réponse de l'utilisateur via la console, on utilise
# la fonction input().
#
# input()
# * arrête le programme en attendant la réponse de l'utilisateur
# * retourne le TEXTE saisi à la console au programme
#
# On assigne normalement le texte à une variable afin de l'utiliser
# plus loin dans le programme.
#

#-----------COMMUNICATION VIA LA CONSOLE---------------#
#
# C'est important de comm

print("Entrer un nombre entier qui sera multiplié par 6")
#user_input = float(input())

#recommandé : garder les input en texte à moins d'avoir à le convertir
user_input = input()
user_input = float(user_input)

result = num * user_input

print("La multiplication donne", result)