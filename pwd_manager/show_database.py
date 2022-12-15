class Show_database():
    def __init__(self, txt):
        self.txt = txt

    def get_txt(self):
        return str(self.txt)
    def set_txt(self, txt):
        self.txt = txt

    def show(self):
        with open(self.txt + ".txt", "w") as handle:
            handle.write("-----------------------------------------\n")
            handle.write("Index Name Passwort Text\n")
            handle.write("-----------------------------------------\n")