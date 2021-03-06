from pyswip import Prolog                   # pyswip for Prolog reasoning

pl = Prolog()
pl.consult("rules.pl")                      # load the knowledge base

starting_question = "age"
starting_message = ("Welcome to Pharmacy Help!\n\nThis system will provide pharmaceutical advice for people with symptoms of the " +
                    "common cold, namely coughing, a blocked nose and a throat ache. It represents the knowledge of our expert, " +
                    "pharmacist Catrien Oom.")

def main():
    from interface import start
    start(starting_message, starting_question)

## Ask the question via the GUI
def ask_question(question):
    if question is not None:
        pl.asserta("asked({})".format(question))
        from interface import show_inquiry
        from inquiries import inquiries
        show_inquiry(inquiries[question])

## Add the fact in the argument to the database, and ask new question
def add_fact(fact):
    print("added fact:", fact)              # debugging purposes
    pl.asserta(fact)
    ask_question(find_next_question())

## Determine what the next question should be
def find_next_question():
    q = list(pl.query("ask(X)"))
    print(q)                                # debugging purposes 
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
    recommendation = find_recommendation()
    additions = find_additions()
    advice = (recommendation, additions)
    return advice

## Infer recommendation
def find_recommendation():
    q = list(pl.query("recommendation(X)"))
    # print(q)                                # debugging purposes
    for answer in q:
        if answer["X"] != "none":
            r = answer["X"]
            from advice import recommendations
            return recommendations[r]
    return None

## Infer additions
def find_additions():
    q = list(pl.query("addition(X)"))
    # print(q)                                # debugging purposes 
    full_addition = ""
    for answer in q:
        if answer["X"] != "none":
            a = answer["X"]
            from advice import additions
            full_addition += additions[a]
    return full_addition

if __name__ == "__main__":
    main()
