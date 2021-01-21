"""
Exemple de comment changer la vue selon une condition dans votre application
"""

import pgzrun

WIDTH = 800
HEIGHT = 600

welcome = True
alive = True
start_button = Rect(200, 150, 400, 300)


# ASTUCE : définir une fonction qui contient des commandes pour draw() pour chacune
# des vues dans votre application
#
# Dans draw(), appeler la fonction appropriée en utilisant des conditions if-elif-else

def welcome_screen():
    """Define elements for draw() if we are on the welcome screen"""
    screen.fill("lightgray")
    screen.draw.textbox("Press to start", start_button, color = "blue", background = "black")

def game_screen():
    """Define elements for draw() if we are on the game screen"""
    screen.fill("blue")

def gameover_screen():
    screen.clear()

def draw():
    if welcome:
        welcome_screen()
    elif alive:
        game_screen()
    else:
        gameover_screen()

def on_mouse_down(pos):
    global welcome
    if welcome and start_button.collidepoint(pos):
        welcome = False
    if not welcome: # logique de jeu
        pass

def update():
    global alive
    if (not welcome) and keyboard.space:
        alive = False


pgzrun.go()