# Plus sur la boucle for
# David Crowley, crowlda@ecolecatholique.ca
# 2020-12-08

#--------------FOR------------------
#
# "Pour", "Pour ce nombre de fois"
#
# STRUCTURE :
#
# for <variable_de_boucle> in range(<nombre>) :
#     # code qui s'éxécute en augmentant la valeur de la <variable_de_boucle>
#     # jusqu'à ce qu'elle arrive à <nombre>
#     # > variable_de_boucle < nombre
#     # > variable_de_boucle = 0 pour commencer
#


#--------DÉTAILS EN LIEN AVEC RANGE--------
#
# SIGNATURE :
#
# range([valeur_de_départ,] valeur_de_fin[, bonds])
#
# les valeurs entre crochets sont optionnels 
#
# Par défaut : valeur_de_départ = 0, bonds = 1
# 
# range() produit une liste de nombres de valeur_de_départ
#     à (valeur_de_fin - 1). 
#


# Exemples de range
"""
#for i in range(10):
#for i in range(6,10):
#for i in range(0,10,2):
#for i in range(10,0,-1):
for i in range(0,-10,-1):
    print(i)
"""

# Exemple utilisant le tableau ASCII
début = 65+32
for c in range(début,début+26): # 'A' est la valeur 65 dans le tableau ASCII
    print(chr(c))