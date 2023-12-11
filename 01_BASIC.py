import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
is_blue = True
x = 60
y = 60

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.K_DOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y=y-3
    if pressed[pygame.K_DOWN]:
        y = y+3
    if pressed[pygame.K_LEFT]:
        x = x-3
    if pressed[pygame.K_RIGHT]:
        x = x+3

    if is_blue:
        color= (0,128,255)
    else:
        color= (255,100,0)

    pygame.draw.rect(screen,color,pygame.Rect(x,y,30,30))
    pygame.display.flip()

pygame.quit()