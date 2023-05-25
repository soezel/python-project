import pygame
import sys
import random

pygame.init()

# Initialisieren des Pygame Fensters
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Frenzy: Battle Against Octopods Invasion")

# Position des Charakters
x_position, y_position = 400, 660

jumping = False
game_over = False

# Physikalische Variablen
y_gravity = 0.6
jump_height = 20
y_velocity = jump_height

# Bilder laden und skalieren
background = pygame.transform.scale(pygame.image.load("projektarbeit/assets/background.png"), (600, 780))
background_width = background.get_width()
background_position = 0

# Gegner laden und skalieren
enemy_surface_1 = pygame.transform.scale(pygame.image.load("projektarbeit/assets/oktar1.png"), (200, 200))
enemy_surface_2 = pygame.transform.scale(pygame.image.load("projektarbeit/assets/oktar2.png"), (200, 200))
enemy_images = [enemy_surface_1, enemy_surface_2]  # Liste mit den beiden Gegner-Bildern
current_enemy_image_index = 0  # Aktueller Index des Gegner-Bildes
enemy_image = enemy_images[current_enemy_image_index]
enemy_x = random.randint(800, 1600)  # Zufällige X-Position des Gegners
enemy_y = y_position

# Spieler laden und skalieren
player_surface_1 = pygame.transform.scale(pygame.image.load("projektarbeit/assets/luma1.png"), (200, 200))
player_surface_2 = pygame.transform.scale(pygame.image.load("projektarbeit/assets/luma2.png"), (200, 200))
player_images = [player_surface_1, player_surface_2]  # Liste mit den beiden Spieler-Bildern
current_player_image_index = 0  # Aktueller Index des Spieler-Bildes
player_image = player_images[current_player_image_index]

# Bewegungsgeschwindigkeiten
character_speed = 0.3
enemy_speed = 3  # Geschwindigkeit des Gegners


# def check_collision():
#     global game_over
#     player_rect = player_image.get_rect(center=(x_position, y_position))
#     enemy_rect = enemy_image.get_rect(center=(enemy_x, enemy_y))
#     if player_rect.colliderect(enemy_rect) and enemy_rect.right < player_rect.centerx:
#         game_over = True
        
def check_collision():
    global game_over
    player_rect = player_image.get_rect(center=(x_position, y_position))
    enemy_rect = enemy_image.get_rect(center=(enemy_x, enemy_y))
    if player_rect.right == enemy_rect.left or player_rect.left == enemy_rect.right:
        game_over = True

        
# Zeitverzögerung für die Animation des Gegners
animation_delay = 200  # Verzögerung in Millisekunden
last_animation_time = pygame.time.get_ticks()

# Zeitverzögerung für die Animation des Spielers
player_animation_delay = 200  # Verzögerung in Millisekunden
last_player_animation_time = pygame.time.get_ticks()

# Endlosschleife
while not game_over:
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
            y_velocity = jump_height

    # Hintergrundbild darstellen und bewegen
    screen.blit(background, (background_position % background_width - background_width, 0))
    screen.blit(background, (background_position % background_width, 0))
    background_position -= character_speed * 6 # Hintergrundbewegungsgeschwindigkeit

    # Gegner nach links bewegen
    enemy_x -= enemy_speed

    # Wenn Charakter springt
    if jumping:
        # Charakterposition aktualisieren
        y_position -= y_velocity
        y_velocity -= y_gravity
        if y_position > 660:
            jumping = False
            y_position = 660

    # Charakter nach rechts bewegen
    x_position += character_speed

    # Animation des Gegners
    if pygame.time.get_ticks() - last_animation_time > animation_delay:
        current_enemy_image_index = (current_enemy_image_index + 1) % len(enemy_images)
        enemy_image = enemy_images[current_enemy_image_index]
        last_animation_time = pygame.time.get_ticks()

    # Animation des Spielers
    if pygame.time.get_ticks() - last_player_animation_time > player_animation_delay:
        current_player_image_index = (current_player_image_index + 1) % len(player_images)
        player_image = player_images[current_player_image_index]
        last_player_animation_time = pygame.time.get_ticks()

   # Spieler auf dem Bildschirm anzeigen
    player_rect = player_image.get_rect(center=(x_position, y_position))
    screen.blit(player_image, player_rect)

# Gegner auf dem Bildschirm anzeigen
    enemy_rect = enemy_image.get_rect(center=(enemy_x, enemy_y))
    screen.blit(enemy_image, enemy_rect)

    # Wenn Gegner den linken Bildschirmrand erreicht, setze ihn zufällig auf den rechten Rand
    if enemy_x + enemy_image.get_width() < 0:
        enemy_x = random.randint(800, 1600)

    # Kollisionsprüfung
    check_collision()

    # Pygame Fenster aktualisieren
    pygame.display.update()
    clock.tick(60)

# Spiel vorbei, zeige Game Over Nachricht
game_over_font = pygame.font.Font(None, 64)
game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(400, 400))
screen.blit(game_over_text, game_over_rect)
pygame.display.update()

# Warte einige Sekunden, bevor das Spiel beendet wird
pygame.time.wait(3000)
pygame.quit()
sys.exit()
