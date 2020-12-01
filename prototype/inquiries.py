## an inquiry is a tuple of strings, containing:
## [0] the question
## [1] answer 1
## [2] the fact that will be put in the database if answer 1 is chosen
## [3] answer 2
## [4] the fact that will be put in the database if answer 2 is chosen

cough3weeks = (
    "Have you had the cough for more than 3 weeks?",
    "Yes",
    "cough(morethan3weeks)",
    "No",
    "cough(yes)"                            # dummy fact
)

youngerthan3months = (
    "Are you under 3 months of age?",
    "Yes",
    "age(under3months)",
    "No",
    "age(over3months)"                      # dummy fact
)
