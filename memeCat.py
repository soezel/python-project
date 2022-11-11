### Auflistung der Möglichen Katzen
### Input von User 
### Ausgabe in txt

from outputAsciiNyanCat import OutputAsciiNyanCat
from outputAsciiBongoCat import OutputAsciiBongoCat
from outputAsciiLordNermal import OutputAsciiLordNermal
from printing import printIndividually, printingGreeting
 
class MemeCat():
    def main (self):
        printingGreeting()
        Input().userInput()
        
class Input():        
    def userInput(self):
        # print("\nPlease Choose from these options to see in Ascii Art \nand don't forget to write the names right (o'ω'o):")
        printIndividually("\n✿ Bongo Cat\n✿ Nyan Cat\n✿ Lord Nermal\n")
        cat = input("> ")
        # time.sleep(1)
        if cat == "Bongo Cat":
            return OutputAsciiBongoCat().asciiBongo(), printIndividually("\nHopefully you'll like the artwork made for you (✿◠‿◠)\n")
        elif cat == "Nyan Cat":
            return OutputAsciiNyanCat().asciiNyan(), printIndividually("\nHopefully you'll like the artwork made for you (✿◠‿◠)\n")
        elif cat == "Lord Nermal":
            return OutputAsciiLordNermal().asciiNermal(), printIndividually("\nHopefully you'll like the artwork made for you (✿◠‿◠)\n")
        else:
            printIndividually("You typed the name wrong… ¯\_(ツ)_/¯\n")

if __name__ == '__main__':
        MemeCat().main()
