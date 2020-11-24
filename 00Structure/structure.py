# <- derrière le "#" est un commentaire de ligne, ignoré par Python
# Toujours inclure un commentaire d'en-tête au début du vos
# fichiers Python. Le prochain commentaire est un bon exemple d'en-tête:

# Ce fichier démontre la structure de base d'un script Python
# David Crowley, crowlda@ecolecatholique.ca
# 2020-11-17

# ----------VOCABULAIRE-----------
# commentaire
# déclaration (simple et composée)
# mot-clé
# bloc de code
# indentation
# erreur de syntaxe
# erreur d'exécution
# erreur de logique

import keyword



## Python exécute les déclaration en ordre séquentielle

print("bonjour") # chaque ligne en Python est une déclaration
print("le")
print("monde")

# Blocs de code : déclarations composées
#
# STRUCTURE de la déclaration composée
#
# signature:
#       bloc de code indenté
#       toutes les lignes ont la même indentation
#
# SIGNATURE
# <mot-clé> <condition>:


# Exemple de déclaration composée (une boucle qui se répète 10 fois)
for i in range(10):
    print(i) # Le bloc de code doit être indenté

# Essaye cette version sans indentation (enlevant les #)
#for i in range(10):
#print(i)


# Mots-clés (reservés)
#
# for est un mot-clé
# voici la liste complète :
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

