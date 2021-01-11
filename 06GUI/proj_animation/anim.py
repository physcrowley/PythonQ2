import pgzrun

WIDTH = 800
HEIGHT = 200

# Sprite
alien = Actor("alien.png")
alien.pos = (0, HEIGHT / 2)
speed = 1


def draw():
    """ Tout ce qu'on veut voir dans notre fenêtre"""
    screen.fill("blue")
    alien.draw()

def update():
    """Changer des choses entre chaque mise à jour de la fenêtre"""
    alien.x = alien.x + speed

pgzrun.go()
# go() lance le programmme Pygame Zero qui utilise les 
# fonctions qu'on a définit ici, comme draw() et update()
# dans une boucle qui se répète jusqu'à 60 fois par seconde