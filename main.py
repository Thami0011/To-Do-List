import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from func import *

# Environment variables
color = "#fff3c7"
available_tasks = []

# Setting functions

### Converts from the file to Task objects listed in a list.
def charge():
    with open("Assets/Tasks.md", "r") as file:
        for value in file:
            words = value.split()
            name = ' '.join(words[:-1])
            value = True if words[-1].lower() == "true" else False
            available_tasks.append(Task(name, value))

### Refreshes the actual list of tasks.      
def refresh():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for i, item in enumerate(available_tasks):
        val = tk.BooleanVar(value=item.value)
        check = ttk.Checkbutton(task_frame, text=item.name, variable=val, command=item.changeValue)
        check.grid(row=i, column=0, sticky="w",pady=5)
        delbutton = ttk.Button(task_frame,text="Delete Task",command=lambda current_item=item: remove_task(current_item))
        delbutton.grid(row=i, column=1,padx=(50,0))

def remove_task(item):
    available_tasks.remove(item)
    del item
    refresh()




### Saves the changes.
def save():    
    file = open("Assets/Tasks.md", 'w')
    for item in available_tasks:
        file.write(f"{item.name} {item.value}\n")
    file.close()

### Disables button as long as entry is empty.
def enable_button(*args):
    if entry_var.get():
        submit_button["state"] = "normal"
    else:
        submit_button["state"] = "disabled"

### Adding a new task to the list variable.
def add():
    available_tasks.append(Task(entry_var.get(), False))
    entry_var.set("")
    refresh()


def on_enter(event):
    if entry_var.get():
        add()


# Initializing the window.
window = ThemedTk(theme="breeze")
ttk.Style().configure("TCheckbutton", background=color)
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


# Create a frame to hold the checkbuttons.
task_frame = tk.Frame(window, bg=color)
task_frame.pack(side="top", anchor="w", pady=0, padx=10)


charge()
refresh()



entry.bind("<Return>", on_enter)
# Launching the app
window.mainloop()
save()
