import pgzrun

WIDTH = 800
HEIGHT = 200

# Sprite
alien = Actor("alien.png")
alien.pos = (0, HEIGHT / 2)
vx_a = 2 # vitesse x de l'alien
vy_a = 1 # vitesse y de l'alien


def draw():
    """ Tout ce qu'on veut voir dans notre fenêtre"""
    screen.fill("blue")
    alien.draw()

def update():
    """Changer des choses entre chaque mise à jour de la fenêtre"""
    global vx_a, vy_a
    
    if (alien.x < 0 or alien.x > WIDTH):
        vx_a = -vx_a # change la direction
    if (alien.y < 0 or alien.y > HEIGHT):
        vy_a = -vy_a
    
    alien.x += vx_a
    alien.y += vy_a

pgzrun.go()
# go() lance le programmme Pygame Zero qui utilise les 
# fonctions qu'on a définit ici, comme draw() et update()
# dans une boucle qui se répète jusqu'à 60 fois par seconde