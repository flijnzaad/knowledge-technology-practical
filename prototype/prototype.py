from pyswip import Prolog                   # pyswip for Prolog reasoning
from inquiries import *

pl = Prolog()
pl.consult("rules.pl")                      # load the knowledge base

def main():
    ask_question(inquiries["younger_than_3_months"])     # starting inquiry

## Ask the question via the GUI
def ask_question(inquiry):
    from interface import show_question

    if inquiry is not None:
        show_question(inquiry)

## Add the fact in arg to the database, and ask new question
def add_fact(fact):
    pl.asserta(fact)
    ask_question(find_next_question())

## Determine what the next question should be
## and remove question from KB so you don't ask it again
def find_next_question():
    q = list(pl.query("ask(X)"))
    if q:
        answer = q[0]["X"]                      # take the first answer 
        # TODO: is this the right location in the code for this?
        pl.asserta("asked({})".format(answer))
        print(answer)                       # for debugging 
        return inquiries[answer]

    # if there are no more questions to ask
    give_advice()
    # TODO: this doesn't work!

## Give the advice via the GUI
def give_advice():
    from interface import show_advice
    advice = find_advice()
    show_advice(advice)

## Make the inference, return the associated advice
def find_advice():
    q = list(pl.query("advice(X)"))
    if q:
        print(q)
        for answer in q:
            if answer["X"] != "none":
                break
        if answer["X"] == "physician":
            return "You should go see your physician."
        else:
            return "You should take {}.".format(answer)

    return None

if __name__ == "__main__":
    main()
