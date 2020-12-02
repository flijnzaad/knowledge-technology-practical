from pyswip import Prolog                   # pyswip for Prolog reasoning
from inquiries import *

pl = Prolog()
pl.consult("rules.pl")                      # load the knowledge base

def main():
    ask_question(cough3weeks)               # starting inquiry

## Ask the question via the GUI
def ask_question(inquiry):
    from interface import show_question
    show_question(inquiry)

## Adds the fact in arg to the database, and asks new question
def add_fact(fact):
    pl.asserta(fact)
    ask_question(find_next_question())

## Determines what the next question should be
def find_next_question():
    cough = list(pl.query("cough(yes)"))
    if cough:                               # this is going wrong
        return youngerthan3months

    # if there are no more questions to ask
    give_advice()

## Gives the advice via the GUI
def give_advice():
    from interface import show_advice
    advice = find_advice()
    show_advice(advice)

## Makes the inference, returns the associated advice
def find_advice():
    q = list(pl.query("go(X)"))             # "Should I go see someone?"
    if q:
        return "You should go see a " + q[0]["X"] + '.'

    q = list(pl.query("take(X)"))           # "Should I take any medication?"
    if q:
        return "You should take " + q[0]["X"] + '.'

    return None

if __name__ == "__main__":
    main()
