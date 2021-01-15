Label("Exemple d'une balle qui bondit", 200, 20, size=20)
ball = Circle(200, 200, 20, fill = 'blue')

vx = 5
vy = 3

def onKeyPress(key):
    # cliquer sur SPACE pour arrêter le jeu
    if key == 'space':
        app.stop()
        Label("fin", 200, 380, size = 10)

def onStep(): # équivalent de update() dans Pygame Zero
    global vx, vy
    
    ball.centerX += vx
    ball.centerY += vy
    
    if ball.centerX > 400 or ball.centerX < 0:
        vx = -vx
    if ball.centerY > 400 or ball.centerY < 0:
        vy = -vy
