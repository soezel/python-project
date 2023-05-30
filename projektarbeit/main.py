import pygame
import sys
import random

class Player:
    def __init__(self, x_position, y_position, speed):
        self.x_position = x_position
        self.y_position = y_position
        self.jumping = False
        self.y_gravity = 0.6
        self.jump_height = 20
        self.y_velocity = self.jump_height
        self.speed = speed

        self.images = [
            pygame.transform.scale(pygame.image.load("projektarbeit/assets/luma1.png"), (200, 200)),
            pygame.transform.scale(pygame.image.load("projektarbeit/assets/luma2.png"), (200, 200))
        ]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]

        self.player_animation_delay = 200  # Zeitverzögerung für die Animation des Spielers in Millisekunden
        self.last_player_animation_time = pygame.time.get_ticks()

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.y_velocity = self.jump_height
   
    def update(self):
        if self.jumping:
            self.y_position -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_position > 660:
                self.jumping = False
                self.y_position = 660

        # Animation des Spielers
        if pygame.time.get_ticks() - self.last_player_animation_time > self.player_animation_delay:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image = self.images[self.current_image_index]
            self.last_player_animation_time = pygame.time.get_ticks()

    def draw(self, screen):
        player_rect = self.image.get_rect(center=(self.x_position, self.y_position))
        screen.blit(self.image, player_rect)

class Enemy:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.speed = 3

        self.images = [
            pygame.transform.scale(pygame.image.load("projektarbeit/assets/oktar1.png"), (200, 200)),
            pygame.transform.scale(pygame.image.load("projektarbeit/assets/oktar2.png"), (200, 200))
        ]
        self.current_image_index = 0
        self.image = self.images[self.current_image_index]

        self.animation_delay = 200  # Zeitverzögerung für die Animation des Gegners in Millisekunden
        self.last_animation_time = pygame.time.get_ticks()

    def update(self):
        self.x_position -= self.speed

        # Animation des Gegners
        if pygame.time.get_ticks() - self.last_animation_time > self.animation_delay:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.image = self.images[self.current_image_index]
            self.last_animation_time = pygame.time.get_ticks()

    def draw(self, screen):
        enemy_rect = self.image.get_rect(center=(self.x_position, self.y_position))
        screen.blit(self.image, enemy_rect)

def check_collision(player, enemy):
    player_rect = pygame.Rect(player.x_position + 15, player.y_position + 15, player.image.get_width() - 150, player.image.get_height() - 150)
    enemy_rect = pygame.Rect(enemy.x_position + 15, enemy.y_position + 15, enemy.image.get_width() - 150, enemy.image.get_height() - 150)
    if player_rect.colliderect(enemy_rect):
        return True
    return False

# Initialisieren des Pygame-Fensters
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Frenzy: Battle Against Octopods Invasion")

# Position des Charakters
x_position, y_position = 400, 660

# Bilder laden und skalieren
background = pygame.transform.scale(pygame.image.load("projektarbeit/assets/background.png"), (600, 780))
background_width = background.get_width()
background_position = 0

player = Player(x_position, y_position, 0.3)
enemy = Enemy(random.randint(800, 1600), y_position)

game_over = False
score = 0

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
        player.jump()

    # Hintergrundbild darstellen und bewegen
    screen.blit(background, (background_position % background_width - background_width, 0))
    screen.blit(background, (background_position % background_width, 0))
    background_position -= player.speed * 6  # Hintergrundbewegungsgeschwindigkeit

    player.update()
    enemy.update()

    player.draw(screen)
    enemy.draw(screen)

    # Wenn Gegner den linken Bildschirmrand erreicht, setze ihn zufällig auf den rechten Rand
    if enemy.x_position + enemy.image.get_width() < 0:
        enemy.x_position = random.randint(800, 1600)
        score += 1

    # Kollisionsprüfung
    if check_collision(player, enemy):
        game_over = True

    # Punkte anzeigen
    font = pygame.font.Font(None, 36)
    score_text = font.render("Punkte: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Pygame Fenster aktualisieren
    pygame.display.update()
    clock.tick(60)

# Spiel vorbei, zeige Game Over Nachricht und Punktzahl
game_over_font = pygame.font.Font(None, 64)
game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(500, 400))
screen.blit(game_over_text, game_over_rect)

score_text = font.render("Punkte: " + str(score), True, (255, 255, 255))
score_rect = score_text.get_rect(center=(500, 500))
screen.blit(score_text, score_rect)

pygame.display.update()

# Warte einige Sekunden, bevor das Spiel beendet wird
pygame.time.wait(3000)
pygame.quit()
sys.exit()
