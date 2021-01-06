## an inquiry itself is a tuple of strings, containing:
## 0: the question itself
## 1: an explanation about why the system asks the question
## a tuple for each answer, containing the answer string and corresponding fact

inquiries = {

    "how_long_cough" :
    (
        "How long have you had the cough?",
        "EXPLANATION",
        (
            "For more than 3 weeks",
            "cough(more_than_3_weeks)"
        ),
        (
            "For more than 7 days",
            "cough(more_than_7_days)"
        ),
        (
            "For less than 7 days",
            "cough(less_than_7_days)"
        )
    ),
    # TODO: does asserta/1 also add the fact if it's already there?

    "younger_than_3_months" :
    (
        "Are you under 3 months of age?",
        "For infants under 3 months, coughing can be a symptom of a life-" +
        "threatening disease.",
        (
            "Yes",
            "age(under_3_months)"
        ),
        (
            "No",
            "age(over_3_months)"
        )
    ),

    "using_ace_inhibitors" :
    (
        "Are you using ACE inhibitors, such as ...? (give examples)",
        "Coughing can be a side effect of this group of medications.",
        (
            "Yes",
            "medication(ace_inhibitors)"
        ),
        (
            "No",
            "medication(none)"
        )
    ),

    # TODO: this has a very similar setup to the previous one; is there a way to
    # generalize this?
    "already_soothing" :
    (
        "Are you already using soothing cough syrup against your cough?",
        None,
        (
            "Yes",
            "medication(soothing_syrup)"
        ),
        (
            "No",
            "medication(none)"
        )
        # TODO: should it be more specific than medication(none)?
    ),

    "experiencing_symptoms" :
    (
        "What symptoms are you experiencing?",
        None,
        (
            "Coughing",
            "cough(yes)"
        ),
        (
            "Blocked nose",
            "blocked_nose(yes)"
        ),                    # dummy fact
        (
            "Throat ache",
            "throat_ache(yes)"                      # dummy fact
        )
    ),

    "additional_symptoms" :
    (
        "Do you also experience other symptoms, such as higher temperature and general malaise?",
        "Additional symptoms may be a sign of an infection.",
        (
            "Yes",
            "additional_symptoms(yes)"
        ),
        (
            "No",
            "additional_symptoms(no)"
        )
    ),

    #  symptom_length =
    #  (
        #  "How long have you been having these symptoms?",
        #  "More than 3 weeks",
        #  "symptomlen(len_more3week)",
        #  "More than 1 week",
        #  "symptomlen(len_more1week)",
        #  "less than 1 week",
        #  "symptomlen(len_less1week)"
    #  )

    "is_pregnant" :
    (
        "Are you pregnant?",
        "Some medication can have an (unwanted) effect on unborn babies, so not " +
        "all medication is suitable for people who are pregnant.",
        (
            "Yes",
            "patient(is_pregnant)"
        ),
        (
            "No",
            "patient(is_notpregnant)"
        ),
        (
            "Maybe",
            "patient(need_pregnancytest)"
        )
    ),

    "younger_than_6_years" :
    (
        "Are you under 6 years old?",
        "Not all medication is suitable for children.",
        (
            "Yes",
            "age(under6yearss)"
        ),
        (
            "No",
            "age(over6years)"
        )
    ),

    "cough_severity" :
    (
        "How severe is your cough?",
        None,
        (
            "Mild",
            "cough(mild)"
        ),
        (
            "Severe",
            "cough(severe)"
        )
    ),

    "cough_kind" :
    (
        "What kind of cough do you have?",
        "A productive cough involves mucus, whereas a dry cough does not.",
        (
            "Dry",
            "cough(dry)"
        ),
        (
            "Productive",
            "cough(productive)"
        )
    ),

    "sedative_medication" :
    (
        "Are you taking a medication that is a sedative?",
        "A sedative medication has \"Kan het reactievermogen verminderen\"" +
        " on the box.",
        (
            "Yes",
            "medication(sedative)"
        ),
        (
            "No",
            "medication(no_sedative)"
        )
    ),

    "antibiotic_medication" :
    (
        "Are you using antibiotics?",
        "If you are using antibiotics, you cannot take an expectorant cough" +
        " syrup.",
        (
            "Yes",
            "medication(antibiotic)"
        ),
        (
            "No",
            "medication(no_antibiotic)"
        )
    ),

    # TODO: asking for age should be more elegant
    "younger_than_2_years" :
    (
        "Are you under 2 years old?",
        "Children under 2 years of age cannot take an expectorant cough syrup.",
        (
            "Yes",
            "age(under_2_years)"
        ),
        (
            "No",
            "age(over_2_years)"
        )
    ),

    "tested_covid19" :
    (
        "Have you tested for COVID-19?",
        None,
        (
            "Yes, the test came back positive",
            "covid(positive)"
        ),
        (
            "Yes, the test came back negative",
            "covid(negative)"
        ),
        (
            "No, I have not been tested for these symptoms",
            "covid(no_test)"
        ),
        (
            "No, but I have a test scheduled",      # needed?
            "covid(test_scheduled)"
        )
    )
}
