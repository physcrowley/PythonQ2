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
#
# > Ne pas copier-coller les commentaires.
#


#---------------VARIABLES-----------------#
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

# On assigne une valeur de chaque type à trois variables différentes
num = 6  
texte = "6" 
decimal = 6.0 


#-----------------TYPES------------------#
#
# Les valeurs de base en Python sont regroupés en trois types :
# * 'int' (nombre entier) --> utilisé pour compter
# * 'str' (texte) --> usage général
# * 'float' (nombre décimal) --> utilisé pour calculer ou pour saisir des nombres à la console
#

#---LA FONCTION TYPE()---#
# Python détermine automatiquement le type de valeur, mais c'est caché
# On peut utiliser la fonction type() pour voir le type des valeurs
print("num =", type(num), "texte =", type(texte), "decimal = ", type(decimal))

#---CONVERTIR LES TYPES---#
# Si on n'a pas besoin de compter ou de calculer, on devrait garder
# les valeurs en format texte, surtout les valeurs qui sont saisies
# à la console. Cela élimine plusieurs erreurs possibles et simplifie
# le programme.
#
# Par contre, on doit souvent utiliser les valeurs saisies pour partir
# un compte ou un calcul. Il convient alors de convertir le texte en
# nombre. On le fait à l'aide des deux fonctions suivantes :
# 
# int(s) # convertir le texte dans la variable s en 'int'.
# float(s) # convertir le texte dans la variable s en 'float'.
# 
# Parfois, on doit combiner du texte et des valeurs pour les afficher.
# À ce moment, il convient de convertir les nombres en texte avec la 
# fonction suivante :
# 
# str(n) # convertir le nombre dans la variable n (int ou float) en 'str'.
#

value = "6" # texte

i_value = int(value) # nombre entier
count = i_value + 1

f_value = float(value) # nombre décimal
result = f_value / 4

print("The final count is " + str(count)) # combiner deux textes
print("The division gives " + str(result))


#------------------ENTRÉES AVEC INPUT()--------------------#
#
# Pour saisir une réponse de l'utilisateur via la console, on utilise
# la fonction input().
#
# input()
# * arrête le programme en attendant la réponse de l'utilisateur
# * retourne (donne) le TEXTE saisi au programme
#
# On assigne normalement le texte à une variable afin de l'utiliser
# plus loin dans le programme.
#

#---COMMUNICATION VIA LA CONSOLE---#
#
# C'est important de communiquer clairement l'intention du programme
# en utilisant des messages à l'utilisateur avec print(). Il y a trois
# types de messages qui devraient être passés à l'utilisateur :
# 
# * une instruction claire et précise
# * une confirmation de saisie ou du résultat du traitement
# * un message d'erreur s'il y a un problème
# 


#---EXEMPLES---#

# Ex 1. Multiplier la valeur saisie
print("Enter an integer value.") # instruction claire

user_input = input()

print("You entered", user_input) # confirmation

result = 6 * user_input

print("Your value multiplied by 6 is", result) # présenter le résultat

# Le résultat n'est pas ce qu'on attend.  
# C'est parce que input() donne du TEXTE. Python définit la 
# multiplication de texte comme la *répétition* du texte 
# le nombre de fois spécifié (ce qui peut être utile, mais  
# n'est pas l'intention ici)


# Ex 2. Multiplier un entier
#     On répète l'exemple précédent avec une modification
print("Enter an integer value.")
user_input = input()
print("You entered", user_input)
result = 6 * int(user_input) # convertir à 'int' pour le calcul
print("Your value multiplied by 6 is", result)

# Ici le programme peut planter si la valeur saisie par l'utilisateur
# ne représente pas un entier (c'est du texte ou un nombre décimal). 
# C'est parce que la fonction int() sera incapable de faire la 
# conversion.

# Noter que le type de user_input n'a pas changé
print(type(user_input)) # toujours du texte ('str')

# Pour changer le type pour le reste du programme, il faut assigner
# le résultat de la conversion à une variable. Voici deux exemples :
i_input = int(user_input) # la valeur originale est conservée
user_input = int(user_input) # la valeur originale est écrasée

print(type(i_input))
print(type(user_input))
