import pygame
import random

class Rect:
    def __init__(self,width,height):
        self.x = random.randint(1, 449)
        self.y = 50
        self.dx = random.randint(5, 10)
        self.width = width
        self.height = height
        self.s = True
    
    def die(self):
        self.x = -100
        self.y = -100
        self.s = False

def kill_roket():
    global rx, ry ,rs
    rs = False
    rx = -100
    ry = -100
screen = pygame.display.set_mode((500, 500))
x = 250
y = 450
rs = False
rx = -100
ry = -100
# random.randint(a, b) случайное целое число в диогонале от a до b 
num_rects = random.randint(3, 6)
                  #0 + 1 500 - ширина квадрата - 1
rects = [Rect(50, 50) for i in range(num_rects)]


while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        pass
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_d] and x < 450:
        x += 5        
    if keys[pygame.K_a] and x > 0:
        x -= 5
    if keys[pygame.K_SPACE] and rs ==False:
        rx = x
        ry = y
        rs = True
        
    if ry <= 0:
       kill_roket()
       
        
    if rs:
        pygame.draw.rect(screen,(255,255,0),(rx,ry,25,25))
        ry -= 5
    for i in range(len(rects)):
        if rects[i].x >= 450 or rects[i].x <= 0:
            rects[i].dx = -rects[i].dx
        if (rx >= rects[i].x and rx <= rects[i].x + rects[i].width or \
            rx + 25 <= rects[i].x + rects[i].width and rx + 25 >= rects[i].x) and \
            ry <= rects[i].y + rects[i].height:
            kill_roket()
            rects[i].die() 
        if rects[i].s:
            rects[i].x += rects[i].dx
            pygame.draw.rect(screen, (0, 255, 0), (rects[i].x, rects[i].y,
                                               rects[i].width, rects[i].height))
        
    
    pygame.draw.rect(screen, (225, 0, 0), (x, y, 50, 50))   
    pygame.display.update()
    pygame.time.delay(12)
        