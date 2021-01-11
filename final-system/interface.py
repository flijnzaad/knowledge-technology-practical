import tkinter as tk
from tkinter.font import Font
from finalsystem import add_fact

## GUI constants
text_width = 100
text_height = 3
button_width  = 30
button_height = 3
window_width  = 700
window_height = 500

## GUI elements
window = tk.Tk()
dimensions = str(window_width) + 'x' + str(window_height)
window.geometry(dimensions)
window.resizable(0, 0)
window.title("Pharmacy Help")
mainframe = tk.Frame(window)
mainframe.pack()

def show_inquiry(inquiry):
    clear_frame(mainframe)
    show_question(inquiry)
    show_explanation(inquiry)
    show_buttons(inquiry)
    window.mainloop()

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def show_question(inquiry):
    question = inquiry[0]
    tk.Label(
        mainframe,
        text    = question,
        font    = Font(size = 16),
        width   = text_width,
        height  = text_height,
        wraplength = window_width
    ).pack()

def show_explanation(inquiry):
    explanation = inquiry[1]
    if explanation is not None:
        tk.Label(
            mainframe,
            text   = explanation,
            font   = Font(size=12),
            width  = text_width,
            height = text_height,
            wraplength = window_width
        ).pack()

def show_buttons(inquiry):
    for option in inquiry[2:]:
        answer = option[0]
        fact = option[1]
        tk.Button(
            mainframe,
            text    = answer,
            width   = button_width,
            height  = button_height,
            command = lambda fact = fact: add_fact(fact)
        ).pack()

def show_advice(full_advice):
    mainframe.pack_forget()                     # clear the frame
    advice = full_advice[0]
    additions = full_advice[1]
    text = tk.Label(
        text = "ADVICE:\n" + advice, 
        font = Font(size = 14, weight = "bold"),
        width = text_width,
        wraplength = window_width
    ).pack(side = "top")
    text = tk.Label(
        text = additions, 
        font = Font(size = 12),
        width = text_width,
        wraplength = window_width
    ).pack(side = "bottom")