from pyswip import Prolog                   # pyswip for Prolog reasoning
from inquiries import *

pl = Prolog()
pl.consult("rules.pl")                      # load the knowledge base

starting_question = "age"

def main():
    ask_question(starting_question)

## Ask the question via the GUI
def ask_question(question):
    from interface import show_inquiry

    pl.asserta("asked({})".format(question))# the question is asked

    if question is not None:
        show_inquiry(inquiries[question])

## Add the fact in the argument to the database, and ask new question
def add_fact(fact):
    print("added fact:", fact)
    pl.asserta(fact)
    ask_question(find_next_question())

## Determine what the next question should be
def find_next_question():
    q = list(pl.query("ask(X)"))
    print(q)
    if q:
        return q[0]["X"]                    # take the first answer

    # if there are no more questions to ask
    give_advice()
    return None

## Give the advice via the GUI
def give_advice():
    advice = find_advice()
    if advice is not None:
        from interface import show_advice
        show_advice(advice)

## Make the inference, return the associated advice
def find_advice():
    q = list(pl.query("advice(X)"))
    print(q)                                # debugging purposes
    for answer in q:
        if answer["X"] != "none":
            return formulate_advice(answer["X"])
    return None

## Formulate the advice for the patient in a sentence
def formulate_advice(advice):
    if advice == "physician":
        return "The patient should go see their physician."  
    else:
        return "The patient should use " + advice + "." 

if __name__ == "__main__":
    main()
