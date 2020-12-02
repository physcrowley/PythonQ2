# Conditions avec une structure plus développée
# Par : David Crowley, crowlda@ecolecatholique.ca
# 2020-12-01 🎄

# Séquence exclusive 
#
# mot-clé elif ("else if ...", "sinon si ...")
#
"""
print("oui, non, peut-être?")

choix  = input().lower()

if choix == "oui":
    print("bravo!")
elif choix == "non": 
    # contrairement à un if, si choix == "oui", 
    # python saute les elif et passe tout de suite au code 
    # qui vient après la séquence de conditions
    print("ok")
elif choix == "peut-être":
    print("mais décide")

print("merci d'avoir participé")
"""

# Séquences avec action par défaut
#
# mot-clé else ("sinon ...")
#
"""
print("oui, non, peut-être?")

choix  = input().lower()

if choix == "oui":
    print("bravo!")
elif choix == "non":
    print("ok")
elif choix == "peut-être":
    print("mais décide")
else:
    print("je n'ai pas compris", choix)

print("merci d'avoir participé")
"""


# Exemple incluant quelque chose qui n'est pas conditionnel
# PRATIQUE À ÉVITER
#

print("oui ou non?")

choix  = input().lower()

# "conditionnel" - seulement dans certains cas définis
if choix == "oui":
    print("bravo!")
    print("merci d'avoir participé") # code qui s'exécute peu importe
elif choix == "non":
    print("ok")
    print("merci d'avoir participé") # code qui s'exécute peu importe
else:
    print("je n'ai pas compris", choix)
    print("merci d'avoir participé") # code qui s'exécute peu importe

# le code qui s'exécute peu importe devrait être à l'extérieur
# des conditions, comme dans les exemples précédants
#print("merci d'avoir participé")