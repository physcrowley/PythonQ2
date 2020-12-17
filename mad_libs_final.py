import os # pour effacer la console
from histoires import cahier # pour inclure les histoires dans l'autre fichier

# Jeu Mad Libs
#
# Histoires écrites par les élèves du cours ICS3U
# Code produit par l'enseignant M. David Crowley
#
# Les histoires qui forment le cahier ont été bougés dans
# un 2e fichier et la liste a été importée. Alors seulement
# la logique pour choisir et faire le jeu reste ici.
#
# 2020-12-16
#


#-----Une fonction pour saisir le choix de menu---------

# Former le texte complet du message d'accueil 
accueil  = f"Il y a {len(cahier)} pages dans ce cahier 'Mad Libs' fait par les élèves ICS3U.\n"
accueil += f"> Indiquer un nombre entre 1 et {len(cahier)} pour choisir une page à faire.\n"
accueil +=  "> Sinon, taper la lettre Q pour quitter le programme."
    # noter la façon plus directe de formatter le texte : f"...{valeur}..."

def get_choice(pages_faites):
    # messages
    print(accueil)
    print(f"\t Rappel : Vous avez déjà fait les pages suivantes : {pages_faites}")
    
    # réponse
    choix = input()
    print() # ligne vide

    # traitement de la réponse
    if choix.isdigit():
        choix = int(choix)
        if choix > 0 and choix <= len(cahier) : # une page valide
            return choix 
        else:
            print("Ce numéro de page n'est pas valide.")
            return get_choice(pages_faites) # répéter la fonction (récursivité)
    
    elif choix.lower() == 'q': # quitter
        print("Merci d'avoir joué. Au revoir!")
        return -1 # page impossible -> signale de quitter la boucle du jeu
    
    else:
        print("Ce choix n'est pas une option valide.")
        return get_choice(pages_faites) # répéter la fonction (récursivité)


#------Boucle du jeu--------
# se rappeler des choix antérieurs
fait = {} # ensemble ('set') vide mais aussi un dictionnaire ('dict') vide

while True:
    # obtenir la page à faire (ou le choix de quitter)
    page = get_choice(fait)

    # traitement du choix
    if page <= 0 : break # quitter la boucle

    else: # ajouter la page à l'ensemble des pages faits

        # {} est interprété comme un 'dict' vide, alors il faut le convertir à un 'set'
        if len(fait) == 0: fait = set(fait)
        
        # dans tous les cas ...
        fait.add(page) 

    # obtenir les phrases et les consignes de la page choisie
    phrases_a_montrer, consignes_a_montrer = cahier[page - 1]()
        # page - 1 : convertir entre 1e page = 1 à 1e élément = 0
        # cahier[page - 1] retourne la fonction (les commandes) pour la page. 
        # ajouter les () exécute la fonction

    # Obtenir les réponses de l'utilisateur
    mots = [] # liste vide
    n = 1 # 1e mot
    for c in consignes_a_montrer: # pour chaque consigne c...
        print(f"{n}-Taper ce type de mot : {c}")
            # les valeurs entre {} seront insérés dans le texte
        
        mots.append(input()) # ajouter le mot entré à la liste
        
        n += 1 # monter le nombre de mots saisis pour signaler le progrès

    # Afficher le résultat
    print("Taper sur Enter pour voir le résultat...")
    input() # attendre

    print("---début---\n")
    for i in range(len(phrases_a_montrer)): # pour chaque phrase à l'index i...
        print(phrases_a_montrer[i].format(mots[i]))
            # print() utilise la méthode .format() qui remplace les {}
            # dans la phrase avec le mot dans le .format()
    print("\n---fin---\n")

    # Attendre avant la prochaine boucle
    print("Taper sur Enter pour continuer...")
    input() # attendre

    # Effacer la console
    os.system('clear') # utiliser avec bash (Linux [incluant repl.it] et MacOS)
    #os.system('cls') # utiliser avec command prompt (Windows)
