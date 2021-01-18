"""Clicky Ball
Cliquer pour créer des balles sans cliquer sur une balle existente
Auteur: David Crowley, crowlda@ecolecatholique.ca
Date : 2020-01-10, révision Pygame Zero : 2020-05-27
"""

from random import randint
import sys
import pgzrun

# Couleurs
colors = ["black", "white", "green", "red", "blue"]
bkgd_color = "black"
shdw_color = (50, 50, 50)  # gray
shdw_offset = 4  # shadow offset in pixels

def toggle_color(color):
    """ Traverser de façon circulaire les couleurs disponibles
    :param color: la couleur actuelle
    :return: la prochaine couleur
    """
    i = colors.index(color)
    if i == len(colors) - 1:
        return colors[0]
    return colors[i + 1]

# Fenêtre
WIDTH = 800
HEIGHT = 600
end_box = Rect(WIDTH / 8, HEIGHT / 8, WIDTH * 0.75, HEIGHT * 0.75)
yes_box = Rect(175, 225, 200, 150)
no_box = Rect(425, 225, 200, 150)

# Variables de jeu initiales
game_over = False
just_died = 0
score = 0
max_score = score

def game_over_screen():
    """Afficher pendant un compte de 120 (~2secondes)"""
    global just_died
    screen.draw.textbox("GAME OVER", end_box, color = (255, 0, 255))
    just_died += 1 #update() = 60 fois par s... just_died < 120 pendant ~2 secondes


def replay_screen():
    """Choisir de jouer encore ou de quitter le jeu"""
    screen.draw.text("Play again? Click to chose.", (yes_box.x, yes_box.y - 50))
    screen.draw.filled_rect(yes_box, "green")
    screen.draw.textbox("YES", yes_box, color = "black")
    screen.draw.filled_rect(no_box, "red")
    screen.draw.textbox("NO", no_box, color = "black")


class Ball:
    """Definir une balle"""
    def __init__(self, radius = 0, pos = (0, 0), velocity = [0, 0]):
        self.r = radius
        self.rect = Rect(pos[0] - self.r, pos[1] - self.r, 2 * self.r, 2 * self.r)
        self.v = velocity
        self.color = colors[randint(1, len(colors) - 1)]
    
    def change_color(self):
        """Changer la couleur"""
        self.color = toggle_color(self.color)
        if self.color == bkgd_color:
            self.color = toggle_color(self.color)


def reset_balls(ball_list):
    """Vider la liste des balles et créer la première balle
    :param ball_list: la liste des balles
    :return: la liste réinitialisée
    """
    ball_list = []
    ball_list.append(Ball(25, (WIDTH // 2, HEIGHT // 2), [500 / 60, 500 / 60]))
    ball_list[0].color = (255, 0, 255)  # set unique color (magenta) for this ball
    return ball_list

balls = []
balls = reset_balls(balls)

def on_mouse_down(pos):
    """Toute la logique du jeu et de la fin du jeu"""
    global game_over, just_died, balls, score, max_score
    X, Y = pos  
    if game_over:
        # options de continuer le jeu
        if no_box.collidepoint(pos):
            sys.exit()
        elif yes_box.collidepoint(pos):
            game_over = False
            just_died = 0
            balls = reset_balls(balls)
    else:
        for ball in balls:
            # si le clic est sur une balle existente
            if ball.rect.collidepoint(pos):
                print("Final score:", score)
                # mettre à jour les pointages
                if score > max_score:
                    max_score = score
                    print("   *** New high score! *** ")
                game_over = True
                score = 0
        # sinon, créer une nouvelle balle avec une taille et une vitesse aléatoire
        if not game_over:
            # ajuster la position de la souris à l'intérieur du cadre, au besoin
            if X < 60:
                X = 60
            elif X > WIDTH - 60:
                X = WIDTH - 60
            if Y < 60:
                Y = 60
            elif Y > HEIGHT - 60:
                Y = HEIGHT - 60
            b = balls.pop()
            balls.append(Ball(randint(10, 50),
                              (X, Y),
                              [randint(-400, 400) / 60, randint(-400, 400) / 60]))
            balls.append(b) # pop et append pour garder la 1e balle à la fin de la liste
            score += 1


def update():
    """Déplacer les  balles"""
    if not game_over:
        for i, ball in enumerate(balls):
            # mettre à jour la position
            ball.rect.move_ip(ball.v)
            # rebondir aux bords
            if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
                ball.v[0] = -ball.v[0]
                # changer la couleur aux murs de côté, sauf la balle initiale
                if i < len(balls) - 1:
                    ball.change_color()  
            if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
                ball.v[1] = -ball.v[1]


def draw():
    screen.fill(bkgd_color)
    if game_over and just_died < 120:
        game_over_screen()
    elif game_over:
        replay_screen()
    else:
        for ball in balls:
            # tracer l'ombre
            screen.draw.filled_circle(
                (ball.rect.centerx + shdw_offset, ball.rect.centery + shdw_offset),
                ball.r, shdw_color)
            # tracer la balle
            screen.draw.filled_circle((ball.rect.center), ball.r, ball.color)
        # superposer les éléments de texte
        screen.draw.text("Click without touching the existing balls.", (200, 15), color = (255, 255, 0))
        score_text = "Score: " + str(score)
        screen.draw.text(score_text, (WIDTH - 100, 15), color = (0, 255, 255))

pgzrun.go()