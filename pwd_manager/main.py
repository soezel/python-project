from database_print import *
from new_database import *
from show_database import *
from output_pwd import Output_pwd

class Passwordmanager():
    def main():
        pwd_block()
        pwd_database()
        option = input("Auswahl:")
        match option:
            case "1":
                New_database().new()
        
class Input():
    def new_name():
        pwd_controller = Output_pwd(" ")
        pwd_controller.txt = input("Bitte den Namen der Datenbank eingeben: ")
        Show_database().show()
 

if __name__ == '__main__':
    Passwordmanager.main()