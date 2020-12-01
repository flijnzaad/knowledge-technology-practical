from pyswip import Prolog                   # pyswip for Prolog reasoning
from inquiries import *

pl = Prolog()
pl.consult("rules.pl")                      # load the knowledge base


def main():
    ask_question(cough3weeks)               # starting inquiry


def ask_question(inquiry):
    from interface import show_question
    show_question(inquiry)


def add_fact(fact):
    pl.asserta(fact)
    ask_question(find_next_question())


def find_next_question():
    # what to do?
    return next_question


def find_advice():
    q = list(pl.query("go(X)"))             # "Should I go see someone?"
    if q:
        return "You should go see a " + q[0]["X"] + '.'

    q = list(pl.query("take(X)"))           # "Should I take any medication?"
    if q:
        return "You should take " + q[0]["X"] + '.'

    return None


def give_advice():
    from interface import show_advice
    advice = find_advice()
    if advice is not None:
        show_advice(advice)


if __name__ == "__main__":
    main()
