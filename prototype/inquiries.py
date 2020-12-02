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

experiencing_symptoms = (
    "What symptoms are you expieriencing?",
    "Coughing",
    "patient(has_cough)",
    "Blocked nose",
    "patient(has_blockednose)",                      # dummy fact
    "Throat ache",
    "patient(has_throatache)"                     # dummy fact
)

additional_symptoms = (
    "Do you also have other symptoms, such as vomiting or nausea for more than 7 days?",
    "Yes I am experiencing nausea",
    "patientadd(is_nauseated)",
    "Yes I am experiencing vomiting",
    "patientadd(is_vomiting)",
    "Yes I am experiencing both",
    "patientadd(is_all)",
    "No I am experiencing neither",
    "patientadd(is_none)"

)

symptom_length = (
    "How long have you been having these symptoms?",
    "More than 3 weeks",
    "symptomlen(len_more3week)",
    "More than 1 week",
    "symptomlen(len_more1week)",
    "less than 1 week",
    "symptomlen(len_less1week)"

)

is_pregnant = (
    "Are you pregnant?",
    "Yes",
    "patient(is_pregnant)",
    "No",
    "patient(is_notpregnant)",
    "Maybe",
    "Patient(need_pregnancytest)"

)

younger_than_6_years = (
    "Are you under 6 years old?",
    "Yes",
    "age(under6yearss)",
    "No",
    "age(over6years)"
)

cough_severity = (
    "How severe is your cough?",
    "Mild",
    "patient(cough_mild)",
    "Severe",
    "patient(cough_severe)"
)

cough_kind = (
    "What kind of cough do you have?",
    "Dry",
    "patient(cough_dry)",
    "productive",
    "patient(cough_productive)"
)

sedative_medication = (
    "Are you taking a medication that is a sedative?",
    "Yes",
    "medication(sedative)",
    "No",
    "medication(no_sedative)"
)



antibiotic_medication = (
    "Are you using antibiotics?",
    "Yes",
    "medication(antibiotic)",
    "No",
    "medication(no_antibiotic)"
)



younger_than_2_years = (
    "Are you under 2 years old?",
    "Yes",
    "age(under2years)",
    "No",
    "age(over2years)"
)

tested_covid19 = (
    "Have you tested for COVID-19?",
    "Yes",
    "covid(test_positive)",
    "No",
    "covid(test_negative)",
    "No but I have a test scheduled",
    "covid(test_scheduled)"

)