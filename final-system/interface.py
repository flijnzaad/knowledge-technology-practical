from tkinter import *
from tkinter.font import Font

## GUI constants
text_width = 600
text_height = 3
button_width  = 30
button_height = 3

## GUI elements
window = Tk()
dimensions = "700x400"
window.geometry(dimensions)
window.resizable(0, 0)
window.title("Pharmacy Help")
mainframe = Frame(window)
mainframe.pack()

def start(starting_message, starting_question):
    Label(
        mainframe,
        text = starting_message, 
        font = Font(size = 12),
        wraplength = text_width
    ).pack(expand = YES)
    from finalsystem import ask_question
    Button(
        mainframe,
        text    = "Let's go!",
        width   = button_width,
        height  = button_height,
        command = lambda: ask_question(starting_question)
    ).pack(expand = YES)
    window.mainloop()

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
    Label(
        mainframe,
        text    = question,
        font    = Font(size = 16),
        height  = text_height,
        wraplength = text_width
    ).pack()

def show_explanation(inquiry):
    explanation = inquiry[1]
    if explanation is not None:
        Label(
            mainframe,
            text   = explanation,
            font   = Font(size=12),
            height = text_height,
            wraplength = text_width
        ).pack()

def show_buttons(inquiry):
    from finalsystem import add_fact
    for option in inquiry[2:]:
        answer = option[0]
        fact = option[1]
        Button(
            mainframe,
            text    = answer,
            width   = button_width,
            height  = button_height,
            command = lambda fact = fact: add_fact(fact)
        ).pack()

def show_advice(advice):
    mainframe.pack_forget()                     # clear the frame
    recommendation = advice[0]
    additions = advice[1]
    Label(
        text = "ADVICE:\n" + recommendation, 
        font = Font(size = 14, weight = "bold"),
        justify = LEFT,
        wraplength = text_width
    ).pack(expand = YES)
    if additions:
        Label(
            text = "ADDITIONAL INFORMATION:\n" + additions, 
            font = Font(size = 12),
            justify = LEFT,
            wraplength = text_width
        ).pack(expand = YES)
    Button(
            text    = "Exit",
            width   = button_width,
            height  = button_height,
            command = lambda: window.destroy()
    ).pack()