# Conditions avec une structure plus développée
# Par : David Crowley, crowlda@ecolecatholique.ca
# 2020-12-01 🎄

# Séquence exclusive 
#
# mot-clé elif ("else if", "sinon si")
#

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