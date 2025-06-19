import pygame
import sys
import time

clock = pygame.time.Clock()

def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    pygame.time.Clock()

    # initialize the pygame module
    pygame.init()
    image1 = pygame.image.load("2dogs.jpg")
    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # done 1: Create an image with the 2dogs.JPG image
    image1 = pygame.transform.scale(image1, (IMAGE_SIZE, IMAGE_SIZE))
    # done 3: Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)

    # Prepare the text caption(s)
    # done 4: Create a font object with a size 28 font.

    font2 = pygame.font.SysFont('comicsans', 50)
    caption2 = font2.render('aaahhh', True, BLACK)

    # done 5: Render the text "Two Dogs" using the font object (it's like MAKING an image).

    # Prepare the music
    # done 8: Create a Sound object from the "bark.wav" file.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # done 9: Play the music (bark) if there's a mouse click.
        press = pygame.key.get_pressed()
        if press[pygame.K_SPACE]:
            sound1 = pygame.mixer.Sound('bark.wav')
       # if press[pygame.K_SPACE]:
        sound1.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # done 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(image1, (0, 0))

        # Draw the text onto the screen
        # TODO 6: done (blit) the text image onto the screen in the middle bottom.

        screen.blit(caption2 , (image1.get_width()//2 - caption2.get_width()//2, image1.get_height()//2))
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()

        # TODO 7: On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()


main()
