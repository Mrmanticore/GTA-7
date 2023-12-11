import pygame
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooting Game")

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

character_size = 50
character_speed = 5
character = pygame.Rect(width // 2 - character_size // 2, height - character_size, character_size, character_size)

bullet_size = 10
bullets = []

enemy_radius = 20
enemies = []

score = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(character.centerx - bullet_size // 2, character.top, bullet_size, bullet_size)
                bullets.append(bullet)
                
    for bullet in bullets:
        bullet.y -= 10
        if bullet.top < 0:
            bullets.remove(bullet)

    if random.randint(1, 100) <= 2:
        enemy_x = random.randint(enemy_radius, width - enemy_radius)
        enemy = pygame.Rect(enemy_x - enemy_radius, 0, enemy_radius * 2, enemy_radius * 2)
        enemies.append(enemy)

    for enemy in enemies:
        enemy.y += 5
        if enemy.top > height:
            enemies.remove(enemy)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character.x -= character_speed
    if keys[pygame.K_RIGHT]:
        character.x += character_speed

    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                score += 1
                bullets.remove(bullet)
                enemies.remove(enemy)

    for enemy in enemies:
        if character.colliderect(enemy):
            running = False

    screen.fill(white)

    for bullet in bullets:
        pygame.draw.polygon(screen, blue, [(bullet.left, bullet.bottom), (bullet.centerx, bullet.top), (bullet.right, bullet.bottom)])

    pygame.draw.rect(screen, red, character)

    for enemy in enemies:
        pygame.draw.circle(screen, red, enemy.center, enemy_radius)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, red)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

font = pygame.font.Font(None, 72)
game_over_text = font.render("Game Over", True, red)
screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
pygame.display.flip()

pygame.time.wait(3000)

pygame.quit()