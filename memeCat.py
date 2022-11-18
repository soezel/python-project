### Auflistung der Möglichen Katzen
### Input von User 
### Ausgabe in txt


from outputAscii import OutputAscii
from printing import printIndividually, printingGreeting
 
class MemeCat():
    def main (self):
        
        printingGreeting()
        Input().userInput()
        
class Input():     
    def userInput(self):
        outputBongo = OutputAscii(" ", " ")
        outputBongo.image = outputBongo.pathImage("/Users/ebruozel/Desktop/Schule 2 Year/Python/CatProj/assets/bongo_cat.jpeg")
        outputBongo.txt = "bongo_cat.txt"

        outputNyan = OutputAscii(" ", " ")
        outputNyan.image = outputNyan.pathImage("/Users/ebruozel/Desktop/Schule 2 Year/Python/CatProj/assets/nyan_cat.jpeg")
        outputNyan.txt = "nyan_cat.txt"

        outputNermal = OutputAscii(" ", " ")
        outputNermal.image = outputNermal.pathImage("/Users/ebruozel/Desktop/Schule 2 Year/Python/CatProj/assets/nyan_cat.jpeg")
        outputNermal.txt = "lord_nermal.txt"

        print("\nPlease Choose from these options to see in Ascii Art \nand don't forget to write the names right (o'ω'o):")
        printIndividually("\n✿ Bongo Cat\n✿ Nyan Cat\n✿ Lord Nermal\n")
        cat = input("> ")
        if cat == "Bongo Cat":
            return outputBongo.ascii(), printIndividually("\nHopefully you'll like the artwork made for you (✿◠‿◠)\n")
        elif cat == "Nyan Cat":
            return outputNyan.ascii(), printIndividually("\nHopefully you'll like the artwork made for you (✿◠‿◠)\n")
        elif cat == "Lord Nermal":
            return outputNermal.ascii(), printIndividually("\nHopefully you'll like the artwork made for you (✿◠‿◠)\n")
        else:
            printIndividually("You typed the name wrong… ¯\_(ツ)_/¯\n")

if __name__ == '__main__':
        MemeCat().main()
