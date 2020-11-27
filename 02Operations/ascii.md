# Tableau ASCII

Les 128 premiers caractères - affichés de façon uniforme sur toutes les plateformes - se trouvent dans le tableau ASCII (ou au début des autres tableaux, comme le tableau Unicode).

L'ordinateur conserve les caractères en mémoire comme des chiffres et utilise le tableau ASCII pour choisir le bon caractère à afficher sur le périphérique de sortie - l'écran, l'imprimante, etc.

Voici une version du tableau. Il y a trois colonnes :

Decimal | Hex | Char
--- | --- | ---
L'entier (base 10) utilisé pour représenter le caractère | Le même nombre en base 16 (hexadécimal) | Le caractère à afficher

---

![Lien vers le tableau ASCII](https://wayhome25.github.io/assets/post-img/cs/ASCII-Table.png)

## Fonctions Python

Si tu as un caractère, tu peux trouver sa valeur numérique (base 10 / décimal) avec la fonction `ord`.

```python
ord('c') # 99, remplace c avec le caractère que tu veux
```

Si tu as un nombre et tu veux obtenir le caractère, tu peux utiliser la fonction `chr`.

```python
chr('111') # 'o', remplace 111 avec le nombre que tu veux
```

C'est aussi utile de savoir qu'il y a toujours une différence de 32 entre les lettres majuscules et leur équivalent minuscule. 'c' est 32 plus haut dans le tableau que 'C'. 'A' est 32 moins haut dans le tableau que 'a'. C'est pratique si tu veux écrire un programme pour changer la case des lettres.
