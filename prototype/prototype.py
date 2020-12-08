from pyswip import Prolog                   # pyswip for Prolog reasoning
from inquiries import *

pl = Prolog()
pl.consult("rules.pl")                      # load the knowledge base

starting_question = "younger_than_3_months"

def main():
    ask_question(starting_question)         # starting inquiry

## Ask the question via the GUI
def ask_question(question):
    from interface import show_question

    pl.asserta("asked({})".format(question))# the question is asked 

    if question is not None:
        show_question(inquiries[question])

## Add the fact in the argument to the database, and ask new question
def add_fact(fact):
    print("added fact:", fact)
    pl.asserta(fact)
    ask_question(find_next_question())

## Determine what the next question should be
def find_next_question():
    q = list(pl.query("ask(X)"))
    if q:
        return q[0]["X"]                    # take the first answer 

    # if there are no more questions to ask
    give_advice()

## Give the advice via the GUI
def give_advice():
    from interface import show_advice
    advice = find_advice()
    show_advice(advice)

## Make the inference, return the associated advice
def find_advice():
    q = list(pl.query("advice(X)"))
    if q:
        print(q)                            # debugging purposes 
        # TODO: this was to avoid the advice "You should take a none.", caused
        # by the dummy fact advice(none). This could probably be less ugly
        for answer in q:
            if answer["X"] != "none":
                break
        if answer["X"] == "physician":
            return "You should go see your physician."
        else:
            return "You should take {}.".format(answer["X"])

    return None

if __name__ == "__main__":
    main()
