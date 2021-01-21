"""
Exemple de comment changer la vue selon une condition dans votre application
"""

import pgzrun

WIDTH = 800
HEIGHT = 600

welcome = True
alive = True
start_button = Rect(200, 150, 400, 300)

# ASTUCE : 
# Dans draw(), suivre la liste de commandes appropriées en utilisant des conditions if-elif-else

def draw():
    if welcome: 
        # dessiner l'écran d'accueil
        screen.fill("lightgray")
        screen.draw.textbox("Press to start", start_button, color = "blue", background = "black")
    elif alive: 
        # dessiner la vue active du jeu
        screen.fill("blue")
    else: 
        # dessiner l'écran game over
        screen.clear()

def on_mouse_down(pos):
    global welcome, alive
    if welcome and start_button.collidepoint(pos):
        # si on est sur l'écran d'acceuil et on clique le bouton
        welcome = False
    if (not welcome) and alive: 
        # logique de jeu
        pass

def update():
    global alive
    if (not welcome) and keyboard.space:
        # on meurt si on pèse sur 'space' (si on n'est pas sur l'écran d'accueil)
        alive = False


pgzrun.go()