import tkinter as tk
from prototype import add_fact

## GUI constants
buttonwidth = 50
buttonheight = 3

## GUI elements
window = tk.Tk()
window.geometry("900x900")
window.title("Pharmacy Help")
mainframe = tk.Frame(window)
mainframe.pack()

def show_inquiry(inquiry):
    clear_frame(mainframe)
    show_question(inquiry[0])
    show_buttons(inquiry)
    window.mainloop()

def show_question(question):
    tk.Label(
        mainframe,
        text    = question,
        width   = 100,
        height  = 3
    ).pack()

def show_buttons(inquiry):
    for option in inquiry[1:]:
        answer = option[0]
        fact = option[1]
        tk.Button(
            mainframe,
            text    = answer,
            width   = buttonwidth,
            height  = buttonheight,
            command = lambda fact = fact: add_fact(fact)
        ).pack()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_advice(advice):
    mainframe.pack_forget()                     # clear the frame
    text = tk.Label(text = "ADVICE: " + advice)
                                            # center the label in the frame
    text.place(relx=.5, rely=.5, anchor="center")
