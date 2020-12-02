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


# un exemple
estBon = False
print(type(estBon))

if estBon:
    print("bravo, on continue")
else:
    estBon = True
    print("maintenant on est bon")

print(estBon)


# try-except -> structure comme if-else mais ou le code dans le
# try peut faire planter le programme
# * les conversions int() et float() par exemple
