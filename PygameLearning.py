import pygame
import math
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Block and Ball Game")
font = pygame.font.SysFont(None,30)

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    WIN.blit(screen_text,(x,y))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
exit_game = False


class Box():

    def __init__(self,height,width,color,y,x):
        self.height = height
        self.width = width
        self.vely = 0
        self.color = color
        self.y = y
        self.x = x
    
    def update_val(self,value):
        self.vely = value

    def update_pos(self):
        self.y+=self.vely
    def get_y(self):
        return self.y
    def get_x(self):
        return self.x


class Ball():
    def __init__(self,radius,color,y,x):
        self.radius = radius
        self.velx = 0
        self.vely = 0
        self.color = color
        self.y = y
        self.x = x
    
    def update_pos(self):
        self.y+=self.vely
        self.x+=self.velx
    
    def get_y(self):
        return self.y

    def get_x(self):
        return self.x


BOX_HEIGHT = 70
BOX_WIDTH = 10
RADIUS = 10
bx1 = Box(BOX_HEIGHT,BOX_WIDTH,WHITE,HEIGHT/2,0)
bx2 = Box(BOX_HEIGHT,BOX_WIDTH,WHITE,HEIGHT/2,WIDTH-BOX_WIDTH)
ball = Ball(RADIUS,RED,random.randint(50,HEIGHT-50),WIDTH/2)

def plot_box(box):
    pygame.draw.rect(WIN,box.color,(box.x,box.y,box.width,box.height))

def plot_ball(ball):
    pygame.draw.circle(WIN, ball.color, (ball.x,ball.y), ball.radius)

def is_Collision(box):
    if box.get_y() <= 0:
        box.y = 0
        box.vely = -box.vely
    elif box.y >= HEIGHT - BOX_HEIGHT:
        box.y = HEIGHT - BOX_HEIGHT
        box.vely = -box.vely

def is_edge_collision_ball(ball):
    if ball.get_y()>= HEIGHT-RADIUS:
        ball.y = HEIGHT-RADIUS
        ball.vely = -ball.vely
    elif ball.get_y() <= 0:
        ball.y = 0
        ball.vely = -ball.vely


def is_box_collision_ball(box,ball):
    if abs(ball.x-box.x)<=10 and abs(ball.x-box.x)>0 and abs(ball.y-box.y)<=box.height/2 and abs(ball.y-box.y)>=0:
        ball.velx = -ball.velx
        ball.vely = -ball.vely
        return True
    elif abs(ball.x-box.x)<=10 and abs(ball.y-box.y)<=box.height and abs(ball.y-box.y)>box.height/2:
        ball.velx = -ball.velx
        ball.vely = ball.vely
        return True
    return False

vel_update_box = 0.4
vel_update_ball = 0.2
def bx1_ai(box, ball):
    if ball.velx < 0:  # Only move if the ball is moving towards bx1
        if ball.y < box.y + box.height / 2:
            box.update_val(-vel_update_box)
        elif ball.y > box.y + box.height / 2:
            box.update_val(vel_update_box)
            

def game_over_ball_out(ball):
    if ball.x<0 or ball.x>WIDTH:
        return True
    return False
def game_loop():
    bx1 = Box(BOX_HEIGHT,BOX_WIDTH,WHITE,HEIGHT/2,0)
    bx2 = Box(BOX_HEIGHT,BOX_WIDTH,WHITE,HEIGHT/2,WIDTH-BOX_WIDTH)
    ball = Ball(RADIUS,RED,random.randint(50,HEIGHT-50),WIDTH/2)
    game_over = False
    ball_vel_choice = [(-vel_update_ball,vel_update_ball),(vel_update_ball,-vel_update_ball),(vel_update_ball,vel_update_ball),(-vel_update_ball,-vel_update_ball)]
    ball.velx ,ball.vely = random.choice(ball_vel_choice)
    exit_game = False
    score = 0
    while not exit_game:

        if game_over:
            WIN.fill(BLACK)
            text_screen("GAME OVER PRESS ENTER TO PLAYYYY!!!!",RED,WIDTH/2-200,HEIGHT/2)
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            game_loop()
        else:
            WIN.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        bx2.update_val(-vel_update_box)
                    if event.key == pygame.K_DOWN:
                        bx2.update_val(vel_update_box)
                    if event.key == pygame.K_w:
                        bx1.update_val(-vel_update_box)
                    if event.key == pygame.K_s:
                        bx1.update_val(vel_update_box)
                
            game_over = game_over_ball_out(ball)
            is_Collision(bx1)
            is_Collision(bx2)
            bx1_ai(bx1,ball)
            is_edge_collision_ball(ball)
            is_box_collision_ball(bx1,ball)
            if is_box_collision_ball(bx2,ball):
                score+=10
                print(score)
            text_screen("SCORE "+str(score),RED,(WIDTH/2)-100,50)
            bx1.update_pos()
            bx2.update_pos()
            plot_box(bx1)
            plot_box(bx2)
            
            ball.update_pos()
            plot_ball(ball)
        pygame.display.update()
    pygame.quit()
    quit()

game_loop()