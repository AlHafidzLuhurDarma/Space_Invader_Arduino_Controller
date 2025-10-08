import pygame

pygame.init()

width = 700
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# Player
player = pygame.image.load('rocket.png')
player_x = 350
player_y = 600
player_velocity = .5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Event Player
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player_x -= player_velocity
        print(player_x)
    if key[pygame.K_RIGHT]:
        player_x += player_velocity
        print(player_x)
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

    window.blit(player, (player_x, player_y))
    pygame.display.update()
    window.fill((0,0,0))
pygame.quit()