# Pygame Zero

Pour tous les exemples et projets que nous développions dans ce cours nous ferons référence à deux documents.

1. Le site de [Pygame Zero](https://pgzero-french.readthedocs.io/fr/latest/index.html)
2. La [présentation](https://docs.google.com/presentation/d/10Gv1qQwPNnl53i2rwbcGB4s1hFUnhd0nQ4N8QVpZQWU/view) sur des concepts de base

## Installation

### Sur Repl.it

Il n'y a aucune installation explicite à faire. Vous devez simplement lancer le programme test dans la section suivante à partir d'un nouveau dossier de projet dans votre espace de travail, et le serveur de repl.it s'occupera d'ajouter les modules nécessaires à ton espace de travail.

### Sur ordinateur

> Cette option est **fortement recommandée** si vous avez un ordinateur Windows/Mac/Linux car les projets Pygame sont plus demandant sur le serveur de repl.it et le font planter plus souvent que d'habitude.

Étapes à suivre :

1. Ouvrir la console **en tant qu'administrateur** (menu Windows > taper `cmd.` > choisir "Exécuter en tant qu'administrateur")
2. Taper la commande `pip install pgzero` ou `python -m pip install pgzero`

> ⚠ Si vous n'ouvrez pas la console en tant qu'administrateur, Pygame Zero ne sera pas installé dans le même dossier que Python (il sera installé dans ton dossier utilisateur) et pourrait ne pas fonctionner avec VS Code.`

## Test de l'installation

Copier le code du fichier [pgzero_test.py](pgzero_test.py), soit les lignes suivantes, dans un nouveau dossier de projet et le lancer via repl.it ou VS Code.

```python
import pgzrun

pgzrun.go()
```

Si ton installation est correcte :

1. la console affichera des lignes semblables à :
    ```bash
    pygame 1.9.6
    Hello from the pygame community. https://www.pygame.org/contribute.html
    ```
2. une fenêtre vide sera créer après quelques instants.
