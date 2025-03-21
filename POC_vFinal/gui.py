import tkinter as tk
from tkinter import ttk
from application import get_recommendations

window = tk.Tk()
window.geometry("600x800")

window.title("Wybór Studiów")

def handle_button_press(event):
    window.destroy()

    # pobiera dane podane przez użytkownika i przekazuje go  get_recommendations()
def search():
        city = city_var.get()
        interests = interest_entry.get()
        results = get_recommendations(city, interests)

        # formatowanie wyników (aby poprawnie były wypisywane)
        if all(isinstance(item, str) and len(item) == 1 for item in results):
            formatted_results = "".join(results)  # scala pojedyncze litery w tekst
        else:
            formatted_results = "\n\n".join(map(str, results))

        result_label.config(text=formatted_results)


# Pole do wpisania miasta
tk.Label(window, text="Podaj miasto:").pack(pady=2)
city_var = tk.StringVar()
city_entry = tk.Entry(window, textvariable=city_var)
city_entry.pack(pady=2)


# Zainteresowania
tk.Label(window, text="Podaj swoje zainteresowania:").pack(pady=2)
interest_entry = tk.Entry(window)
interest_entry.pack(pady=2)

# Przycisk do wyszukania
search_button = tk.Button(window, text="Znajdź kierunki studiów", command=search)
search_button.pack(pady=5)

# Pole do wyświetlenia wyników
result_label = tk.Label(window, text="", wraplength=400, justify="left", anchor="w")
result_label.pack(pady=5)

# Start the event loop.
window.mainloop()