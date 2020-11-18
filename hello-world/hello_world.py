from pyswip import Prolog                   # pyswip for Prolog reasoning 
from interface import show_message
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

    show_message(give_advice())
