import tkinter as tk
from tkinter.font import Font
from finalsystem import add_fact, ask_question

## GUI constants
buttonwidth = 30
buttonheight = 3

## GUI elements
window = tk.Tk()
window.geometry("700x300")
window.title("Pharmacy Help")
mainframe = tk.Frame(window)
mainframe.pack()

def first_question(inquiry, starting_question):
    clear_frame(mainframe)
    show_question(inquiry)
    show_explanation(inquiry)
    show_age_buttons()
    show_next_button(starting_question)
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
    tk.Label(
        mainframe,
        text    = question,
        font    = Font(size=16),
        width   = 100,
        height  = 3,
    ).pack()

def show_explanation(inquiry):
    explanation = inquiry[1]
    if explanation is not None:
        tk.Label(
            mainframe,
            text   = explanation,
            font   = Font(size=12),
            width  = 100,
            height = 3
        ).pack()

def show_age_buttons():
    var = tk.StringVar()
    button1 = tk.Radiobutton(
                text     = "months",
                variable = var,
                value    = 1
              ).pack()
    button2 = tk.Radiobutton(
                text     = "years",
                variable = var,
                value    = 2
              ).pack()

def show_next_button(question):
    print("number")

def show_buttons(inquiry):
    for option in inquiry[2:]:
        answer = option[0]
        fact = option[1]
        tk.Button(
            mainframe,
            text    = answer,
            width   = buttonwidth,
            height  = buttonheight,
            command = lambda fact = fact: add_fact(fact)
        ).pack()

def show_advice(advice):
    mainframe.pack_forget()                 # clear the frame
    text = tk.Label(text = "ADVICE: " + advice, font = Font(size=14))
                                            # center the label in the frame
    text.place(relx=.5, rely=.5, anchor="center")
