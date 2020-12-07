## an inquiry is a tuple of strings, containing:
## [0] the question
## [1] answer 1
## [2] the fact that will be put in the database if answer 1 is chosen
## [3] answer 2
## [4] the fact that will be put in the database if answer 2 is chosen
## etc.

how_long_cough = (
    "How long have you had the cough?",
    "For more than 3 weeks",
    "cough(more_than_3_weeks)",
    "For more than 7 days",
    "cough(more_than_7_days)",
    "For less than 7 days",
    "cough(less_than_7_days)"
)
# TODO: does asserta/1 also add the fact if it's already there?

younger_than_3_months = (
    "Are you under 3 months of age?",
    "Yes",
    "age(under_3_months)",
    "No",
    "age(over_3_months)"
)

using_ace_inhibitors = (
    "Are you using ace inhibitors?",
    "Yes",
    "medication(ace_inhibitors)",
    "No",
    "medication(none)"
)

# TODO: this has a very similar setup to the previous one; is there a way to
# generalize this?
already_soothing = (
    "Are you already using soothing cough syrup against your cough?",
    "Yes",
    "medication(soothing_syrup)",
    "No",
    "medication(none)"
    # TODO: should it be more specific than medication(none)?
)

experiencing_symptoms = (
    "What symptoms are you experiencing?",
    "Coughing",
    "cough(yes)",
    "Blocked nose",
    "blocked_nose(yes)",                    # dummy fact
    "Throat ache",
    "throat_ache(yes)"                      # dummy fact
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

#  symptom_length = (
    #  "How long have you been having these symptoms?",
    #  "More than 3 weeks",
    #  "symptomlen(len_more3week)",
    #  "More than 1 week",
    #  "symptomlen(len_more1week)",
    #  "less than 1 week",
    #  "symptomlen(len_less1week)"
#  )

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
    "Yes, it came back positive",
    "covid(positive)",
    "Yes, it came back negative",
    "covid(negative)",
    "No",
    "covid(no_test)",
    "No, but I have a test scheduled",      # needed? 
    "covid(test_scheduled)"
)
