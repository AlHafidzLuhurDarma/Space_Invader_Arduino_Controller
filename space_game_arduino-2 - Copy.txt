
import pygame
import random
import serial
import math

arduinoData = serial.Serial('com3', 9600)

pygame.init()

def is_Collision(enemy_x, enemy_y, player_x, player_y):
    distance = math.sqrt((math.pow(enemy_x-player_x,2)) + (math.pow(enemy_y-player_y, 2)))
    if distance <= 30:
        return True
    else:
        return False

width = 700
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# Background
background = pygame.image.load('background1.png')
pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

# Player
player = pygame.image.load('rocket.png')
player_x = int(width/2)
player_y = int(height-70)
player_velocity = 8

# Enemy-1
enemy = []
enemy_x = []
enemy_y = []
enemy_velocity = []
enemy_army = 5
for i in range(enemy_army):
    enemy.append(pygame.image.load('alien-ship.png'))
    enemy_x.append(random.randint(0,int(width-21)))
    enemy_y.append(int(height/4))
    enemy_velocity.append(8)

# Enemy-2
enemy2 = []
enemy2_x = []
enemy2_y = []
enemy2_velocity = []
enemy2_army = 5
for i in range(enemy2_army):
    enemy2.append(pygame.image.load('space-ship.png'))
    enemy2_x.append(random.randint(0,int(width-21)))
    enemy2_y.append(int(height/3))
    enemy2_velocity.append(8)

# Enemy-3
enemy3 = []
enemy3_x = []
enemy3_y = []
enemy3_velocity = []
enemy3_army = 5
for i in range(enemy3_army):
    enemy3.append(pygame.image.load('alien-ship (1).png'))
    enemy3_x.append(random.randint(0,int(width-21)))
    enemy3_y.append(int(height/2))
    enemy3_velocity.append(8)

# Bullet
bullet = pygame.image.load('bullet (2).png')
bullet_index = False
bullet_velocity = 10
bullet_y = 0
bullet_x = 0
bullet_state = 'ready'

# Scores
scores = 0
score_index = False
font = pygame.font.Font('freesansbold.ttf', 32)
textY = 10
textX = 10

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.blit(background, (0,0))

    # Event Player
    arduinoPacket = arduinoData.readline()
    arduinoPacket = str(arduinoPacket, 'utf-8')
    arduinoPacket = arduinoPacket.strip('\r\n')
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or arduinoPacket == 'Kiri':
        player_x -= player_velocity
    if key[pygame.K_RIGHT] or arduinoPacket == 'Kanan':
        player_x += player_velocity
    if key[pygame.K_UP] or arduinoPacket == 'Up':
        player_y -= player_velocity
    if key[pygame.K_DOWN]:
        player_y += player_velocity
    if bullet_state == 'ready':
        if key[pygame.K_SPACE] or arduinoPacket == 'Shot':
            bullet_index = True
            bullet_x = player_x
            bullet_y = player_y
            bullet_sound = pygame.mixer.Sound('laser.wav')
            bullet_sound.play()
    print(arduinoPacket)

    # Bullet Movements
    if bullet_index == True:
        window.blit(bullet, (bullet_x, bullet_y))
        bullet_y -= bullet_velocity
        bullet_state = 'reload'
    if bullet_y <= 5:
        bullet_index = False
        bullet_state = 'ready'


    # Boundaries
    if player_x >= int(width-20):
        player_x = int(width - 21)
    if player_x <= 0:
        player_x = 1
    if player_y >= int(height-20):
        player_y = int(height - 21)
    if player_y <= 10:
        player_y = 11

    # Enemy Movements
    for i in range(enemy_army):
        enemy_x[i] += enemy_velocity[i]
        window.blit(enemy[i], (enemy_x[i], enemy_y[i]))
        if enemy_x[i] >= int(width-20) or enemy_x[i] <=0 :
            enemy_velocity[i] *= (-1)
    for i in range(enemy_army):
        collision1 = is_Collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision1 == True:
            enemy_x[i] = random.randint(0,int(width-21))
            bullet_y = player_y
            bullet_index = False
            score_index = True
            bullet_state = 'ready'


    # Enemy 2 Movements
    for i in range(enemy2_army):
        enemy2_x[i] += enemy2_velocity[i]
        window.blit(enemy2[i], (enemy2_x[i], enemy2_y[i]))
        if enemy2_x[i] >= int(width-20) or enemy2_x[i] <=0 :
            enemy2_velocity[i] *= (-1)
    for i in range(enemy_army):
        collision2 = is_Collision(enemy2_x[i], enemy2_y[i], bullet_x, bullet_y)
        if collision2 == True:
            enemy2_x[i] = random.randint(0,int(width-21))
            bullet_y = player_y
            collision2 = False
            bullet_index = False
            score_index = True
            bullet_state = 'ready'


    # Enemy 3 Movements
    for i in range(enemy3_army):
        enemy3_x[i] += enemy3_velocity[i]
        window.blit(enemy3[i], (enemy3_x[i], enemy3_y[i]))
        if enemy3_x[i] >= int(width-20) or enemy3_x[i] <=0 :
            enemy3_velocity[i] *= (-1)
        collision3 = is_Collision(enemy3_x[i], enemy3_y[i], bullet_x, bullet_y)
        if collision3 == True:
            collision3 = False
            bullet_y = player_y
            enemy3_x[i] = random.randint(0,int(width-21))
            bullet_index = False
            score_index = True
            bullet_state = 'ready'
    # Scores
    if score_index == True:
        explotion_sound = pygame.mixer.Sound('explosion.wav')
        explotion_sound.play()
        scores += 1
        score_index = False
        collision1 = False
    score = font.render('Score: ' + str(scores), True, (255,255,255))
    window.blit(score, (textX, textY))
    window.blit(player, (player_x, player_y))
    pygame.display.update()
    window.fill((0,0,0))
pygame.quit()