# Exemples de conditions

# STRUCTURE
#
# if <condition à évaluer> :
#     <commandes à faire si la condition est vraie>
#     <(doit avoir au moins une commande)>
# <le programme continue ici... immédiatement si la condition est fausse>
#   ... aussi après le code conditionnel

# exemple simple
""" <--- les triple guillemets sont utilisé pour un commentaire de plusieurs lignes
print("oui ou non?")

choix = input()

if choix.lower() == "oui":
    print("excellent choix") # bloc indenté
    print("tu est la personne la plus intellgente au monde!")
    # etc.

print("merci d'avoir joué")
""" # <-- il faut fermer le commentaire triple guillemets aussi

# exemple de SÉQUENCE de conditions
"""
print("oui ou non?")
choix = input().lower()

if choix == "oui":
    print("très positif")

print("rouge ou vert?")
choix = input().lower()

if choix == "rouge":
    print("très festif")

print("merci d'avoir joué")
"""

# exemple de CASCADE de conditions

print("oui ou non?")
choix = input().lower()

if choix == "oui":
    print("très positif")

    print("rouge ou vert?")
    choix = input().lower()

    if choix == "rouge":
        print("très festif")

print("merci d'avoir joué")