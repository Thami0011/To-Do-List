import tkinter as tk
from ttkthemes import ThemedTk
import func

color = "#fff3c7"

# Initializing the window
window = ThemedTk(theme="breeze")
window.title("List IT")
window.geometry("1000x700")
window.resizable(True, True)
window.iconbitmap("Assets/ListIT.ico")

# Setting the background color :
window.configure(bg=color)

# Setting the window title
title = tk.Label(window, text="ListIT - Your To Do List App !", width=70, bg=color, font=("Protest Strike", 14, "bold"))
title.pack(pady=5)

check = tk.Checkbutton(window)
check.pack()




# Launching the app
window.mainloop()

