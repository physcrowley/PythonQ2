# Déclarer et utiliser des listes
# David Crowley, crowlda@ecolecatholique.ca
# 2020-12-15

"""
COLLECTIONS

Il y a plusieurs collections de valeurs dans Python. Une collection
garde PLUSIEURS VALEURS à l'intérieur d'une seule variable.

Trois qui sont très semblables sont les listes, les tuples et les
ensembles. Dans les trois cas, on accède aux valeurs individuelles
en utilisant un indice (une adresse sous forme de nombre entier).

> Le premier indice est toujours 0.
> Le dernier indice est toujours len(<collection>) - 1 où <collection>
    est remplacé avec le nom de la variable qui représente la liste,
    le tuple ou l'ensemble.
> Les indices sont spécifiés entre crochets immédiatement après le nom
    de la variable, p. ex. ma_liste[<indice>] où indice est remplacé par
    une nombre entier inclut entre 0 et len(ma_liste) - 1.


LISTE - la collection la plus utilisée

Propriétés : 
    * on peut modifier les valeurs
    * la longueur peut changer
    * l'ordre de placement des éléments est conservé

Déclaration --> avec des crochets [ ]

ma_liste = [1,2,3]
ma_liste[0] # 1
len(ma_liste) # 3
ma_liste.append(4) # [1,2,3,4]
ma_liste.remove(2) # [1,3,4]


TUPLE - une collection de constantes

Propriété : 
    * on ne peut pas modifier ni les valeurs, ni la longueur
    
Déclaration --> avec des parenthèses ( )

mon_tuple = ('lundi','mardi','mercredi','jeudi','vendredi','samedi','dimanche')
len(mon_tuple) # 7


ENSEMBLE - collection de valeurs uniques

Propriété : 
    * une seule copie de chaque valeur unique
    * l'ordre des éléments n'est pas conservé

Déclaration --> avec des accolades { }

mon_ensemble = {1,2,3}
"""

#---- Tester les propriétés via la console python ---
#
# Voir le Meet et les exercices pour des exemples


#------- Exemple pour traverser une liste -------

ma_liste = ['a', 'b', 'c']

# la boucle `for each`... pour chaque x dans collection
for lettre in ma_liste:
    lettre = chr(ord(lettre) + 1) # augmente la valeur ASCII (ord) et retourne le nouveau caractère (chr)
    print(lettre)
print(ma_liste) # la liste originale n'a pas changé (seulement la variable temporaire 'lettre')

# avec une boucle `for` de base... 
#   utilise len(ma_liste) pour le nombre d'iterations
for indice in range(len(ma_liste)):
    ma_liste[indice] = chr(ord(ma_liste[indice]) + 1)
    print(ma_liste[indice])
print(ma_liste) # la liste a changé car on manipulait directement ses valeurs


#--------------- Jeu de mots ------------------

# Préparer les phrases à trou
phrases = []
consignes = []
# le trou dans la phrase est indiqué par les {}
phrases.append("Une {} tombe sur ma tête.")
consignes.append("nom commun")
phrases.append("Je vais chez le {} pour me faire vérifier.")
consignes.append("professionnel, masculin")


# Obtenir les réponses de l'utilisateur
mots = []
# on demande un mot pour chaque consigne, utilisant la boucle 'for each'
for c in consignes:
    # ici le print utilise la méthode .format() qui remplace chaque {}
    # dans le texte avec la valeur dans le .format()
    print("Taper un mot qui est un(e) {}".format(c))
    mots.append(input())


# Afficher le résultat
print("Quand tu est prêt(e) pour le résultat, tape Enter")
input() # attend

for i in range(len(phrases)):
    # les trous {} dans les phrases sont remplacés par les mots.
    print(phrases[i].format(mots[i]))

print("\nMerci d'avoir joué!")