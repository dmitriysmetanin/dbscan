import random
import pygame

def get_points_by_mouse(AX, AY):
    pygame.init()
    points = []
    screen = pygame.display.set_mode((640, 640))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                points.append((x / 640 * AX,
                               (640 - y) / 640 * AY))
                pygame.draw.circle(screen, (128, 128, 128, 1), (x, y), 5)
                pygame.display.update()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return points
