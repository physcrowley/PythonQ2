import pgzrun

WIDTH = 600
HEIGHT = 300

alien = Actor("alien.png")
alien.pos = (WIDTH/2, HEIGHT/2)
speed = 1 # nombre de pixels par update

def draw():
    screen.fill("white")
    alien.draw()

def on_mouse_move(pos):
    alien.pos = pos

pgzrun.go()