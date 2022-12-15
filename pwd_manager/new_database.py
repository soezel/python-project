class New_database():
    def new(self, index = input("Index= "), name = input("Name= "), password = input("Passwort= "), note = input("Notiz= ")):
        with open(self.txt + ".txt", "a") as handle:
            handle.write("{0},{1},{2},{3}\n".format(index,name,password,note))