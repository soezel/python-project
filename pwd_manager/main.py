from database_print import *
from save_password import *
from create_database import *
# from show_database import *
# from output_pwd import Output_pwd

class main():
    create_database()
    def pwd_manager():
        pwd_block()
        manage_password()
        option = input("Auswahl:")
        match option:
            case "1":
                save_password()
        
# class Input():
#     def new_name():
        # pwd_controller = Output_pwd(" ")
        # pwd_controller.txt = input("Bitte den Namen der Datenbank eingeben: ")
        # Show_database().show()
 

if __name__ == '__main__':
    main.pwd_manager()