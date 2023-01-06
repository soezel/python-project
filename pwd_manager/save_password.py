def save_password(index="1",name="Max",password="123",notiz="Test"):
    with open("FI-B-Passwortmanager.txt", "a") as pwd_handle:
        pwd_handle.write("{0},{1},{2},{3}\n".format(index,name,password,notiz))
