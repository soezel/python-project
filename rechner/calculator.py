import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Taschenrechner")
        master.configure(bg="#de8559")

        # Erstellen der Anzeige
        self.display = tk.Entry(
            master, width=25, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Erstellen der Buttons
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
        ]
        row = 1
        col = 0
        for button_text in buttons:
            button = tk.Button(master, text=button_text, width=5, height=2, font=("Arial", 12),
                               command=lambda text=button_text: self.button_click(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Erstellen des "="-Buttons
        equals_button = tk.Button(master, text="=", width=5, height=2, font=("Arial", 12),
                                  command=self.calculate)
        equals_button.grid(row=5, column=2, padx=5, pady=5)

    def button_click(self, text):
        # Fügt den Text des gedrückten Buttons zur Anzeige hinzu
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + text)

    def calculate(self):
        # Berechnet den Ausdruck in der Anzeige
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")


window = tk.Tk()
window.iconbitmap("rechner/icon/taschenrechner.ico")
calc = Calculator(window)
window.mainloop()
