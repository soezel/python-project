import pygame
import sys

# Initialisiere Pygame
pygame.init()

# Definiere die Bildschirmgröße
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Lade die beiden PNG-Bilder
image1 = pygame.transform.scale(pygame.image.load("projektarbeit/assets/oktar1.png"), (200, 200))
image2 = pygame.transform.scale(pygame.image.load("projektarbeit/assets/oktar2.png"), (200, 200))

# Überprüfe, ob die Bilder die gleiche Größe haben
if image1.get_size() != image2.get_size():
    raise ValueError("Die Bilder müssen die gleiche Größe haben.")

# Definiere die Anzahl der Frames und die Animationsgeschwindigkeit
num_frames = 50
animation_speed = 100  # Frames pro Sekunde

# Hauptanimationschleife
current_frame = 0
image_index = 0  # Index, um die beiden Bilder abwechselnd zu wechseln
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Berechne den Alpha-Wert für den aktuellen Frame
    alpha = current_frame / (num_frames - 1)

    # Wähle das aktuelle Bild basierend auf dem Bildindex
    if image_index == 0:
        current_image = image1
    else:
        current_image = image2

    # Mische das aktuelle Bild basierend auf dem Alpha-Wert
    interpolated_image = pygame.Surface(current_image.get_size(), pygame.SRCALPHA)
    interpolated_image.blit(current_image, (0, 0))
    interpolated_image.set_alpha(int(alpha * 255))

    # Zeichne das Zwischenbild auf den Bildschirm
    screen.fill((0, 0, 0))
    screen.blit(interpolated_image, (0, 0))
    pygame.display.flip()

    # Aktualisiere den aktuellen Frame und den Bildindex
    current_frame += 1
    if current_frame >= num_frames:
        current_frame = 0
        # Wechsle den Bildindex
        image_index = (image_index + 1) % 2

    clock.tick(animation_speed)
