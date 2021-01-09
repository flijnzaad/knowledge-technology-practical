import tkinter as tk
from tkinter.font import Font
from finalsystem import add_fact

## GUI constants
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
        width   = 100,
        height  = 3,
        wraplength = window_width,
        # wrap    = tk.WORD
    ).pack()

def show_explanation(inquiry):
    explanation = inquiry[1]
    if explanation is not None:
        tk.Label(
            mainframe,
            text   = explanation,
            font   = Font(size=12),
            width  = 100,
            height = 3,
            wraplength = window_width,
            # wrap   = tk.WORD
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

def show_advice(advice):
    clear_frame(mainframe)
    tk.Label(
        text = "ADVICE: " + advice, 
        font = Font(size = 14)
    ).pack( anchor = tk.N )