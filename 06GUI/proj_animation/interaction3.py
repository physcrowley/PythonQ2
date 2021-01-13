import pgzrun

WIDTH = 600
HEIGHT = 300

alien = Actor("alien.png")
alien.pos = (WIDTH/2, HEIGHT/2)


def draw():
    screen.fill("blue")
    alien.draw()

"""
def update():
    if keyboard.s:
        alien.angle += 90
    if keyboard.d:
        alien.angle -= 90
"""


def on_key_down(key):
    if key == keys.S:
        alien.angle += 90
    if key == keys.D:
        alien.angle -= 90


pgzrun.go()