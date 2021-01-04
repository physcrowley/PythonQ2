from turtle import *

#speed("slowest")  #Pour l'aider a aller plus vite
rayon = 1  #Le premier rayon par défaut
rayonSpiral = 100
while (rayon < rayonSpiral):
    circle(rayon, 180)
    rayon += 7
      #écartement entre 2 demi-cercle de la spirale
input("Press Enter to end program")