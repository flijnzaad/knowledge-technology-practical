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
age = tk.StringVar()

def first_question(inquiry, starting_question):
    clear_frame(mainframe)
    show_question(inquiry)
    show_explanation(inquiry)
    show_age_buttons()
    show_next_button(starting_question)
    for i in mainframe.winfo_children():
        print(i.winfo_class())
    window.mainloop()

def show_inquiry(inquiry):
    clear_frame(mainframe)
    show_question(inquiry)
    show_explanation(inquiry)
    show_buttons(inquiry)
    for i in mainframe.winfo_children():
        print(i.winfo_class())
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
    button1 = tk.Radiobutton(
        text     = "0 - 3 months",
        variable = age,
        value    = "age(under_3_months)"
    )
    button1.pack( anchor = tk.W )
    button1.select()

    tk.Radiobutton(
        text     = "3 - 12 months",
        variable = age,
        value    = "age(under_1_year)"
    ).pack( anchor = tk.W )
    tk.Radiobutton(
        text     = "1 - 2 years",
        variable = age,
        value    = "age(under_2_years)"
    ).pack( anchor = tk.W )
    tk.Radiobutton(
        text     = "2 - 6 years",
        variable = age,
        value    = "age(under_6_years)"
    ).pack( anchor = tk.W )
    tk.Radiobutton(
        text     = "older than 6 years",
        variable = age,
        value    = "age(no_importance)"
    ).pack( anchor = tk.W )

def show_next_button(question):
    tk.Button(
        mainframe,
        text    = "Next",
        width   = 5,
        height  = 1,
        command = lambda: callback(question)
    ).pack( anchor = tk.SE )

def callback(question):
    add_fact(age.get())
    ask_question(question)

def show_buttons(inquiry):
    for option in inquiry[2:]:
        answer = option[0]
        fact = option[1]
        tk.Button(
            mainframe,
            text    = answer,
            width   = buttonwidth,
            height  = buttonheight,
            command = lambda: add_fact(fact)
        ).pack()

def show_advice(advice):
    mainframe.pack_forget()                 # clear the frame
    text = tk.Label(text = "ADVICE: " + advice, font = Font(size=14))
                                            # center the label in the frame
    text.place(relx=.5, rely=.5, anchor="center")
