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
    print("added fact:", fact)              # debugging purposes
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
    advice = formulate_advice()
    if advice is not None:
        from interface import show_advice
        show_advice(advice)

## Returns advice with additions 
def formulate_advice():
    advice = find_advice()
    additions = find_additions()
    full_advice = (advice, additions)
    return full_advice

## Infer advice
def find_advice():
    q = list(pl.query("advice(X)"))
    print(q)                                # debugging purposes
    for answer in q:
        if answer["X"] != "none":
            advice = answer["X"]
            from advice import medications
            return medications[advice]
    return None

## Infer additions to the advice
def find_additions():
    q = list(pl.query("addition(X)"))
    print(q)
    full_additions = ""
    for answer in q:
        if answer["X"] != "none":
            new_addition = answer["X"]
            from advice import additions
            full_additions += additions[new_addition]
    return full_additions

if __name__ == "__main__":
    main()
