import pygame

pygame.init()

width = 700
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()
pygame.quit()