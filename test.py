start_cords = (250, 450)
cubs_cords = ((150, 150), (350, 150), (350, 150), (350, 350))
render_distance = 500
render_radius = 250
visibility = (start_cords, (start_cords[0] - render_radius, start_cords[1] - render_distance),
              (start_cords[0] + render_radius, start_cords[1] - render_distance))  # ABC
BA = ((visibility[1][0] - visibility[0][0]) ** 2 + (visibility[1][1] - visibility[0][1]) ** 2) ** 1 / 2
CA = ((visibility[2][0] - visibility[0][0]) ** 2 + (visibility[2][1] - visibility[0][1]) ** 2) ** 1 / 2
BC = ((visibility[1][0] - visibility[2][0]) ** 2 + (visibility[2][1] - visibility[1][1]) ** 2) ** 1 / 2
p = (BA + CA + BC) / 2
S = (p * (p - BA) * (p - CA) * (p - BC)) ** 1 / 2
print(S)