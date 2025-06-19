import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Moving Smile")
    screen = pygame.display.set_mode((640, 480))
    eye_x = 0
    eye_y = 0
    while True:
        # TODO 4: Set the clock speed to 60 fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pressed_keys = pygame.key.get_pressed()
            if  pressed_keys[pygame.K_LEFT]:
                eye_x = eye_x - 5
            if pressed_keys[pygame.K_RIGHT]:
                eye_x = eye_x + 5
            if pressed_keys[pygame.K_UP]:
                eye_y = eye_y - 5
            if pressed_keys[pygame.K_DOWN]:
                eye_y = eye_y + 5


        screen.fill((255, 255, 255))  # white

        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240 + eye_x, 160 + eye_y), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240 + eye_x, 160 + eye_y), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242 + eye_x, 162 + eye_y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400 + eye_x, 160 + eye_y), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400 + eye_x, 160 + eye_y), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398 + eye_x, 162 + eye_y), 7)  # black pupil

        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        pygame.draw.circle(screen, (100,255,0), (320, 245), 25)

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)

        pygame.display.update()


main()
