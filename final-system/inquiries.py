## an inquiry itself is a tuple of strings, containing:
## 0: the question itself
## 1: an explanation about why the system asks the question
## a tuple for each answer, containing the answer string and corresponding fact

inquiries = {

    # -------------GENERAL QUESTIONS---------------
    "age" :
    (
        "What is the age of the patient?",
        "Children and infants cannot take the same medications as adults.",
        (
            "0 - 3 months",
            "age(under_3_months)"
        ),
        (
            "3 months - 2 years",
            "age(under_2_years)"
        ),
        (
            "2 years - 6 years",
            "age(under_6_years)"
        ),
        (
            "Older than 6 years",
            "age(older_than_6_years)"
        ),
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

    "pregnancy" :
    (
        "Is the patient pregnant?",
        "Some medication can have an (unwanted) effect on unborn babies, so not " +
        "all medication is suitable for people who are pregnant.",
        (
            "Yes",
            "pregnant(yes)"
        ),
        (
            "No",
            "pregnant(no)"
        ),
    ),

    # -------------------COUGH--------------------
    "how_long_cough" :
    (
        "How long has the patient had the cough?",
        "If the patient has had the cough for a long time, they might have an underlying infection.",
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

    "using_ace_inhibitors" :
    (
        "Is the patient using ACE inhibitors, such as enalapril or lisinopril?",
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
            "tried(soothing_syrup)"
        ),
        (
            "No",
            "tried(none)"                   # dummy fact
        )
    ),

    "additional_symptoms_cough" :
    (
        "Is the patient also experiencing other symptoms, such as a higher temperature and general malaise?",
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

    "cough_severity" :
    (
        "How severe is the patient's cough?",
        "The severity of a cough is based on both the frequency and the intensity of the cough.",
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
        "A dry cough does not involve mucus and feels like an itch in the throat.\n" +
        "A productive cough means successfully coughing up mucus.\n" +
        "A persistent cough is when one tries to cough up mucus, but they can't.",
        (
            "Dry",
            "cough(dry)"
        ),
        (
            "Productive",
            "cough(productive)"
        ),
        (
            "Persistent",
            "cough(persistent)"
        )
    ),

    "sedative_medication" :
    (
        "Is the patient taking a medication that is a sedative?",
        "Sedative medications are those that may reduce alertness.",
        (
            "Yes",
            "medication(sedative)"
        ),
        (
            "No",
            "medication(none)"              # dummy fact
        )
    ),

    "antibiotic_medication" :
    (
        "Is the patient using antibiotics?",
        "If the patient is using antibiotics, they cannot take an expectorant cough syrup.",
        (
            "Yes",
            "medication(antibiotic)"
        ),
        (
            "No",
            "medication(none)"              # dummy fact
        )
    ),

    # ---------------BLOCKED NOSE------------------
    "how_long_blocked_nose" :
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

    "already_balloon" :
    (
        "Has the patient already tried using a bulb syringe or nasal aspirator to remedy the blocked nose?",
        "For infants, bulb syringes and nasal aspirators can be used to \"suck out\" the blockage.",
        (
            "Yes",
            "tried(balloon)"
        ),
        (
            "No",
            "tried(none)"                   # dummy fact
        )
    ),

    "breastfed" :
    (
        "Is the patient breastfed?",
        "An breastfed infant with a blocked nose cannot drink properly, so if the advised remedy is not working immediately they should see a physician.",
        (
            "Yes",
            "breastfed(yes)"
        ),
        (
            "No",
            "breastfed(no)"
        )
    ),

    "longQT_syndrome" :
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

    "already_decongestant" :
    (
        "Has the patient already tried using a decongestant nose spray?",
        None,
        (
            "Yes",
            "tried(decongestant)"
        ),
        (
            "No",
            "tried(none)"                   # dummy fact
        )
    ),

    "already_salt_spray" :
    (
        "Has the patient already tried using a saline nose spray or drops?",
        None,
        (
            "Yes",
            "tried(salt_spray)"
        ),
        (
            "No",
            "tried(none)"                   # dummy fact
        )
    ),

    # ---------------THROAT ACHE-------------------
    "how_long_throat_ache" :
    (
        "How long has the patient had the throat ache?",
        "If the patient has had the throat ache for a long time, they might have an underlying infection.",
        (
            "For more than 7 days",
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

    "additional_symptoms_throat_ache" :
    (
        "Is the patient also experiencing other symptoms, such as a fever or an ear ache?",
        "A fever may be a sign of a throat infection, and an ear ache may be the sign of an ear infection.",
        (
            "Yes",
            "additional_symptoms(yes)"
        ),
        (
            "No",
            "additional_symptoms(no)"
        )
    )
}