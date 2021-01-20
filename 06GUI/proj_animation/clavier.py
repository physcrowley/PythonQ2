import pgzrun

ball  = Actor("ballon")


def draw():
    screen.fill("blue")
    ball.draw()


def update():
    # vérifie si la touche est enfoncée et envoie True ou False
    if keyboard.up:
        ball.y -= 10
    if keyboard.down:
        ball.y += 10

"""
def on_key_down(key):
    # vérifie se la touche pressée était une des ces valeurs
    if key == keys.UP:
        ball.y -= 10
    if key == keys.DOWN:
        ball.y += 10
"""

pgzrun.go()
