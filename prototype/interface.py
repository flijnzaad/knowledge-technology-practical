import tkinter as tk
from prototype import add_fact

## GUI elements
window = tk.Tk()
window.geometry("600x800")                  # changed from 600x200 to fit other Qs 
window.title("Pharmacy Help")
frame  = tk.Frame(window)
frame.pack()

def show_question(inquiry):
    question = inquiry[0]

    # frame.pack_forget()                     # clear the frame 
    # TODO: doesn't work

    tk.Label(
        frame,
        text    = question,
        width   = 100,
        height  = 3
    ).pack()

    for option in inquiry[1:]:
        answer = option[0]
        fact = option[1]
        tk.Button(
            frame,
            text    = answer,
            width   = 20,
            height  = 3,
            command = lambda fact = fact: add_fact(fact)
        ).pack()

    window.mainloop()

def show_advice(advice):
    frame.pack_forget()                     # clear the frame
    text = tk.Label(text = "ADVICE: " + advice)
                                            # center the label in the frame
    text.place(relx=.5, rely=.5, anchor="center")
