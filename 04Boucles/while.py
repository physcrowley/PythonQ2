# Exemples de boucles
#
#

# C'est quoi une boucle?
#
# C'est une façon de répéter du code sans avoir à le copier et coller
#
# Deux types
# 
# * while -> (générale) on ne sait pas combien de fois on va répéter
# * for -> on connaît d'avance le nombre de répétitions
#

#----------------WHILE-----------------
#
# "Pendant", "Tant et aussi longtemps que"
#
#  STRUCTURE :
#
# while <condition / booléen> :
#     # code qui s'éxécute tant que la condition reste vrai
#     # doit inclure une façon de quitter la boucle
#

# Exemple simple, infini
""" <-- début de commentaire multi-ligne
while True:
    print("this is the song that never ends")
    # arrive à la fin du code, vérifie la condition. Si vrai, répète.
    
    # ici il n'y a rien que brise la boucle, alors elle se répète à l'infini
""" # <-- fin de commentaire multi-ligne 


# Exemple simple corrigé
"""
while True:
    print("this is the song that never ends")
    
    print("\t...unless you enter q")
    end = input().lower()
    if end == "q":
        break # le mot-clé break quitte une boucle, sans toucher la condition de la boucle
"""

# Exemple simple, version 2
"""
repeat = True # boolean (est soit True, soit False)
while repeat:
    print("this is the song that never ends")
    
    print("\t...unless you enter q")
    end = input().lower()
    if end == "q":
        repeat = False # on change la valeur utilisée dans la condition de la boucle
"""

# Exemple - compter tous les nombres de 1 à 10

num = 0
somme = 0
while num < 10 :
    print(num, somme) # utiliser print() pour voir comment les variables évoluent
    somme += num # = somme + num
    num += 1 #= num + 1
    
print(num, somme)



#--------------FOR------------------
#
# "Pour", "Pour ce nombre de fois"
#
#  STRUCTURE :
#
# for <variable_de_boucle> in range(<nombre>) :
#     # code qui s'éxécute en augmentant la valeur de la <variable_de_boucle>
#     # jusqu'à ce qu'elle arrive à <nombre>
#     # > variable_de_boucle < nombre
#     # > variable_de_boucle = 0 pour commencer
#

somme = 0
for num in range(10) :
    print(num, somme)
    somme += num # = somme + num
    num += 1 #= num + 1
    
print(num, somme)

print("fin")