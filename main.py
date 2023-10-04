import pygame
import os

pygame.font.init()
#setup
WINDOW = pygame.display.set_mode((600, 600))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MYCOLOR = (48, 213, 200)
BLACK = (0, 0, 0)

#bullet and player movement
BULLET_VEL = 7
MAX_BULLETS = 3
vrVel = 0
hrVel = 0
vyVel = 0
hyVel = 0
eventRun = True

#deals with the health of the user
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

HEALTH_FONT = pygame.font.SysFont('roboto', 20)

# image importing
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('spaceship_yellow.png')), (50, 50)), 0)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('spaceship_red.png')), (50, 50)), 180)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('space.png')), (600, 600))
YELLOW_WIN = pygame.transform.scale(pygame.image.load(os.path.join('yellow_win.png')), (600, 600))
TITLE = pygame.transform.scale(pygame.image.load(os.path.join('title.png')), (600, 600))
RED_WIN = pygame.transform.scale(pygame.image.load(os.path.join('red_win.png')), (600, 600))


def draw_window(red, yellow, yellow_bullets, red_bullets, red_health, yellow_health):
    WINDOW.blit(SPACE, (0, 0))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED, bullet)

    red_health_text = HEALTH_FONT.render('RED HEALTH: ' + str(red_health), 1, RED)
    yellow_health_text = HEALTH_FONT.render('YELLOW HEALTH: ' + str(yellow_health), 1, YELLOW)
    text = HEALTH_FONT.render('PLAY AGAIN?' , True , BLACK)
    
    WINDOW.blit(red_health_text, (10, 10))
    WINDOW.blit(yellow_health_text, (200, 10))
    
    if yellow_health == 0:
        WINDOW.blit(RED_WIN, (0, 0))
        pygame.draw.rect(WINDOW, YELLOW, [WINDOW.get_width() / 2, WINDOW.get_height() / 2, 140, 40])
        WINDOW.blit(text , (WINDOW.get_width()/2 + 50, WINDOW.get_height() / 2))
        pygame.display.update()
        
    if red_health == 0:
        WINDOW.blit(YELLOW_WIN, (0, 0))
        pygame.draw.rect(WINDOW, RED, [WINDOW.get_width() / 2, WINDOW.get_height() / 2, 140, 40])
        WINDOW.blit(text , (WINDOW.get_width()/2 + 50, WINDOW.get_height() / 2))
        pygame.display.update()

def yellow_movement(keys_pressed, yellow):
    global vyVel
    global hyVel
    # a - left, w - up, s - down, d - right
    if yellow.x + hyVel > WINDOW.get_width() :
        yellow.x -= 0.1
        hyVel = 0
        print('stop')
    elif yellow.x + hyVel < 0 :
        yellow.x += 0.1
        hyVel = 0
        print('stop')
    
    if yellow.y + vyVel > WINDOW.get_height() :
        yellow.y -= 0.1
        vyVel = 0
    elif yellow.y + vyVel < 0 :
        yellow.y += 0.1 
        vyVel = 0

    if keys_pressed[pygame.K_a] and yellow.x - hyVel > 0:
        yellow.x += hyVel
        hyVel = hyVel - 0.5
    elif yellow.x - hyVel > 0 and hyVel < 0 :
        hyVel += 0.5
        yellow.x += hyVel

    if keys_pressed[pygame.K_d] and yellow.x + hyVel + 50 < WINDOW.get_width():
        yellow.x += hyVel
        hyVel= hyVel + 0.5
    elif yellow.x + hyVel + 50 < WINDOW.get_width() and hyVel > 0 :
        hyVel -= 0.5 
        yellow.x += hyVel

    if keys_pressed[pygame.K_w] and yellow.y - vyVel > 0:
        yellow.y += vyVel
        vyVel = vyVel - 0.5
    elif yellow.y - vyVel > 0 and vyVel < 0 :
        vyVel += 0.5
        yellow.y += vyVel

    if keys_pressed[pygame.K_s] and yellow.y + vyVel + 50 < WINDOW.get_height():
        yellow.y += vyVel
        vyVel = vyVel + 0.5
    elif yellow.y + vyVel + 50 < WINDOW.get_height() and vyVel > 0 :
        vyVel -= 0.5
        yellow.y += vyVel

def red_movement(keys_pressed, red):
    global vrVel
    global hrVel
    # a - left, w - up, s - down, d - right
    if red.x + hrVel > WINDOW.get_width() :
        red.x -= 0.1
        hrVel = 0
        print('stop')
    elif red.x + hrVel < 0 :
        red.x += 0.1
        hrVel = 0
        print('stop')
    
    if red.y + vrVel > WINDOW.get_height() :
        red.y -= 0.1
        vrVel = 0
    elif red.y + vrVel < 0 :
        red.y += 0.1 
        vrVel = 0

    if keys_pressed[pygame.K_LEFT] and red.x - hrVel > 0:
        red.x += hrVel
        hrVel = hrVel - 0.5
    elif red.x - hyVel > 0 and hrVel < 0 :
        hrVel += 0.5
        red.x += hrVel

    if keys_pressed[pygame.K_RIGHT] and red.x + hrVel + 50 < WINDOW.get_width():
        red.x += hrVel
        hrVel= hrVel + 0.5
    elif red.x + hrVel + 50 < WINDOW.get_width() and hrVel > 0 :
        hrVel -= 0.5 
        red.x += hrVel

    if keys_pressed[pygame.K_UP] and red.y - vrVel > 0:
        red.y += vrVel
        vrVel = vrVel - 0.5
    elif red.y - vrVel > 0 and vrVel < 0 :
        vrVel += 0.5
        red.y += vrVel

    if keys_pressed[pygame.K_DOWN] and red.y + vrVel + 50 < WINDOW.get_height():
        red.y += vrVel
        vrVel = vrVel + 0.5
    elif red.y + vrVel + 50 < WINDOW.get_height() and vrVel > 0 :
        vrVel -= 0.5
        red.y += vrVel
def bullet_movement(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.y += BULLET_VEL
        # checks for collision
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        if bullet.y > WINDOW.get_height():
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.y -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        if bullet.y < 0:
            red_bullets.remove(bullet)

def game():
    global eventRun
    #make spaceship objects
    red = pygame.Rect(100, 435, 50, 50) # makes red spaceship boundaries
    yellow = pygame.Rect(100, 15, 50, 50) # makes yellow spaceship boundaries
    
    
    
    yellow_bullets = []
    red_bullets = []
    
    red_health = 10
    yellow_health = 10
    
    
    clock = pygame.time.Clock()
    first = True
    
    WINDOW.blit(TITLE, (0, 0))
    pygame.display.update()
    pygame.time.wait(1000)
    print('hello')
    running = True

    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and eventRun:
                
                if event.key == pygame.K_f and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + 20, yellow.y + 15, 10, 5)
                    yellow_bullets.append(bullet)
                
                if event.key == pygame.K_SPACE and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x + 20, red.y + 15, 10, 5)
                    red_bullets.append(bullet)

            if event.type == RED_HIT and eventRun:
                red_health -= 1
            
            if event.type == YELLOW_HIT and eventRun:
                yellow_health -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if WINDOW.get_width()/2 <= mouse[0] <= WINDOW.get_width()/2+140 and WINDOW.get_height()/2 <= mouse[1] <= WINDOW.get_height()/2+40 :
                    red_health = 10
                    yellow_health = 10
                    draw_window(red, yellow, yellow_bullets, red_bullets, red_health, yellow_health)
                eventRun = True
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        
        
        bullet_movement(yellow_bullets, red_bullets, yellow, red)
        
        
        # last 2 things in game method
        draw_window(red, yellow, yellow_bullets, red_bullets, red_health, yellow_health)
        pygame.display.update()
        
        if red_health == 0 or yellow_health == 0:
            eventRun = False
        
#the following is like the main method in java
if __name__ == '__main__':
    pygame.init()
    game()
    pygame.quit() 

