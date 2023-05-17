import pygame
import sys

pygame.init()

# Initialisieren des Pygame Fensters
CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Frenzy: Battle Against Octopods Invasion")

# Position des Charakters
X_POSITION, Y_POSITION = 400, 660

jumping = False

# Physikalische Variablen
Y_GRAVITY = 0.6
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

# Bilder laden und skalieren
STANDING_SURFACE = pygame.transform.scale(pygame.image.load("projektarbeit/assets/luma1.png"), (48, 64))
JUMPING_SURFACE = pygame.transform.scale(pygame.image.load("projektarbeit/assets/luma2.png"), (48, 64))
BACKGROUND = pygame.image.load("projektarbeit/assets/background.png")
BACKGROUND_WIDTH = BACKGROUND.get_width()
background_position = 0

# Positionierung des Charakter
rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

# Bewegungsgeschwindigkeiten
STEP_SIZE = 0.01
CHARACTER_SPEED = 0.3
BACKGROUND_SPEED = 4

# Endlosschleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tasteneingaben abfragen
    keys_pressed = pygame.key.get_pressed()

    # Wenn Leertaste gedrückt wird, starte Sprung
    if keys_pressed[pygame.K_SPACE]:
        if not jumping:
            jumping = True
            Y_VELOCITY = JUMP_HEIGHT

    # Hintergrundbild darstellen und bewegen
    SCREEN.blit(BACKGROUND, (background_position % BACKGROUND_WIDTH - BACKGROUND_WIDTH, 0))
    SCREEN.blit(BACKGROUND, (background_position % BACKGROUND_WIDTH, 0))
    background_position -= BACKGROUND_SPEED
    if background_position <= -BACKGROUND_WIDTH:
        background_position = 0

    # Wenn Charakter springt
    if jumping:
        # Charakterposition aktualisieren
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_POSITION > 660:
            jumping = False
            Y_POSITION = 660
        mario_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(JUMPING_SURFACE, mario_rect)
    else:
        # Wenn Charakter nicht springt, setze auf stehendes Bild
        mario_rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))
        SCREEN.blit(STANDING_SURFACE, mario_rect)

    # Charakter nach rechts bewegen
    X_POSITION += STEP_SIZE * CHARACTER_SPEED

    # Pygame Fenster aktualisieren
    pygame.display.update()
    CLOCK.tick(60)
