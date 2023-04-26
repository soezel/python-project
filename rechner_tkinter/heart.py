import tkinter as tk
from tkinter import messagebox


def calculate_love():
    name1 = eingabe1.get()
    name2 = eingabe2.get()
    ergebnis = len(set(name1.lower()) & set(name2.lower())) / \
        len(set(name1.lower()) | set(name2.lower())) * 100
    messagebox.showinfo("Ergebnis", "Die Liebe zwischen {} und {} beträgt {:.2f}%".format(
        name1, name2, ergebnis))


window = tk.Tk()
window.title("Liebesrechner")
window.iconbitmap("rechner/icon/heart.ico")
window.configure(bg="#bf699a")

# Setze die Größe des Fensters auf 500x300 Pixel
window.geometry("500x300")

eingabe1_label = tk.Label(
    window, text="Name der ersten Person:", font=("Arial", 20))
eingabe1_label.pack(pady=10)
eingabe1 = tk.Entry(window, font=("Arial", 20))
eingabe1.pack(pady=20)

eingabe2_label = tk.Label(
    window, text="Name der zweiten Person:", font=("Arial", 20))
eingabe2_label.pack(pady=10)
eingabe2 = tk.Entry(window, font=("Arial", 20))
eingabe2.pack(pady=20)

berechnen_button = tk.Button(
    window, text="Berechnen", command=calculate_love, font=("Arial", 20))
berechnen_button.pack()

window.mainloop()
