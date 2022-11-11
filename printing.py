
import sys
import time

def printingGreeting():
    printIndividually("\n●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●\n")
    print("\nWelcome to The Ascii Art Gallery! (´･ω･`) \nToday it's all about Meme Cats!!\n")
    printIndividually("●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●●")
    print("\nPlease Choose from these options to see in Ascii Art \nand don't forget to write the names right (o'ω'o):")

def printIndividually(ascii, delay=0.100):
        for a in ascii:
            sys.stdout.write(a)
            sys.stdout.flush()
            time.sleep(delay)

    