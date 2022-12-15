from PIL import Image

asciiCharacters = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]


class Cat():
    def __init__(self, image, txt):
        self.image = image
        self.txt = txt
        
    def get_image(self):
        return str(self.image)
    def set_image(self,image):
        self.image = image

    def get_txt(self):
        return str(self.txt)
    def set_txt(self, txt):
        self.txt = txt

    def pathImage(self, str):
        self.image = Image.open(str)
        return self.image

    def ascii(self):
        self.image
        width, height = self.image.size
        aspect_ratio = height/width
        new_width = 140
        new_height = aspect_ratio * new_width * 0.55
        self.image = self.image.resize((new_width, int(new_height)))
        ascii_art = convertToAsciiArt(self.image)
        saveAsText(self, ascii_art)

def convertToAsciiArt(image):
    ascii_art = []
    (width, height) = image.size
    for y in range(0, height - 1):
        line = ''
        for x in range(0, width - 1):
            px = image.getpixel((x, y))
            line += convertPixelToCharacter(px)
        ascii_art.append(line)
    return ascii_art

def convertPixelToCharacter(pixel):
    (r, g, b) = pixel
    pixel_brightness = r + g + b
    max_brightness = 255 * 3
    brightness_weight = len(asciiCharacters) / max_brightness
    index = int(pixel_brightness * brightness_weight) - 1
    return asciiCharacters[index]

def saveAsText(self, ascii_art):
    with open(self.txt, "w") as file:
        for line in ascii_art:
            file.write(line)
            file.write('\n')
            # print(line + '\n')
        file.close()