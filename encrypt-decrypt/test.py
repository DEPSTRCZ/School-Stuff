import tkinter as tk

root = tk.Tk()

# získáme rozměry okna
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()

# vytvoříme Label widget s textem "Uprostřed okna"
label = tk.Label(root, text="Uprostřed okna")

# určíme pozici label widgetu
label.grid(row=0, column=0)

# nastavíme vlastnosti sloupců a řádků
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
