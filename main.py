from random import randrange

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.speed_x = 0
        self.speed_y = 0
        x = start_cords[0]
        y = start_cords[1]
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.isJump = False
        # pygame.draw.rect(screen, white, (20, 20, 50, 50))

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        speed = 10
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_a]:
            self.speed_x = -speed
            # camera.move()
        if self.keys[pygame.K_d]:
            self.speed_x = speed
            # camera.move()

        # self.rect.x += speed_x
        # self.rect.y += speed_y

    def get_pos(self):
        return str(self.rect.x) + " " + str(self.rect.y)


class Camera():
    def __init__(self):
        self.rect = pygame.Rect(0, 0, size[0], size[1])

    def move(self):
        self.rect.x += player.speed_x
        self.rect.y += player.speed_y

        print(camera.rect)


class BackgroundObject(pygame.sprite.Sprite):
    def __init__(self, sprite, scale, start_pos):
        x = start_pos[0]
        y = start_pos[1]
        self.speed = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        # pygame.draw.rect(screen, white, (20, 20, 50, 50))

    def update(self):
        self.rect.x += -player.speed_x
        self.rect.y += -player.speed_y


class Tree(BackgroundObject):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        super().__init__("tree.png", (150, 150), position)


class Cloud(BackgroundObject):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        super().__init__("cloud.png", (200, 150), position)
        self.speed = 1

    def update(self):
        self.rect.x += -self.speed
        self.rect.x += -player.speed_x
        self.rect.y += -player.speed_y


if __name__ == "__main__":
    pygame.init()
    size = (1000, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Игра")
    screen.fill((0, 0, 0))

    start_cords = (250, 440)
    cubs_cords = ((150, 150), (350, 150), (350, 150), (350, 350))
    render_distance = 500
    render_radius = 250

    camera = Camera()
    objects = pygame.sprite.Group()
    for x in range(-2000, 2000, 400):
        tree = Tree((x, 440))
        objects.add(tree)
    for i in range(30):
        cloud = Cloud((randrange(-2000, 2000, 100), randrange(50, 150, 10)))
        objects.add(cloud)
    player = Player()
    players = pygame.sprite.Group()
    background = pygame.sprite.Group()

    players.add(player)

    fps = pygame.time.Clock()
    run = True
    while run:
        fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((154, 227, 245))
        background = pygame.sprite.Group()
        objects.update()
        for obj in objects:
            # print(obj.rect)
            if obj.rect.colliderect(camera.rect):
                background.add(obj)
        # print("-" * 20)
        background.update()
        background.draw(screen)
        players.update()
        players.draw(screen)
        pygame.display.flip()

    pygame.quit()
