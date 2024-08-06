
import pygame

screen = pygame.display.set_mode((500, 500))
x=22
dx = 1000
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        pass
    if x >=450 or x <=0:
        dx *= -1
    pygame.draw.rect(screen, (255,0,0), (x,240,200,200))
    x+=dx
    pygame.display.update()
    pygame.time.delay(0)