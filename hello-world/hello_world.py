from pyswip import Prolog                   # pyswip for Prolog reasoning 
import tkinter as tk                        # tkinter for using GUI 
pl = Prolog()
pl.consult("hello_world.pl")                # load the knowledge base 

                                            # some GUI stuff 
window = tk.Tk()
question = tk.Label(
    text = "Do you have muscle pain?",
    fg = "white",
    bg = "black",
    width = 25,
    height = 3
)
question.pack()

def muscle_pain(pain=True):
    if pain:
        pl.asserta("pain(muscle)")          # add fact to KB 
    else:
        pl.asserta("pain(none)")            # add dummy fact to KB  
    window.destroy()

yes = tk.Button(                            # yes button 
    text    = "Yes",
    width   = 20,
    height  = 3,
    command = lambda: muscle_pain(True)     # callback function: pain=true 
)
yes.pack()

no = tk.Button(                             # no button 
    text    = "No",
    width   = 20,
    height  = 3,
    command = lambda: muscle_pain(False)    # callback function: pain=false 
)
no.pack()

window.mainloop()

q = pl.query("take(X)")                     # "Should I take any medication?"  

print(list(q))

# fix bug here
if q:                                 
    print("You should take", list(q)[0]["X"])
else:                                       # query is empty so no medication 
    print("You're healthy, you don't need any medication.")
