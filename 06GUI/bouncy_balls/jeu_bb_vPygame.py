"""
@title : Clicky Ball
@description : Simple game with bouncing balls created where you click until you click on an existing ball
@author : David Crowley
@date : 2020-01-10, updated 2020-05-28
"""

import pygame
from random import randint

# ---------------+SETUP+--------------------

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
colors = [BLACK, WHITE, GREEN, RED, BLUE]
bkgd_color = BLACK
shdw_color = (50, 50, 50)  # gray
shdw_offset = 4  # shadow offset in pixels


def change_color(color):
    # function to change colors by traversing the colors list
    i = colors.index(color)
    if i == len(colors) - 1:
        return colors[0]
    return colors[i + 1]


# Create window
pygame.init()
MAX_X = 800
MAX_Y = 600
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("Clicky Ball")
# Manage how fast the screen updates
fps = 60
clock = pygame.time.Clock()

# text elements
font = pygame.font.SysFont('Calibri', 25, True, False)
title_text = font.render("Click without touching the existing balls.", True, (255, 255, 0))
end_text = font.render("GAME OVER", True, (255, 0, 255))
replay_text = font.render("Play again? Click to chose.", True, WHITE)
yes_text = font.render("YES", True, BLACK)
no_text = font.render("NO", True, BLACK)

# replay game options
yes_box = pygame.Rect(175, 225, 200, 150)
no_box = pygame.Rect(425, 225, 200, 150)

class Ball:
    # define ball object
    def __init__(self, radius = 0, pos = (0, 0), velocity = [0, 0]):
        self.r = radius
        self.v = velocity
        self.color = colors[randint(1, len(colors) - 1)]
        self.rect = pygame.Rect(pos[0] - self.r, pos[1] - self.r, 2 * self.r, 2 * self.r)

        # # create a semi-transparent surface for drawing the ball
        # # (this option was replaced with a simple ball shadow for performance reasons)
        # self.sfc = pygame.Surface((2 * self.r, 2 * self.r)).convert()
        # self.sfc.set_colorkey(bkgd_color)
        # self.sfc.set_alpha(ALPHA)    # ALPHA was set to 128

    def change(self):
        # changes ball color and makes sure it is not the same as the background color.
        self.color = change_color(self.color)
        if self.color == bkgd_color:
            self.color = change_color(self.color)


def reset_balls(ball_list):
    # clears the balls list and creates a new first ball
    ball_list = []
    ball_list.append(Ball(25, (MAX_X // 2, MAX_Y // 2), [500 / 60, 500 / 60]))
    ball_list[0].color = (255, 0, 255)  # set unique color (magenta) for this ball
    return ball_list


# initialize ball list
balls = []
balls = reset_balls(balls)

# initial game states
running = True
game_over = False
score = 0
max_score = score

# -------- Main Program Loop -----------
while running:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            X, Y = pygame.mouse.get_pos()
            if game_over:
                # if clicked on NO
                if no_box.collidepoint(X, Y):
                    running = False
                    break
                # if clicked on YES
                elif yes_box.collidepoint(X, Y):
                    game_over = False
                    balls = reset_balls(balls)
            else:
                # if clicked on a ball, GAME OVER
                for ball in balls:
                    if ball.rect.collidepoint(X, Y):
                        game_over = True
                        print("Final score:", score)
                        # update high score and reset score
                        if score > max_score:
                            max_score = score
                            print("   *** New high score! *** ")
                        score = 0
                        # freeze the screen with GAME OVER text
                        screen.blit(end_text, (10, 10))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                # otherwise, create a new ball where you clicked
                if not game_over:
                    # set mouse position inside the frame if necessary
                    if X < 60:
                        X = 60
                    elif X > MAX_X - 60:
                        X = MAX_X - 60
                    if Y < 60:
                        Y = 60
                    elif Y > MAX_Y - 60:
                        Y = MAX_Y - 60
                    # add new ball, keeping the first ball on top
                    b = balls.pop()
                    balls.append(Ball(randint(10, 50),  # random radius
                                      (X, Y),  # at mouse position
                                      [randint(-400, 400) / 60, randint(-400, 400) / 60]))  # random velocity
                    balls.append(b)
                    score += 1
    # --- Update positions
    if not game_over:
        for i, ball in enumerate(balls):
            # update position of each ball
            ball.rect.move_ip(ball.v)
            # change direction at edges
            if ball.rect.left <= 0 or ball.rect.right >= MAX_X:
                ball.v[0] = -ball.v[0]
                # change color at side walls for all balls but the first
                if i != len(balls) - 1:
                    ball.change()  
            if ball.rect.top <= 0 or ball.rect.bottom >= MAX_Y:
                ball.v[1] = -ball.v[1]
    # --- Drawing code
    screen.fill(bkgd_color)
    if game_over:
        screen.blit(replay_text, (yes_box.x, yes_box.y - 50))
        pygame.draw.rect(screen, GREEN, yes_box)
        screen.blit(yes_text, yes_box.center)
        pygame.draw.rect(screen, RED, no_box)
        screen.blit(no_text, no_box.center)
    else:
        for ball in balls:
            pygame.draw.circle(screen, shdw_color,
                               [ball.rect.centerx + shdw_offset, ball.rect.centery + shdw_offset],
                               ball.r)  # ball's shadow
            pygame.draw.circle(screen, ball.color, ball.rect.center, ball.r)  # ball
        screen.blit(title_text, (200, 15))
        score_text = font.render("Score: " + str(score), True, (0, 255, 255))
        screen.blit(score_text, (MAX_X - 150, 15))
    # --- Update the screen
    pygame.display.flip()
    # --- Define refresh rate
    clock.tick(fps)
# Close the window and quit.
pygame.quit()