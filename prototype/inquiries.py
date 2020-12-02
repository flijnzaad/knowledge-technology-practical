## an inquiry is a tuple of strings, containing:
## [0] the question
## [1] answer 1
## [2] the fact that will be put in the database if answer 1 is chosen
## [3] answer 2
## [4] the fact that will be put in the database if answer 2 is chosen

cough_3_weeks = (
    "Have you had the cough for more than 3 weeks?",
    "Yes",
    "cough(morethan3weeks)",
    "No",
    "cough(yes)"                            # dummy fact
)

younger_than_3_months = (
    "Are you under 3 months of age?",
    "Yes",
    "age(under3months)",
    "No",
    "age(over3months)"                      # dummy fact
)

using_ace_inhibitors = (
    "Are you using ace inhibitors?",
    "Yes",
    "medication(ace_inhibitors)",
    "No",
    ""                                      # dummy fact is already present 
    # don't know whether pyswip accepts this
)

# TODO: this has a very similar setup to the previous one; is there a way to
# generalize this?
already_soothing = (                                                  
    "Are you already using soothing cough syrup against your cough?",
    "Yes",
    "medication(soothing_syrup)",
    "No",
    ""
)
