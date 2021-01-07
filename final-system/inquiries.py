## an inquiry itself is a tuple of strings, containing:
## 0: the question itself
## 1: an explanation about why the system asks the question
## a tuple for each answer, containing the answer string and corresponding fact

inquiries = {

    # -------------GENERAL QUESTIONS---------------
    "age" :
    (
        "Please enter the age of the patient.\n" + 
        "For patients 12 months or older,\n" +
        "please round down to the nearest year.", # TODO: okay?
        "EXPLANATION"
    ),

    "which_symptom" :
    (
        "Which symptom is the patient experiencing?",
        None,
        (
            "Coughing",
            "cough(yes)"
        ),
        (
            "Blocked nose",
            "blocked_nose(yes)"
        ),
        (
            "Throat ache",
            "throat_ache(yes)"
        )
    ),

    "tested_covid19" :
    (
        "Has the patient been tested for COVID-19?",
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
            "No, they have not been tested.",
            "covid(no_test)"
        ),
        (
            "No, but they have a test scheduled",      # needed?
            "covid(test_scheduled)"
        )
    ),

    # -------------------COUGH--------------------
    "how_long_cough" :
    (
        "How long has the patient had the cough?",
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

    "using_ace_inhibitors" :
    (
        "Is the patient using ACE inhibitors, such as ...? (give examples)",
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
        "Has the patient already tried using soothing cough syrup against their cough?",
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

    "additional_symptoms" :
    (
        "Does the patient also experience other symptoms, such as higher temperature and general malaise?",
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

    "is_pregnant" :
    (
        "Is the patient pregnant?",
        "Some medication can have an (unwanted) effect on unborn babies, so not " +
        "all medication is suitable for people who are pregnant.",
        (
            "Yes",
            "patient(is_pregnant)"
        ),
        (
            "No",
            "patient(is_not_pregnant)"
        ),
        (
            "Maybe",
            "patient(need_pregnancy_test)"
        )
    ),

    "cough_severity" :
    (
        "How severe is the patient's cough?",
        "EXPLANATION",
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
        "What kind of cough does the patient have?",
        "A productive cough involves mucus, whereas a dry cough does not.",
        (
            "Productive",
            "cough(productive)"
        ),
        (
            "Dry",
            "cough(dry)"
        )
    ),

    "sedative_medication" :
    (
        "Is the patient taking a medication that is a sedative?",
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
        "Are the patient using antibiotics?",
        "If the patient are using antibiotics, you cannot take an expectorant cough" +
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

    # ---------------BLOCKED NOSE------------------
    "how_long_blocked_nose":
    (
        "How long has the patient had the blocked nose?",
        "If the patient has had the blocked nose for a long time, they might have a sinus infection.",
        (
            "For more than 3 weeks",
            "blocked_nose(more_than_3_weeks)"
        ),
        (
            "For less than 3 weeks",
            "blocked_nose(less_than_3_weeks)"
        )
    ),

    "already_balloon":
    (
        "Has the patient already tried using a balloon to remedy the blocked nose?",
        "EXPLANATION about the balloon",
        (
            "Yes",
            "medication(balloon)"
        ),
        (
            "No",
            "medication(none)"
        )
    ),

    "longQT_syndrome":
    (
        "Does the patient have Long QT Syndrome (a heart rhythm condition?)",
        "Individuals with this syndrome cannot take a decongestant nose spray.",
        (
            "Yes",
            "longQT_syndrome(yes)"
        ),
        (
            "No",
            "longQT_syndrome(no)"
        )
    ),

    "already_decongestant":
    (
        "Has the patient already tried using a decongestant nose spray?",
        None,
        (
            "Yes",
            "medication(decongestant)"
        ),
        (
            "No",
            "medication(none)"
        )
    ),


    # ---------------THROAT ACHE-------------------
    "how_long_throat_ache":
    (
        "How long has the patient had the throat ache?",
        "EXPLANATION",
        (
            "For more than a week",
            "throat_ache(more_than_7_days)"
        ),
        (
            "Between 3 and 7 days",
            "throat_ache(more_than_3_days)"
        ),
        (
            "For less than 3 days",
            "throat_ache(less_than_3_days)"
        )
    ),

    "fever":
    (
        "Does the patient have a temperature above 38.5 degrees Celsius?",
        "A throat ache combined with a fever may be a sign of an infection.",
        (
            "Yes",
            "fever(yes)"
        ),
        (
            "No",
            "fever(no)"
        )
    )
}
