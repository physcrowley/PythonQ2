# Exemples et notes

Ce site inclut les exemples de code qui sont développés en classe. (test de CR)

## Structure de dossiers

Ce dossier `PythonQ2` est le dossier qui contient tout le code du semestre. C'est l'équivalent de votre **espace de travail** personnel.

Chaque concept se trouve dans un dossier séparé, comme chacun de vos dossiers de **projet**.

Les **fichiers** :

* Dans chaque dossier, il y aura généralement un `README.md` qui s'affiche sur le site de GitHub et qui contient des détails en lien avec chaque concept.
* Il y a également un ou plusieurs fichiers `.py` qui incluent des exemples de code. Il y aura des commentaires dans ces fichiers qui expliquent aussi la logique du script Python.

## Fichiers spécifiques à repl.it

Plusieur fichiers de configuration sont créées sur repl.it afin de simplifier le lancement de projets via le serveur.

**Toujours présent** :

* `.replit` qui spécifie surtout quoi faire avec le bouton `Run`, notamment en donnant la commande à exécuter via la console.

> On modifie manuellement le fichier `.replit`

**Présents pour des projets qui incluent des modules comme `pgzero`** :

* `pyproject.toml` qui indique quels modules doivent être inclus dans le projet
* `poetry.lock` qui inclut un paquet de détails spécifiques sur les versions des modules à chercher

> Ces deux fichiers sont générés automatiquement par repl.it. N'ayez pas peur de la complexité de leur contenu! Vous pouvez les ignorer s'ils sont présents.
