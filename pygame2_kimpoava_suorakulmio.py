# Import a library of functions called 'pygame'
import pygame
import random

# Initialize the game engine
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]

# Set the height and width of the screen
SIZE = [400, 400]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Kimpoava suorakulmio")

# Aloituspiste
rect_x = 50
rect_y = 50

# Neliön suunta ja nopeus
rect_change_x = 5
rect_change_y = 5

clock = pygame.time.Clock()
# -------- ohjelman pääsilmukka ---
# Loop until the user clicks the close button.
done = False
while done == False:
    for event in pygame.event.get():  # Käyttäjä teki jotain
        if event.type == pygame.QUIT:  # Jos klikattiin sulje
            done = True  # 'booleanlippu', jolla poistutaan silmukasta

    # Asetetaan tausta mustaksi
    screen.fill(BLACK)

    # Piirretään neliö
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    # Piirretään punainen neliö valkoisen sisään
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])

    # Liikutetaan neliötä aloituspisteestä
    rect_x += rect_change_x
    rect_y += rect_change_y
    # Objekti kimpoaa tarvittaessa
    if rect_y > 350 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 350 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()