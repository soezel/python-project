import pygame
import sys
import random

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

# Gegner laden und skalieren
ENEMY_SURFACE = pygame.transform.scale(pygame.image.load("projektarbeit/assets/gegner.png"), (64, 64))
enemy_x = random.randint(800, 1600)  # Zufällige X-Position des Gegners
enemy_y = Y_POSITION - ENEMY_SURFACE.get_height()  # Y-Position des Gegners (gleich wie Charakter)

# Positionierung des Charakters
rect = STANDING_SURFACE.get_rect(center=(X_POSITION, Y_POSITION))

# Bewegungsgeschwindigkeiten
STEP_SIZE = 0.01
CHARACTER_SPEED = 0.3
ENEMY_SPEED = 3  # Geschwindigkeit des Gegners

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
    background_position -= CHARACTER_SPEED * 4  # Hintergrundbewegungsgeschwindigkeit

    # Gegner nach links bewegen
    enemy_x -= ENEMY_SPEED

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
    X_POSITION += CHARACTER_SPEED

    # Gegner auf dem Bildschirm anzeigen
    enemy_rect = ENEMY_SURFACE.get_rect(topleft=(enemy_x, enemy_y))
    SCREEN.blit(ENEMY_SURFACE, enemy_rect)

    # Wenn Gegner den linken Bildschirmrand erreicht, setze ihn zufällig auf den rechten Rand
    if enemy_x + ENEMY_SURFACE.get_width() < 0:
        enemy_x = random.randint(800, 1600)

    # Pygame Fenster aktualisieren
    pygame.display.update()
    CLOCK.tick(60)
