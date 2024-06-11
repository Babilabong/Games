import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Babila starship war!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)


blue = 0
red = 1
yellow = 2

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
CHOOSE_SPACESHIP_FONT = pygame.font.SysFont('comicsans', 20)
PLAYER_CHOOSE_FONT = pygame.font.SysFont('comicsans', 35)
START_TIMER_FONT = pygame.font.SysFont('comicsans',50)

FPS = 60
VEL = [5, 5, 3]
BULLET_VEL = [7, 9, 7]
MAX_BULLETS = [5, 4, 7]
LIFE = [10, 8, 9]
COLOR = [BLUE, RED, YELLOW]
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
EXSPLOSION_WIDTH, EXSPLOSION_HEIGHT = 40,40


LEFT_HIT = pygame.USEREVENT + 1
RIGHT_HIT = pygame.USEREVENT + 2
BULLET_HIT = pygame.USEREVENT + 3

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

BLUE_SPACESHIPE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'spaceship_navy2.png')), (200, 200))
RED_SPACESHIPE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png')), (200, 200))
YELLOW_SPACESHIPE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png')), (200, 200))


def draw_spaceship_data(turn):
    for i in range(3):
        draw_text = CHOOSE_SPACESHIP_FONT.render("movement speed = " + str(VEL[i]), 1, WHITE)
        WIN.blit(draw_text, (100+250*i, 260))

        draw_text = CHOOSE_SPACESHIP_FONT.render("bullet speed = " + str(BULLET_VEL[i]), 1, WHITE)
        WIN.blit(draw_text, (100 + 250 * i, 290))

        draw_text = CHOOSE_SPACESHIP_FONT.render("max bullet = " + str(MAX_BULLETS[i]), 1, WHITE)
        WIN.blit(draw_text, (100 + 250 * i, 320))

        draw_text = CHOOSE_SPACESHIP_FONT.render("life = " + str(LIFE[i]), 1, WHITE)
        WIN.blit(draw_text, (100 + 250 * i, 350))
    if turn == 0:
        draw_text = PLAYER_CHOOSE_FONT.render("left player please choose your spaceship", 1, WHITE)
    else:
        draw_text = PLAYER_CHOOSE_FONT.render("right player please choose your spaceship", 1, WHITE)

    WIN.blit(draw_text, (100, 400))


def drew_choose_spaceshipe():
    players = []
    run = True
    choose_time = 0
    while run:
        WIN.blit(SPACE, (0, 0))
        WIN.blit(BLUE_SPACESHIPE, (100, 50))
        WIN.blit(RED_SPACESHIPE, (350,50))
        WIN.blit(YELLOW_SPACESHIPE, (600,50))
        draw_spaceship_data(choose_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x >= 100 and x <= 300 and y >= 50 and y <= 250: #choose the blue spaceship
                    players.append(0)
                    choose_time += 1
                elif x >= 350 and x <= 550 and y >= 50 and y <= 250:
                    players.append(1)
                    choose_time += 1
                elif x >= 600 and x <= 800 and y >= 50 and y <= 250:
                    players.append(2)
                    choose_time += 1
            if choose_time > 1:
                return choose_spaceship(players)

            pygame.display.update()

def choose_spaceship(players):
    choice1 = players[0] #int(input("Choose left spaceship:\n1 for blue(speed=5,shot speed=7,shots=5,life=10)\n2 for red(speed=5,shot speed=9,shots=4,life=8)\n3 for yellow(speed=3,shot speed=7,shots=7,life=9)\n"))-1
    if choice1 == 1:
        png = 'spaceship_red.png'
    elif choice1 == 2:
        png = 'spaceship_yellow.png'
    else:
        png = 'spaceship_navy2.png'

    LEFT_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', png))
    LEFT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(LEFT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

    choice2 = players[1] #int(input("Choose right spaceship:\n1 for blue(speed=5,shot speed=7,shots=5,life=10)\n2 for red(speed=5,shot speed=9,shots=4,life=8)\n3 for yellow(speed=3,shot speed=7,shots=7,life=9)\n")) - 1
    if choice2 == 1:
        png = 'spaceship_red.png'
    elif choice2 == 2:
        png = 'spaceship_yellow.png'
    else:
        png = 'spaceship_navy2.png'

    RIGHT_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', png))
    RIGHT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RIGHT_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
    return LEFT_SPACESHIP,RIGHT_SPACESHIP,choice1,choice2


LEFT_SPACESHIP,RIGHT_SPACESHIP,l_spaceship,r_spaceship = drew_choose_spaceshipe()


EXSPLOSION_IMAGE = pygame.image.load(os.path.join('Assets', 'pngwing.com.png'))
EXSPLOSION = pygame.transform.scale(EXSPLOSION_IMAGE, (EXSPLOSION_WIDTH, EXSPLOSION_HEIGHT))

def draw_window(right, left, right_bullets, left_bullets, right_health, left_health,start):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    right_health_text = HEALTH_FONT.render(
        "Health: " + str(right_health), 1, WHITE)
    left_health_text = HEALTH_FONT.render(
        "Health: " + str(left_health), 1, WHITE)
    WIN.blit(right_health_text, (WIDTH - right_health_text.get_width() - 10, 10))
    WIN.blit(left_health_text, (10, 10))

    WIN.blit(RIGHT_SPACESHIP, (right.x, right.y))
    WIN.blit(LEFT_SPACESHIP, (left.x, left.y))

    if start == True:
        for i in range(3,0,-1):
            draw_text = START_TIMER_FONT.render(str(i), 1, WHITE)
            WIN.blit(draw_text, ((WIDTH - draw_text.get_width()) // 2, (HEIGHT - draw_text.get_height()) // 2))
            pygame.display.update()
            pygame.time.delay(1000)
            draw_the_begin(right_health, left_health,right,left)
        draw_text = START_TIMER_FONT.render("FIGHT", 1, WHITE)
        WIN.blit(draw_text, ((WIDTH - draw_text.get_width()) // 2, (HEIGHT - draw_text.get_height()) // 2))
        pygame.display.update()
        pygame.time.delay(1000)
        start = False

    for bullet in right_bullets:
        pygame.draw.rect(WIN, COLOR[r_spaceship], bullet)

    for bullet in left_bullets:
        pygame.draw.rect(WIN, COLOR[l_spaceship], bullet)

    pygame.display.update()
    return start


def draw_the_begin(right_health, left_health,right,left):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    right_health_text = HEALTH_FONT.render(
        "Health: " + str(right_health), 1, WHITE)
    left_health_text = HEALTH_FONT.render(
        "Health: " + str(left_health), 1, WHITE)
    WIN.blit(right_health_text, (WIDTH - right_health_text.get_width() - 10, 10))
    WIN.blit(left_health_text, (10, 10))

    WIN.blit(RIGHT_SPACESHIP, (right.x, right.y))
    WIN.blit(LEFT_SPACESHIP, (left.x, left.y))


def left_handle_movement(keys_pressed, left):
    if keys_pressed[pygame.K_a] and left.x - VEL[l_spaceship] > 0:  # LEFT
        left.x -= VEL[l_spaceship]
    if keys_pressed[pygame.K_d] and left.x + VEL[l_spaceship] + left.width < BORDER.x:  # RIGHT
        left.x += VEL[l_spaceship]
    if keys_pressed[pygame.K_w] and left.y - VEL[l_spaceship] > 0:  # UP
        left.y -= VEL[l_spaceship]
    if keys_pressed[pygame.K_s] and left.y + VEL[l_spaceship] + left.height < HEIGHT - 15:  # DOWN
        left.y += VEL[l_spaceship]


def right_handle_movement(keys_pressed, right):
    if keys_pressed[pygame.K_LEFT] and right.x - VEL[r_spaceship] > BORDER.x + BORDER.width:  # LEFT
        right.x -= VEL[r_spaceship]
    if keys_pressed[pygame.K_RIGHT] and right.x + VEL[r_spaceship] + right.width < WIDTH:  # RIGHT
        right.x += VEL[r_spaceship]
    if keys_pressed[pygame.K_UP] and right.y - VEL[r_spaceship] > 0:  # UP
        right.y -= VEL[r_spaceship]
    if keys_pressed[pygame.K_DOWN] and right.y + VEL[r_spaceship] + right.height < HEIGHT - 15:  # DOWN
        right.y += VEL[r_spaceship]


def handle_bullets(left_bullets, right_bullets, left, right):
    i = 0
    for bullet in left_bullets:
        bullet.x += BULLET_VEL[l_spaceship]
        if right.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RIGHT_HIT))
            left_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            left_bullets.remove(bullet)
        for obullet in right_bullets:
            if obullet.colliderect(bullet):
                #pygame.event.post(pygame.event.Event(BULLET_HIT))
                right_bullets.remove(obullet)
                left_bullets.remove(bullet)
                i=20
                while i > 0:
                    WIN.blit(EXSPLOSION, (obullet[0] - EXSPLOSION_WIDTH // 2, obullet[1] - EXSPLOSION_HEIGHT // 2))
                    pygame.display.update()
                    i -= 1



    for bullet in right_bullets:
        bullet.x -= BULLET_VEL[r_spaceship]
        if left.colliderect(bullet):
            pygame.event.post(pygame.event.Event(LEFT_HIT))
            right_bullets.remove(bullet)
        elif bullet.x < 0:
            right_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():

    right = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    left = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    right_bullets = []
    left_bullets = []

    right_health = LIFE[r_spaceship]
    left_health = LIFE[l_spaceship]

    clock = pygame.time.Clock()
    start = True

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN and start == False:
                if event.key == pygame.K_q and len(left_bullets) < MAX_BULLETS[l_spaceship]:
                    bullet = pygame.Rect(
                        left.x + left.width, left.y + left.height//2+3, 10, 5)
                    left_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_SPACE and len(right_bullets) < MAX_BULLETS[r_spaceship]:
                    bullet = pygame.Rect(
                        right.x, right.y + right.height//2+3, 10, 5)
                    right_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()

            if event.type == RIGHT_HIT:
                right_health -= 1
                #BULLET_HIT_SOUND.play()

            if event.type == LEFT_HIT:
                left_health -= 1
                #BULLET_HIT_SOUND.play()

        winner_text = ""
        if right_health <= 0:
            winner_text = "Left player Wins!"

        if left_health <= 0:
            winner_text = "Right player Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break


        keys_pressed = pygame.key.get_pressed()
        left_handle_movement(keys_pressed, left)
        right_handle_movement(keys_pressed, right)

        handle_bullets(left_bullets, right_bullets, left, right)

        start = draw_window(right, left, right_bullets, left_bullets,
                            right_health, left_health, start)



    main()


if __name__ == "__main__":
    main()
