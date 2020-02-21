#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import config
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((config.sw, config.sh))
p1s = 0
p1e = 0
p2s = 0
p2e = 0
p1score = 0
p2score = 0
p1time = 0
p2time = 0
k = 0
w1 = 0
w2 = 0


def disp(text, colour, pos):
    font = pygame.font.Font(config.retro, 15)
    display = font.render(text, False, colour)
    screen.blit(display, pos)


def intro():
    display_crash_text = 500
    while display_crash_text:
        screen.fill(config.BLACK)
        font = pygame.font.Font(config.retro, 80)
        display = font.render('C Y K ', False, config.GREEN)
        screen.blit(display, (config.sw / 2 - 100, config.sh / 2 - 100))
        disp('presents you', config.RED, (config.sw / 2 - 70, config.sh
                                          / 2))
        font = pygame.font.Font(config.retro, 30)
        display = font.render('THIS AINT MY LAST RIDE', False,
                              config.BLUE)
        screen.blit(display, (config.sw / 2 - 100, config.sh / 2 + 40))
        display_crash_text -= 1
        pygame.display.flip()


def crash(x):
    display_crash_text = 500
    while display_crash_text:
        screen.fill(config.BLACK)
        disp(x, config.RED, (config.sw / 2 - 150, config.sh / 2))
        display_crash_text -= 1
        pygame.display.flip()


pygame.display.set_caption('this aint my last ride')
running = True
player = pygame.image.load('boat.png').convert_alpha()
player2 = pygame.image.load('boat2.png').convert_alpha()
player = pygame.transform.scale(player, (80, 40))
player2 = pygame.transform.scale(player2, (80, 40))

obstacle = []
obstacle_mask = []
obstacle_rect = []
offseto_x = []
offseto_y = []
offseto2_x = []
offseto2_y = []
intro()

# crash("Loading game . . .")

for i in range(90):
    obstacle.append(pygame.image.load('iceberg.png').convert_alpha())
    obstacle[i] = pygame.transform.scale(obstacle[i], (100, 100))
    obstacle_mask.append(pygame.mask.from_surface(obstacle[i], 50))
    obstacle_rect.append(obstacle[i].get_rect())
    offseto_x.append(0)
    offseto_y.append(0)
    offseto2_x.append(0)
    offseto2_y.append(0)
    obstacle_rect[i].y = random.randint(30, 650)
    obstacle_rect[i].x = random.randint(50, 1600)

enemy = []
enemy_mask = []
enemy_rect = []
offset_x = []
offset_y = []
offset2_x = []
offset2_y = []

for i in range(10):
    if i < 6:
        enemy.append(pygame.image.load('pirate.png').convert_alpha())
        enemy[i] = pygame.transform.scale(enemy[i], (150, 75))
    else:
        enemy.append(pygame.image.load('bgbattleship.png'
                                       ).convert_alpha())
        enemy[i] = pygame.transform.scale(enemy[i], (200, 200))
    enemy_mask.append(pygame.mask.from_surface(enemy[i], 50))
    enemy_rect.append(enemy[i].get_rect())
    offset_x.append(0)
    offset_y.append(0)
    offset2_x.append(0)
    offset2_y.append(0)
    enemy_rect[i].y = i * 127 + 46
    enemy_rect[i].x = random.randint(0, 1600)
enemy_rect[6].y = 2 * 127 + 15
enemy_rect[6].x = 1568
enemy_rect[7].y = 3 * 127 + 10
enemy_rect[7].x = random.randint(0, 1600)
enemy_rect[8].y = 4 * 127 + 10
enemy_rect[8].x = random.randint(0, 1600)
enemy_rect[9].y = 1 * 127 + 10
enemy_rect[9].x = random.randint(0, 1600)
playerXr = 0
playerXl = 0
playerYu = 0
playerYd = 0
speed = config.playerspeed

player_mask = pygame.mask.from_surface(player, 50)
player2_mask = pygame.mask.from_surface(player2, 50)
player_rect = player.get_rect()
player2_rect = player2.get_rect()

afont = pygame.font.Font(None, 16)
hitsurf = afont.render('Hit!!!  Oh noes!!', 1, (255, 255, 255))
(last_px, last_py) = (0, 0)
player_rect.x = config.sw / 2
player_rect.y = 760
player2_rect.x = config.sw / 2
player2_rect.y = 0
crash('Round 1')
while running:
    screen.fill(config.AQUA)
    for i in range(7):
        pygame.draw.rect(screen, config.BLUE, [0, i * 127, config.sw,
                                               40])
    if not k % 2:
        p1time += 1
        player_rect.x = player_rect.x + playerXr - playerXl
        player_rect.y = player_rect.y + playerYd - playerYu
        if player_rect.x <= 0:
            player_rect.x = 0
        if player_rect.x >= config.sw - 80:
            player_rect.x = config.sw - 80
        if player_rect.y <= 0:
            player_rect.y = 0
            pygame.time.wait(500)
            crash('P1' + config.suc + str(k // 2 + 1))
            w1 += 1
            p1score += p1e + p1s
            screen.fill(config.BLACK)
            player_rect.x = config.sw / 2
            player_rect.y = 760
            k += 1
            playerXl = 0
            playerXr = 0
            playerYu = 0
            playerYd = 0

        if player_rect.y >= config.sh - 40:
            player_rect.y = config.sh - 40
    else:
        p2time += 1
        player2_rect.x = player2_rect.x + playerXr - playerXl
        player2_rect.y = player2_rect.y + playerYd - playerYu
        if player2_rect.x <= 0:
            player2_rect.x = 0
        if player2_rect.x >= config.sw - 80:
            player2_rect.x = config.sw - 80
        if player2_rect.y <= 0:
            player2_rect.y = 0
        if player2_rect.y >= config.sh - 40:
            player2_rect.y = config.sh - 40
            pygame.time.wait(500)
            crash('P2' + config.suc + str(k // 2 + 1))
            p2score += p2e + p2s
            player2_rect.x = config.sw / 2
            player2_rect.y = 0
            k += 1
            w2 += 1
            if k == 8:
                running = 0
                break
            crash('Round ' + str(k // 2 + 1))
            playerXl = 0
            playerXr = 0
            playerYu = 0
            playerYd = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN \
                and event.key == pygame.K_ESCAPE:
            running = False

        if event.type == pygame.KEYDOWN:
            if not k % 2:
                if event.key == pygame.K_LEFT:
                    playerXl = speed
                if event.key == pygame.K_RIGHT:
                    playerXr = speed
                if event.key == pygame.K_UP:
                    playerYu = speed
                if event.key == pygame.K_DOWN:
                    playerYd = speed
            else:
                if event.key == pygame.K_a:
                    playerXl = speed
                if event.key == pygame.K_d:
                    playerXr = speed
                if event.key == pygame.K_w:
                    playerYu = speed
                if event.key == pygame.K_s:
                    playerYd = speed
        if event.type == pygame.KEYUP:
            if k % 2:
                if event.key == pygame.K_a:
                    playerXl = 0
                if event.key == pygame.K_d:
                    playerXr = 0
                if event.key == pygame.K_w:
                    playerYu = 0
                if event.key == pygame.K_s:
                    playerYd = 0
            else:
                if event.key == pygame.K_LEFT:
                    playerXl = 0
                if event.key == pygame.K_RIGHT:
                    playerXr = 0
                if event.key == pygame.K_UP:
                    playerYu = 0
                if event.key == pygame.K_DOWN:
                    playerYd = 0
    (px, py) = (player_rect[0], player_rect[1])
    (p2x, p2y) = (player2_rect[0], player2_rect[1])
    disp('P1 Score: ' + str(p1score + p1s + p1e), config.GREEN, (0, 0))
    disp('P1 Time: ' + str(p1time // 40), config.GREEN, (0, 20))
    disp('P2 Score: ' + str(p2score + p2s + p2e), config.RED, (1400, 0))
    disp('P2 Time: ' + str(p2time // 40), config.RED, (1400, 20))
    if k % 2:
        disp('Start', config.RED, (config.sw / 2 - 100, 0))
        disp('End', config.RED, (config.sw / 2 - 100, 760))
    else:
        disp('Start', config.GREEN, (config.sw / 2 - 100, 760))
        disp('End', config.GREEN, (config.sw / 2 - 100, 0))
    p1e = 0
    p2e = 0
    for i in range(6 + k // 2 + 1):
        offset_x[i] = px - enemy_rect[i][0]
        offset_y[i] = py - enemy_rect[i][1]
        offset2_x[i] = p2x - enemy_rect[i][0]
        offset2_y[i] = p2y - enemy_rect[i][1]
        a = enemy_mask[i].overlap(player_mask, (offset_x[i],
                                                offset_y[i]))
        b = enemy_mask[i].overlap(player2_mask, (offset2_x[i],
                                                 offset2_y[i]))
        overlap = a or b
        if offset_y[i] < 0:
            p1e += 10
        if offset2_y[i] > 0:
            p2e += 10
        if overlap:
            pygame.time.wait(200)
            if not k % 2:
                crash('P1' + config.cra)
                p1score += p1e + p1s
                player_rect.x = config.sw / 2
                player_rect.y = 760
            else:
                crash('P2' + config.cra)
                p2score += p2e + p2s
                player2_rect.x = config.sw / 2
                player2_rect.y = 0
                if k + 1 == 8:
                    running = 0
                    break
                crash('Round ' + str(k // 2 + 2))
            k += 1
            playerXl = 0
            playerXr = 0
            playerYu = 0
            playerYd = 0
            overlap = 0
            break
    p1s = 0
    p2s = 0
    for i in range(10 + k // 2 * 20):
        offseto_x[i] = px - obstacle_rect[i][0]
        offseto_y[i] = py - obstacle_rect[i][1]
        offseto2_x[i] = p2x - obstacle_rect[i][0]
        offseto2_y[i] = p2y - obstacle_rect[i][1]
        if offseto_y[i] < 0:
            p1s += 5
        if offseto2_y[i] > 0:
            p2s += 5
        c = obstacle_mask[i].overlap(player_mask, (offseto_x[i],
                                                   offseto_y[i]))
        d = obstacle_mask[i].overlap(player2_mask, (offseto2_x[i],
                                                    offseto2_y[i]))
        overlap = c or d
        if overlap:
            screen.blit(hitsurf, (0, 0))
            pygame.time.wait(500)
            if not k % 2:
                crash('P1' + config.cra)
                p1score += p1e + p1s
                player_rect.x = config.sw / 2
                player_rect.y = 760
                pygame.time.wait(300)
            else:
                crash('P2' + config.cra)
                p2score += p2e + p2s
                player2_rect.x = config.sw / 2
                player2_rect.y = 0
                if k + 1 == 8:
                    running = 0
                    break
                crash('Round ' + str(k // 2 + 2))
                pygame.time.wait(300)
            k += 1
            playerXl = 0
            playerXr = 0
            playerYu = 0
            playerYd = 0
            break
    if k == 8:
        break
    for i in range(6 + k // 2 + 1):
        if not (k % 2):
            if i < 3:
                enemy_rect[i].x = (enemy_rect[i].x + (i + 1) * 3 + w1
                                   * 5 + 2) % 1600
            elif i < 6:
                enemy_rect[i].x = (enemy_rect[i].x + (6 - i) * 3 + w1
                                   * 5 + 2) % 1600
            else:
                enemy_rect[i].x = (enemy_rect[i].x + w1 * (10 - i) * 3) \
                                  % 1600
        else:
            if i < 3:
                enemy_rect[i].x = (enemy_rect[i].x + (i + 1) * 3 + w2
                                   * 5 + 2) % 1600
            elif i < 6:
                enemy_rect[i].x = (enemy_rect[i].x + (6 - i) * 3 + w2
                                   * 5 + 2) % 1600
            else:
                enemy_rect[i].x = (enemy_rect[i].x + w2 * (10 - i) * 2) \
                                  % 1600
        screen.blit(enemy[i], (enemy_rect[i][0], enemy_rect[i][1]))
    for i in range(10 + k // 2 * 20):
        screen.blit(obstacle[i], (obstacle_rect[i][0],
                                  obstacle_rect[i][1]))
    screen.blit(player, (player_rect[0], player_rect[1]))
    screen.blit(player2, (player2_rect[0], player2_rect[1]))
    pygame.display.flip()
    clock.tick(40)
if p1score > p2score:
    crash('GAME OVER  ,P1 , You win')
elif p2score > p1score:
    crash('GAME OVER  ,P2 , You win')
else:
    if p1time < p2time:
        crash('GAME OVER  ,P1 , You win')
    elif p2time < p1time:
        crash('GAME OVER,  P2 , You win')
    else:
        crash('GAME OVER,  You both win')
pygame.quit()
