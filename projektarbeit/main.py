import pgzrun

WIDTH = 640
HEIGHT = 480

# Laden Sie das GIF-Image als Animation
char_anim = pgzrun("projektarbeit/assets/luma.gif")

# Definieren Sie die Startposition des Charakters
char_pos = (100, 100)

def draw():
    # Zeichnen Sie den Charakter
    char_anim.draw(char_pos)

# Starten Sie das Spiel
pgzrun.go()
