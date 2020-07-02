import pygame
from classes import Player, Enemy, Projectile

pygame.init()
window = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Game")
bg = pygame.image.load('Sprites/Game/bg.jpg')


def redraw_game_window():
    window.blit(bg, (0, 0))
    Rab.draw(window)
    goblin.draw(window)
    for shell in bullets:
        shell.draw(window)

    pygame.display.update()


clock = pygame.time.Clock()


Rab = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
bullets = []

running = True
while running:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if Rab.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(Rab.x + Rab.width // 2),
                                      round(Rab.y + Rab.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and Rab.x > Rab.vel:
        Rab.x -= Rab.vel
        Rab.left = True
        Rab.right = False
        Rab.standing = False

    elif keys[pygame.K_RIGHT] and Rab.x < 500 - Rab.width - Rab.vel:
        Rab.x += Rab.vel
        Rab.right = True
        Rab.left = False
        Rab.standing = False

    else:
        Rab.standing = True
        Rab.walk_count = 0

    if not Rab.is_jump:
        if keys[pygame.K_UP]:
            Rab.is_jump = True
            Rab.right = False
            Rab.left = False
            Rab.walk_count = 0
    else:
        if Rab.jump_count >= -10:
            neg = 1
            if Rab.jump_count < 0:
                neg = -1
            Rab.y -= (Rab.jump_count ** 2) * 0.5 * neg
            Rab.jump_count -= 1
        else:
            Rab.is_jump = False
            Rab.jump_count = 10

    redraw_game_window()

pygame.quit()
