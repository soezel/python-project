import tkinter as tk

# Fenster erstellen
window = tk.Tk()
window.title("BMI Rechner")
window.iconbitmap("rechner/icon/bmi.ico")

# Farbschema definieren
background_color = "#f4f4f4"
accent_color = "#316349"
text_color = "#333333"

# Funktion zum Berechnen des BMI


def calculate_bmi():
    height = float(height_entry.get()) / 100
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    bmi_label.config(text=f"Ihr BMI beträgt: {bmi:.2f}", fg=accent_color)

    if bmi < 18.5:
        status_label.config(text="Untergewicht", fg="#ff6347")
    elif 18.5 <= bmi < 25:
        status_label.config(text="Normalgewicht", fg="#32cd32")
    elif 25 <= bmi < 30:
        status_label.config(text="Übergewicht", fg="#ffa500")
    else:
        status_label.config(text="Adipositas", fg="#ff4500")


# Widgets erstellen
title_label = tk.Label(window, text="BMI Rechner", font=(
    "Helvetica", 16), bg=background_color, fg=text_color)
height_label = tk.Label(window, text="Größe (in cm)",
                        bg=background_color, fg=text_color)
height_entry = tk.Entry(window, bg=background_color, fg=text_color)
weight_label = tk.Label(window, text="Gewicht (in kg)",
                        bg=background_color, fg=text_color)
weight_entry = tk.Entry(window, bg=background_color, fg=text_color)
calculate_button = tk.Button(
    window, text="BMI berechnen", command=calculate_bmi, bg=accent_color, fg="white")
bmi_label = tk.Label(window, bg=background_color, fg=text_color)
status_label = tk.Label(window, bg=background_color, fg=text_color)

# Widgets positionieren
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
height_label.grid(row=1, column=0, padx=10, pady=10)
height_entry.grid(row=1, column=1, padx=10, pady=10)
weight_label.grid(row=2, column=0, padx=10, pady=10)
weight_entry.grid(row=2, column=1, padx=10, pady=10)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
bmi_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Fenster anzeigen
window.mainloop()
