from pyswip import Prolog                   # pyswip for Prolog reasoning

pl = Prolog()
pl.consult("rules.pl")                      # load the knowledge base

def main():
    ask_questions()

def ask_questions():
    from interface import show_question
    show_question(
        "Have you had the cough for more than 3 weeks?",
        "Yes",
        "cough(morethan3weeks)",
        "No",
        "cough(yes)"
    )

def add_fact(fact):
    pl.asserta(fact)
    from interface import show_advice
    show_advice(give_advice())

def give_advice():
    q = list(pl.query("go(X)"))

    if q:
        return "Go to the " + q[0]["X"] + "."
    else:
        return "None generated yet."

if __name__ == "__main__":
    main()
