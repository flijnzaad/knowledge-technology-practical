from pyswip import Prolog                   # pyswip for Prolog reasoning 
import tkinter as tk                        # tkinter for using GUI 
pl = Prolog()
pl.consult("hello_world.pl")                # load the knowledge base

## Query handling
def give_advice():
    q = list(pl.query("take(X)"))           # "Should I take any medication?"  

    if q:                                 
        return "You should take " + q[0]["X"] + '.'
    else:                                   # query is empty so no medication 
        return "You don't need any medication."

## Callback function for yes/no buttons 
def muscle_pain(pain = True):
    fact = "pain(muscle)" if pain else "pain(none)"
    pl.asserta(fact)                        # add (dummy) fact to the KB 

    frame.pack_forget()
    advice = tk.Label(text = give_advice())
    advice.place(relx=.5, rely=.5, anchor="center")

## GUI elements
window = tk.Tk()
window.geometry("300x200")
window.title("Pharmacy Help")
frame  = tk.Frame(window)
frame.pack()
question = tk.Label(
    frame,
    text    = "Do you have muscle pain?",
    width   = 25,
    height  = 3
).pack()

yes = tk.Button(
    frame,
    text    = "Yes",
    width   = 20,
    height  = 3,
    command = lambda: muscle_pain(True)     # function called when pressed 
).pack()

no = tk.Button(
    frame,
    text    = "No",
    width   = 20,
    height  = 3,
    command = lambda: muscle_pain(False)    # function called when pressed
).pack()

window.mainloop()                           # keep window running until closed 
