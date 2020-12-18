# conçu pour que la liste `cahier` soit importé par mad_libs_final.py
# qui utilise toutes ces listes de phrases et de consignes

#------Une fonction par "page" d'un cahier Mad Libs------

def page_djc():
    """Page de M. Crowley""" 

    phrases = []
    consignes = []

    # le trou dans la phrase est indiqué par les {}
    phrases.append("Un(e) {} s'en va patiner")
    # chaque consigne spécifie quel type de mot va dans le trou
    consignes.append("personne")

    phrases.append("accompagné(e) par un(e) {} qui")
    consignes.append("personne")

    phrases.append("apporte un(e) {}.")
    consignes.append("objet")

    phrases.append("Soudain un(e) {} arrive")
    consignes.append("véhicule, singulier")

    phrases.append("sur la glace en {}.")
    consignes.append("mouvement, adverbe (finit avec -ant)")

    phrases.append("Les deux héros {}")
    consignes.append("verbe d'action, 3e pers. pluriel")

    phrases.append("le(la) {} pour tenter de")
    consignes.append("même objet qu'avant")

    phrases.append("dévier le(la) {}.")
    consignes.append("même véhicule qu'avant")

    phrases.append("Cela est {}.")
    consignes.append("efficacité (p. ex. très efficace, futile)")

    phrases.append("Le(la) {}")
    consignes.append("toujours le même véhicule")
    
    phrases.append("{} au milieu du canal.")
    consignes.append("verbe de mouvement, 3e pers. singulier")

    phrases.append("Remplis de {} les héros")
    consignes.append("émotion, singulier")

    phrases.append("crient <<Quel(le) {}!>>.")
    consignes.append("activité, singulier")
    

    # les listes de phrases et de consignes sont locales à cette fonction
    # les exporter vers le programme avec le mot-clé return
    return phrases, consignes


def page_damian(): 
    phrases = []
    consignes = []

    phrases.append("George mange son {} pour diner")
    consignes.append("nom commun")
    phrases.append("Ils veut du {} avec sont diner.")
    consignes.append("nom commun")
    phrases.append("Il a déja sont {} avec lui")
    consignes.append("nom commun")

    return phrases, consignes


def page_david():
    phrases = []
    consignes = []

    phrases.append("{} fait des biscuits le jour de la veille de Noël.")
    consignes.append("nom d'une femelle dans ta famille (mère,soeur,enfant...):")
    phrases.append("Elle utilise un {} pour déchiqueter la pâte.")
    consignes.append("outil de la cuisine, nom masculin:")
    phrases.append("Une fois qu'elle a fini de la mettre en pièce, elle a mis les morceaux de la pâte dans le four. Après que les biscuits étaient cuits, elle les a placé sur une {}.")
    consignes.append("nom féminin d'un objet qui peut soutenir des choses.")
    phrases.append("À minuit, Père Noël a réveillé tout le monde quand il a {} avec un très grand bruit.")
    consignes.append("verbe écrit au participe passé et s'accorde avec l'auxiliaire avoir:")
    phrases.append("Les enfants ont reconnu qui les a réveillé, alors ils sont allés voir le Père Noël. Ils l'ont demandé pour des {}.")
    consignes.append("nom commun au pluriel(masculin ou féminin) qui désigne un objet:")
    phrases.append("Le Père Noël a accepté leurs demandes, tout pendant qu'il mangeait des biscuits. Il leur a aussi remercié pour les biscuits en leur donnant des {}.")    
    consignes.append("nom commun au pluriel(masculin ou féminin) qui désigne un objet autre que celui de ci-haut:")

    return phrases, consignes


def page_joseph():
    phrases = []
    consignes = []

    phrases.append("Une {} tombe sur ma tête.")
    consignes.append("nom commun")
    phrases.append("Je vais chez le {} pour me faire vérifier.")
    consignes.append("professionnel, masculin")
    phrases.append("il m'a dit de prendre des {} pour ma douleur")
    consignes.append("nom commun")
    phrases.append("Dans le matin, j'ai demander a {} de me faire une petit collation.")
    consignes.append("(ma) nom commun feminin")
    phrases.append("Mon père a crier apres moi et il m'a {}.")
    consignes.append("Verbe à l'infinitif")
    phrases.append("Il y a plusieurs {} facon de demander de faire ma collation tous seul.")
    consignes.append("Adjectif")
    phrases.append("mon père n'est pas come d'autre {}.")
    consignes.append("nom commun")
    phrases.append("Il se fache tres {}.")
    consignes.append("Adverbe")
    phrases.append("Mais, je l'{}.")
    consignes.append("verbe")
    phrases.append("Mes {} on rit de moi après quils on vuent le gros bump sur ma tete")
    consignes.append("Nom commun")
    phrases.append(" j'ai {}.")
    consignes.append("Verbe à l'infinitif")
    phrases.append(" Mes parent on senti ma et ils ont m'acheter un {}.")
    consignes.append("Nom commun")

    return phrases, consignes


def page_nicholas():
    phrases = []
    consignes = []

    phrases.append("Aujourd'hui nous allons au restarant {} .")
    consignes.append("nom propre")
    phrases.append(" car on c'est mon {} aujourdh'hui.")
    consignes.append("un célébration")
    phrases.append(" Le president ma donner 50$ pour manger des {}.")
    consignes.append(" nom propre ")
    phrases.append(" mais le {} a manger mon argen ")
    consignes.append("nom comun")
    phrases.append(" Aprée {} on quit le restarant ")
    consignes.append("temp")
    phrases.append("quand soudainement un {} nous attacke")
    consignes.append(" nom comun")
    phrases.append("Avec le aide de {} on le/la arréte")
    consignes.append("superhéro")
    phrases.append("pour célébré tout mond comence a {}")
    consignes.append("verbe")

    return phrases, consignes


def page_samir():
    phrases = []
    consignes = []

    phrases.append("Vous allez chez le/la/l' {}")
    consignes.append("lieu")

    phrases.append("Vous entrez pour prendre un/une {}")
    consignes.append("objet")

    phrases.append("Vous quittez pour le donner au {}")
    consignes.append("personne")

    phrases.append("Il vous dit {}")
    consignes.append("mot")

    phrases.append("Vous êtes maintenant {}")
    consignes.append("adjectif")

    phrases.append("Vous quittez pour aller chez {} ")
    consignes.append("lieu")

    phrases.append("Vous êtes là pour {}")
    consignes.append("verbe")

    return phrases, consignes


def page_():
    phrases = []
    consignes = []



    return phrases, consignes


#----Regrouper toutes les "pages" dans une liste cahier----
cahier = [page_djc, page_damian, page_david, page_joseph, page_nicholas, page_samir]
