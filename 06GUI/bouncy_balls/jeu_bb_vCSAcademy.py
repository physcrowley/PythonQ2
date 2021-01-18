""" Bouncy ball remake using the CS Academy graphics framework 
from a Pygame Zero code base. The Group object and its 'visible' property
really changed and simplified the screen-changing logic of the game.

Must be run on CS Academy's sandbox : https://academy.cs.cmu.edu/ide
or with their graphics modules installed locally : https://academy.cs.cmu.edu/desktop

David Crowley
2020-01-18
"""

from random import randint

# App - automatically draws all visible objects
app.background = 'black'
app.stepsPerSecond = 30
WIDTH = 400     # both must be 400
HEIGHT = 400    #  - they are used to check for the wall and floor

# Game colours
colors = ["white", "green", "red", "blue"]

def toggle_color(color):
    """ Traverser de façon circulaire les couleurs disponibles
    :param color: la couleur actuelle
    :return: la prochaine couleur
    """
    i = colors.index(color)
    if i == len(colors) - 1:
        return colors[0]
    return colors[i + 1]


# Gameplay elements
score = 0
max_score = score
prompt = Label("Click without touching the existing balls.", 10, 10, align='left-top', fill = 'yellow')
score_text = Label("Score: " + str(score), 280, 10, align = 'left-top', size = 24, fill = 'cyan')
first_ball = Circle(200, 200, 25, fill = 'magenta')
first_ball.dx = 150 / app.stepsPerSecond
first_ball.dy = 200 / app.stepsPerSecond
balls = Group()

play = Group(balls, prompt, score_text)


# Game over elements
since_died = 0
game_over = Label("GAME OVER", 200, 200, size = 42, fill = 'magenta')

end = Group(game_over, visible = False)


# Replay elements
yes_box = Rect(45, 125, 150, 150, fill = 'green')
no_box = Rect(205, 125, 150, 150, fill = 'red')
again = Label("Play again? Click to chose.", yes_box.left, yes_box.top - 20, align = 'left-top', size = 18, fill = 'white')
yes = Label("YES", yes_box.centerX, yes_box.centerY, size = 36)
no = Label("NO", no_box.centerX, no_box.centerY, size = 36)

replay = Group(yes_box, no_box, again, yes, no, visible = False)


# State-changing functions

def change_color(ball):
    """Changer la couleur"""
    ball.fill = toggle_color(ball.fill)


def game_over_screen():
    if not end.visible:
        end.visible = True
        play.visible = False


def replay_screen():
    if not replay.visible: 
        replay.visible = True
        end.visible = False


def reset_game():
    """Réinitialiser le Group de balles et les variables du jeu"""
    global score
    
    balls.clear()
    first_ball.centerX = 200
    first_ball.centerY = 200
    balls.add(first_ball)
    
    score = 0
    since_died = 0
    play.visible = True
    replay.visible = False
    

# Initialise the game
reset_game()

# Game logic

def onMousePress(x, y):
    """Toute la logique du jeu et de la fin du jeu"""
    
    global since_died, score, max_score
    
    if replay.visible:
        if no_box.hits(x, y):
            replay.visible = False
            app.stop()
        elif yes_box.hits(x, y):
            reset_game()
    
    elif play.visible:
        if balls.hitTest(x, y):
            # fin du jeu
            print("Final score:", score)
            if score > max_score:
                max_score = score
                print("   *** New high score! *** ")
            game_over_screen()
        else:
            # ajouter une nouvelle balle avec son centre à l'intérieur du cadre
            pad = 55
            if x < pad:
                x = pad
            elif x > WIDTH - pad:
                x = WIDTH - pad
            if y < pad:
                y = pad
            elif y > HEIGHT - pad:
                y = HEIGHT - pad
            
            new_ball = Circle(x, y, randint(10, 50), fill = colors[randint(1, len(colors) - 1)])
            new_ball.dx = randint(-400, 400) / app.stepsPerSecond
            new_ball.dy = randint(-400, 400) / app.stepsPerSecond
            balls.add(new_ball)
            
            # augmenter le pointage
            score += 1
            score_text.value = "Score: " + str(score)


def onStep():
    """Déplacer les  balles ou afficher le message de fin """
    global since_died
    
    if play.visible:
        for i, ball in enumerate(balls):
            # mettre à jour la position
            ball.centerX += ball.dx
            ball.centerY += ball.dy
            # rebondir aux bords
            if ball.left <= 0 or ball.right >= WIDTH:
                ball.dx = -ball.dx
                # changer la couleur aux murs de côté, sauf la balle initiale
                if i > 0:
                    change_color(ball)  
            if ball.top <= 0 or ball.bottom >= HEIGHT:
                ball.dy = -ball.dy
    
    elif end.visible:
        # attendre 2 secondes avant d'afficher les options
        since_died += 1
        if since_died > 2 * app.stepsPerSecond:
            replay_screen()