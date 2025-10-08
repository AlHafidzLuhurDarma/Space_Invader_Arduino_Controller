import pygame

pygame.init()

width = 700
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# Background
background = pygame.image.load('background.png')

# Player
player = pygame.image.load('rocket.png')
player_x = int(width/2)
player_y = int(height-70)
player_velocity = .5

# Enemy-1
enemy = pygame.image.load('alien-ship.png')
enemy_x = 0
enemy_y = int(height/4)
enemy_velocity = .5

# Enemy-2
enemy2 = pygame.image.load('space-ship.png')
enemy2_x = 10
enemy2_y = int(height/3)
enemy2_velocity = .5

# Enemy-3
enemy3 = pygame.image.load('alien-ship (1).png')
enemy3_x = 20
enemy3_y = int(height/2)
enemy3_velocity = .5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #window.blit(background, (0,200))
    # Event Player
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player_x -= player_velocity
    if key[pygame.K_RIGHT]:
        player_x += player_velocity
    if key[pygame.K_UP]:
        player_y -= player_velocity
    if key[pygame.K_DOWN]:
        player_y += player_velocity

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
    enemy_x += enemy_velocity
    if enemy_x >= int(width-20) or enemy_x <=0 :
        enemy_velocity *= (-1)

    # Enemy 2 Movements
    enemy2_x += enemy2_velocity
    if enemy2_x >= int(width-20) or enemy2_x <=0 :
        enemy2_velocity *= (-1)

    # Enemy 3 Movements
    enemy3_x += enemy3_velocity
    if enemy3_x >= int(width-20) or enemy3_x <=0 :
        enemy3_velocity *= (-1)

    window.blit(enemy, (enemy_x, enemy_y))
    window.blit(enemy2, (enemy2_x, enemy2_y))
    window.blit(enemy3, (enemy3_x, enemy3_y))
    window.blit(player, (player_x, player_y))
    pygame.display.update()
    window.fill((0,0,0))
pygame.quit()