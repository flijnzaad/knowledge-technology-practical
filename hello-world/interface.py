import tkinter as tk                        # tkinter for using GUI 
from hello_world import muscle_pain

## GUI elements
window = tk.Tk()
window.geometry("300x200")
window.title("Pharmacy Help")
frame  = tk.Frame(window)
frame.pack()
tk.Label(
    frame,
    text    = "Do you have muscle pain?",
    width   = 25,
    height  = 3
).pack()

tk.Button(
    frame,
    text    = "Yes",
    width   = 20,
    height  = 3,
    command = lambda: muscle_pain(True)     # function called when pressed 
).pack()

tk.Button(
    frame,
    text    = "No",
    width   = 20,
    height  = 3,
    command = lambda: muscle_pain(False)    # function called when pressed
).pack()

window.mainloop()                           # keep window running until closed 

def show_message(message):
    frame.pack_forget()
    text = tk.Label(text = message)
    text.place(relx=.5, rely=.5, anchor="center")