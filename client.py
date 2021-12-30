import socket

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        x = 100
        y = 440
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.isJump = False
        # pygame.draw.rect(screen, white, (20, 20, 50, 50))
        self.message = str(self.rect.x) + str(self.rect.y)

    def update(self):
        speed_x = 0
        speed_y = 0
        speed = 10
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_a]:
            speed_x = -speed
        if self.keys[pygame.K_d]:
            speed_x = speed
        if self.keys[pygame.K_SPACE]:
            self.isJump = True

        self.rect.x += speed_x
        self.rect.y += speed_y
        self.message = str(self.rect.x) + " " + str(self.rect.y)

    def get_pos(self):
        self.message = str(self.rect.x) + " " + str(self.rect.y)


# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
# client_socket.connect(("localhost", 10000))

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Игра")
screen.fill((0, 0, 0))

start_cords = (250, 450)
cubs_cords = ((150, 150), (350, 150), (350, 150), (350, 350))
render_distance = 500
render_radius = 250

player = Player()
players = pygame.sprite.Group()
players.add(player)

run = True
while run:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            pass

    # считываем мышку, клавиатуру и прочие команды
    # if pygame.mouse.get_focused():
    #     print(pygame.mouse.get_pos())

    # отправляем команду
    message = "<" + player.message + ">"
    # client_socket.send(message.encode())

    # data = client_socket.recv(1024)
    # data = data.decode()

    # рисуем новое состояние игры
    screen.fill((0, 0, 0))
    players.update()
    players.draw(screen)
    pygame.display.flip()
    # print(data)
pygame.quit()
