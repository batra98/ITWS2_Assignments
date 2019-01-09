import pygame
from pygame.locals import *
import spaceship
import bulletclass
import time
import sys
import random
import alienclass
import missile
import sys

pygame.init()
mainClock = pygame.time.Clock()


background = pygame.image.load("final2.jpeg")
bg = pygame.image.load("final.jpeg")
width = 800
height = 765
screen = pygame.display.set_mode((765, height))
pygame.display.set_caption('SPACE INVADERS')


screen.blit(bg, (0, 0))


flag = True
check = True
pyg_font = pygame.font.SysFont('Comics Sans MS', 100)
surfexel = pyg_font.render(
    "Click start to run the game", False, [145, 30, 180])
screen.blit(surfexel, (175, 20))
button = pygame.Rect(310, 650, 180, 70)


while check is True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if button.collidepoint(mouse_pos):
                check = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    screen.blit(bg, (0, 0))
    surfexel = pygame.font.SysFont('Comics Sans MS', 50).render(
        "Click start to run the game", False, [145, 30, 180])
    screen.blit(surfexel, (175, 20))

    pygame.draw.rect(screen, [145, 30, 180], button)
    surfexel2 = pygame.font.SysFont('Comics Sans MS', 50).render(
        "START", False, [255, 255, 255])
    screen.blit(surfexel2, (340, 665))
    pygame.display.update()


def update():
    global numa
    # numa+=1
    flag = 0
    if numa != 16:
        i = alienclass.Aliens(random.choice(posx), random.choice(
            posy), d, pyg_font, pygame.time.get_ticks())
        for j in list(aliens):
            if j.x == i.x and j.y == i.y:
                flag = 1
                break
        if flag == 0:
            numa += 1
            aliens.append(i)

        elif flag == 1:
            update()
    else:
        return


score = 0
sc = pygame.font.SysFont('Comics Sans MS', 60)
surf = sc.render("SCORE:"+" "+str(score), False, [0, 0, 0])


levelspawn = 10000
leveldisapper = 8000


d = 50
updated = True

x_move = 0
ship = spaceship.spaceship(width/2, height-66, pyg_font)
ship.draw(screen, surf, pygame.display.flip)


bullet = []
numb = 0

bullet1 = []
numb1 = 0

posx = []
i = 0
while i < width:
    posx.append(i)
    i = i + width/8


posy = []
posy.append(100)
posy.append(200)

aliens = []
numa = 1

for i in range(numa):
    i = alienclass.Aliens(random.choice(posx), random.choice(
        posy), d, pyg_font, pygame.time.get_ticks())
    aliens.append(i)

start = pygame.time.get_ticks()


while flag:
    finish = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x_move = width/8
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                x_move = -width/8
            if event.key == pygame.K_SPACE:
                numb += 1
                i = bulletclass.Bullet(ship.x+20, height-70, pyg_font)
                bullet.append(i)
            if event.key == pygame.K_s:
                numb1 += 1
                i = missile.missile(ship.x+20, height-70, pyg_font)
                bullet1.append(i)

        if event.type == pygame.KEYUP:
            x_move = 0

    screen.blit(background, (0, 0))
    for i in range(numb):
        bullet[i].move(screen)
        bullet[i].draw(screen)

    for i in range(numb1):
        bullet1[i].move(screen)
        bullet1[i].draw(screen)

    if finish-start >= levelspawn:
        update()
        start = pygame.time.get_ticks()

    for i in list(aliens):
        if i.new is True:
            i.draw(screen)
        elif i.new is False:
            i.draw2(screen)

        for j in list(bullet):
            if j.hit(i.x, i.y, i.d):
                bullet.remove(j)
                numb -= 1
                aliens.remove(i)
                numa -= 1
                score += 1
                if levelspawn > 1000 and leveldisapper > 1000:
                    levelspawn -= 100
                    leveldisapper -= 100

        for j in list(bullet1):
            if j.hit(i.x, i.y, i.d):
                bullet1.remove(j)
                numb1 -= 1
                i.time += 5000
                i.draw2(screen)

                i.new = False

    for i in list(aliens):
        if pygame.time.get_ticks() - i.time >= leveldisapper:
            aliens.remove(i)
            numa -= 1

    ship.x += x_move
    if ship.x < 0:
        ship.x -= x_move
    if ship.x >= width:
        ship.x -= x_move

    surf = sc.render("SCORE:"+" "+str(score), False, [0, 0, 0])

    ship.draw(screen, surf, pygame.display.flip)
    x_move = 0

    mainClock.tick(50)
