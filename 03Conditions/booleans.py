# Un type de variable qui est utile dans des conditions
# Par : David Crowley, crowlda@ecolecatholique.ca
# 2020-12-02 🎄


# types déjà vus
# --------------
# str -> texte
# int -> nombre entier
# float -> nombre décimal

# type 'bool' -> booléen (vrai/faux; 1/0; quelque chose/rien)

# UTILITÉ
#
# un drapeau, un indicateur d'état
#
# noms commencentent généralement par est<quelquechose> ou is<something>
# pour nous rappeller que la valeur est soit True ou False


# EXEMPLE où le booléen remplace une expression de comparaison
# Le code ci-dessous change la valeur de isOn entre True et False.
# S'il était False au début, il finit par être True et vice-versa.
# C'est comme le comportement d'un bouton sur un appareil.
isOn = False
print(type(isOn)) # <- 'bool' ou booléen

if isOn: # <- sera vrai si isOn = True
    isOn = False
    print("éteint")
else: # <- si isOn = False
    isOn = True
    print("allumé")

print(isOn)


# EXEMPLE où le booléen est utilisé comme indicateur pour nous
# permettre d'agir plus tard dans le programme au lieu de directement
# à l'intérieur de la séquence de conditions
estOui = False 
print("oui ou non")
choix = input().lower()

# Au lieu de faire quelque chose directement, on change juste
# la valeur de notre indicateur estOui. Cela nous permet de
# développer de la logique plus complexe (ici, demander une
# confirmation en cas de la réponse "non").
if choix == "oui":
    estOui = True
    print("oui...")
elif choix == "non":
    print("non...")
    print("confirme ton choix, SVP. Tu veux oui ou non?")
    choix = input().lower()

    if choix == "oui":
        estOui = True
        print("oui...")
    else:
        print("non... c'est clair.")
else: # capter l'erreur et le présenter à l'utilisateur
    print("je n'ai pas compris la réponse. je présume non")

# Maintenant, on va agir sur la réponse en utilisant la
# valeur de notre indicateur estOui (qui est soit True ou False)
if estOui:
    print("maintenant on joue!")
else:
    print("Au revoir!")

