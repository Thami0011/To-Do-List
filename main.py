import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from func import *

# Environment variables
color = "#fff3c7"
available_tasks = []



# Setting functions
### Converts from the file to Task objects listed in a list
def charge():
    with open("Assets/Tasks.md", "r") as file:
        for value in file:
            words = value.split()
            name = ' '.join(words[:-1])
            value = True if words[-1].lower() == "true" else False
            available_tasks.append(Task(name, value))

### Refreshes the actual list of tasks            
def refresh():
    for item in available_tasks:
        val = tk.BooleanVar()
        val.set(item.value)
        check = ttk.Checkbutton(window, text=item.name,variable=val ,command=item.changeValue, onvalue=True, offvalue=False)
        check.pack(pady=10, anchor="w")
### Saves the changes

def save():
    file = open("Assets/Tasks.md", 'w')
    for item in available_tasks:
        file.write(f"{item.name} {item.value}\n")
    file.close()

def enable_button(*args):
    if entry_var.get():
        submit_button["state"] = "normal"
    else:
        submit_button["state"] = "disabled"

def add():
    available_tasks.append(Task(entry_var.get(), False))
    entry_var.set()
    refresh()


# Initializing the window
window = ThemedTk(theme="breeze")
entry_var = tk.StringVar()
window.title("List IT")
window.geometry("1000x700")
window.resizable(True, True)
window.iconbitmap("Assets/ListIT.ico")
window.configure(bg=color)
title = tk.Label(window, text="ListIT - Your To Do List App !", width=70, bg=color, font=("Protest Strike", 14, "bold"))
title.pack(pady=5)
entry = ttk.Entry(window, textvariable=entry_var)
entry.pack(fill=tk.X, padx=20)
submit_button = ttk.Button(window, text="Add Task", state="disabled", command=add)
submit_button.pack(pady=10)
entry_var.trace_add("write", enable_button)
charge()
refresh()

# Launching the app
window.mainloop()
save()
