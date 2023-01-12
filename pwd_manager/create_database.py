def create_database():
    print("Speichere das Programm")     
            
    with open("FI-B-Passwortmanager.txt", "w") as mein_datei_handle:
        mein_datei_handle.write("-----------------------------------------\n")
        mein_datei_handle.write("Index Name Passwort Text\n")
        mein_datei_handle.write("-----------------------------------------\n")
