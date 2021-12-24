import pygame

if __name__ == "__main__":
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Игра")
    screen.fill((0, 0, 0))

    start_cords = (250, 450)
    cubs_cords = ((150, 150), (350, 150), (350, 150), (350, 350))
    render_distance = 500
    render_radius = 250

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        visibility = (start_cords, (start_cords[0] - render_radius, start_cords[1] - render_distance),
                      (start_cords[0] + render_radius, start_cords[1] - render_distance))  # ABC
        BA = ((visibility[1][0] - visibility[0][0]) ** 2 + (visibility[1][1] - visibility[0][1]) ** 2) ** 1 / 2
        CA = ((visibility[2][0] - visibility[0][0]) ** 2 + (visibility[2][1] - visibility[0][1]) ** 2) ** 1 / 2
        BC = ((visibility[1][0] - visibility[2][0]) ** 2 + (visibility[2][1] - visibility[1][1]) ** 2) ** 1 / 2
        p = (BA + CA + BC) / 2
        S = (p * (p - BA) * (p - CA) * (p - BC)) ** 1 / 2



    pygame.quit()
