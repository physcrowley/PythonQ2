import pgzrun

WIDTH = 800
HEIGHT = 200

# Sprite
alien = Actor("alien.png")
alien.pos = (0, HEIGHT / 2)
v_a = 1 # vitesse de l'alien

ball = Actor("ballon.png")
ball.pos = (0, HEIGHT - 30)
v_b = 1 # vitesse du ballon
rotation = 1 # rotation du ballon


def draw():
    """ Tout ce qu'on veut voir dans notre fenêtre"""
    screen.fill("blue")
    alien.draw()
    ball.draw()

def update():
    """Changer des choses entre chaque mise à jour de la fenêtre"""
    alien.x = alien.x + v_a
    ball.x += v_b
    ball.angle -= rotation

pgzrun.go()
# go() lance le programmme Pygame Zero qui utilise les 
# fonctions qu'on a définit ici, comme draw() et update()
# dans une boucle qui se répète jusqu'à 60 fois par seconde