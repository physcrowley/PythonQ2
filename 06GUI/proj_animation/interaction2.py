import pgzrun

WIDTH = 600
HEIGHT = 300

alien = Actor("alien.png")
alien.pos = (WIDTH/2, HEIGHT/2)
speed = 1 # nombre de pixels par update

p_text = ""
a_text = ""

def draw():
    screen.fill("blue")
    alien.draw()
    screen.draw.text(p_text, (10,10), color = "white")
    screen.draw.text(a_text, (10,30), color = "white")

def on_mouse_move(pos):
    global p_text, a_text
    p_text = "Position: " + str(pos)
    alien.angle = alien.angle_to(pos)
    a_text = "Angle: " + str(round(alien.angle))


pgzrun.go()