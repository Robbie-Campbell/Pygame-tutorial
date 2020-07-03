import pygame
from classes import Player, Enemy, Projectile

pygame.init()
window = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Game")
bg = pygame.image.load('Sprites/Game/bg.jpg')
score = 0

bullet_sound = pygame.mixer.Sound("Sprites/Game/bullet.wav")
hit_sound = pygame.mixer.Sound("Sprites/Game/hit.wav")
game_music = pygame.mixer.music.load("Sprites/Game/music.mp3")

pygame.mixer.music.play(-1)


def redraw_game_window():
    window.blit(bg, (0, 0))
    score_current = font.render("Score: " + str(score), 1, (0, 0, 0))
    window.blit(score_current, (390, 10))
    Rab.draw(window)
    goblin.draw(window)
    for shell in bullets:
        shell.draw(window)

    pygame.display.update()


clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsans', 30, True)
Rab = Player(300, 410, 64, 64)
goblin = Enemy(100, 410, 64, 64, 450)
shoot_loop = 0
bullets = []

running = True
while running:
    clock.tick(27)

    if goblin.visible:
        if Rab.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and Rab.hitbox[1] + Rab.hitbox[3] > goblin.hitbox[1]:
            if Rab.hitbox[0] + Rab.hitbox[2] > goblin.hitbox[0] and Rab.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                Rab.hit(window)
                score -= 5

    if shoot_loop > 0:
        shoot_loop += 1
    if shoot_loop > 3:
        shoot_loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for bullet in bullets:
        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                    goblin.hit()
                    score += 1
                    hit_sound.play()
                    bullets.pop(bullets.index(bullet))

        if 500 > bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot_loop == 0:
        bullet_sound.play()
        if Rab.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(Rab.x + Rab.width // 2),
                                      round(Rab.y + Rab.height // 2), 6, (0, 0, 0), facing))

        shoot_loop = 1

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
