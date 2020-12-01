import tkinter as tk
from prototype import add_fact

## GUI elements
window = tk.Tk()
window.geometry("300x200")
window.title("Pharmacy Help")
frame  = tk.Frame(window)
frame.pack()

def show_question(question, answer1, fact1, answer2, fact2):
    tk.Label(
        frame,
        text    = question,
        width   = 25,
        height  = 3
    ).pack()

    tk.Button(
        frame,
        text    = answer1,
        width   = 20,
        height  = 3,
        command = lambda: add_fact(fact1)
    ).pack()

    tk.Button(
        frame,
        text    = answer2,
        width   = 20,
        height  = 3,
        command = lambda: add_fact(fact2)
    ).pack()

    window.mainloop()

def show_advice(advice):
    frame.pack_forget()                     # clear the frame
    text = tk.Label(text = "ADVICE: " + advice)
                                            # center the label in the frame
    text.place(relx=.5, rely=.5, anchor="center")
