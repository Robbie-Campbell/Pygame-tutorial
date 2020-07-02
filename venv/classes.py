import pygame

bg = pygame.image.load('Sprites/Game/bg.jpg')

class Player(object):

    walk_right = [pygame.image.load('Sprites/Game/R1.png'), pygame.image.load('Sprites/Game/R2.png'),
                  pygame.image.load('Sprites/Game/R3.png'), pygame.image.load('Sprites/Game/R4.png'),
                  pygame.image.load('Sprites/Game/R5.png'), pygame.image.load('Sprites/Game/R6.png'),
                  pygame.image.load('Sprites/Game/R7.png'), pygame.image.load('Sprites/Game/R8.png'),
                  pygame.image.load('Sprites/Game/R9.png')]

    walk_left = [pygame.image.load('Sprites/Game/L1.png'), pygame.image.load('Sprites/Game/L2.png'),
                 pygame.image.load('Sprites/Game/L3.png'), pygame.image.load('Sprites/Game/L4.png'),
                 pygame.image.load('Sprites/Game/L5.png'), pygame.image.load('Sprites/Game/L6.png'),
                 pygame.image.load('Sprites/Game/L7.png'), pygame.image.load('Sprites/Game/L8.png'),
                 pygame.image.load('Sprites/Game/L9.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_jump = False
        self.jump_count = 10
        self.left = False
        self.right = False
        self.walk_count = 0
        self.standing = True

    def draw(self, win):
        win.blit(bg, (0, 0))
        if not self.standing:
            if self.walk_count + 1 >= 27:
                self.walk_count = 0
            if self.left:
                win.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
            elif self.right:
                win.blit(self.walk_right[self.walk_count // 3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.right:
                win.blit(self.walk_right[0], (self.x, self.y))
            else:
                win.blit(self.walk_left[0], (self.x, self.y))


class Enemy(object):
    walk_right = [pygame.image.load('Sprites/Game/R1E.png'), pygame.image.load('Sprites/Game/R2E.png'),
                  pygame.image.load('Sprites/Game/R3E.png'), pygame.image.load('Sprites/Game/R4E.png'),
                  pygame.image.load('Sprites/Game/R5E.png'), pygame.image.load('Sprites/Game/R6E.png'),
                  pygame.image.load('Sprites/Game/R7E.png'), pygame.image.load('Sprites/Game/R8E.png'),
                  pygame.image.load('Sprites/Game/R9E.png'), pygame.image.load('Sprites/Game/R10E.png'),
                  pygame.image.load('Sprites/Game/R11E.png')]

    walk_left = [pygame.image.load('Sprites/Game/L1E.png'), pygame.image.load('Sprites/Game/L2E.png'),
                 pygame.image.load('Sprites/Game/L3E.png'), pygame.image.load('Sprites/Game/L4E.png'),
                 pygame.image.load('Sprites/Game/L5E.png'), pygame.image.load('Sprites/Game/L6E.png'),
                 pygame.image.load('Sprites/Game/L7E.png'), pygame.image.load('Sprites/Game/L8E.png'),
                 pygame.image.load('Sprites/Game/L9E.png'), pygame.image.load('Sprites/Game/L10E.png'),
                 pygame.image.load('Sprites/Game/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        if self.walk_count + 1 >= 33:
            self.walk_count = 0

        if self.vel > 0:
            win.blit(self.walk_right[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        else:
            win.blit(self.walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walk_count = 0


class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
