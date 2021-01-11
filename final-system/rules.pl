%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added using asserta/1.
:- dynamic 
    additional_symptoms/1, 
    advice/1,
    age/1,
    asked/1,
    blocked_nose/1,
    breastfed/1,
    cough/1,
    longQT_syndrome/1,
    medication/1,
    pregnant/1,
    take_medication/1,
    take_decongestant/1,
    tried/1,
    throat_ache/1.

%% Dummy facts to 'introduce' the predicates to the knowledge base
additional_symptoms(unknown).
medication(unknown).
pregnant(unknown).
longQT_syndrome(unknown).

%% Commonly known facts about age.
age(under_6_years) :-
    age(under_2_years).

age(under_2_years) :-
    age(under_3_months).

% Ask the first question (after age question).
ask(pregnancy) :-
    \+ asked(pregnancy),
    age(older_than_6_years).

% Standard second question.
ask(which_symptom) :-
    \+ asked(which_symptom).

% Standard third question.
ask(covid) :-
    \+ asked(covid).

%% ----------------------------------------------------
%%       Rules that infer which questions to ask          
%% ----------------------------------------------------

%% COUGHING
ask(how_long_cough) :-
    \+ asked(how_long_cough),
    cough(yes),
    \+ age(under_3_months).

ask(additional_symptoms_cough) :-
    \+ asked(additional_symptoms_cough),
    cough(more_than_7_days).

ask(cough_severity) :-
    \+ asked(cough_severity),
    cough(yes),
    \+ age(under_6_years),
    pregnant(no).

ask(already_soothing) :-
    \+ asked(already_soothing),
    cough(mild).

ask(cough_kind) :- 
    \+ asked(cough_kind),
    cough(mild),
    tried(soothing_syrup).

ask(cough_kind) :-
    \+ asked(cough_kind),
    cough(severe).

ask(sedative_medication) :-
    \+ asked(sedative_medication),
    cough(dry).

ask(antibiotic_medication) :-
    \+ asked(antibiotic_medication),
    cough(persistent).

%% BLOCKED NOSE
ask(how_long_blocked_nose) :-
    \+ asked(how_long_blocked_nose),
    blocked_nose(yes).

ask(breastfed) :-
    \+ asked(breastfed),
    blocked_nose(less_than_3_weeks),
    age(under_2_years).

ask(already_salt_spray) :-
    \+ asked(already_salt_spray),
    blocked_nose(less_than_3_weeks),
    \+ age(under_2_years),
    age(under_6_years).

ask(longQT_syndrome) :-
    \+ asked(longQT_syndrome),
    blocked_nose(yes),
    \+ age(under_6_years),
    pregnant(no).

%% THROAT ACHE
ask(how_long_throat_ache) :-
    \+ asked(how_long_throat_ache),
    throat_ache(yes).

ask(additional_symptoms_throat_ache) :-
    \+ asked(additional_symptoms_throat_ache),
    throat_ache(less_than_7_days).

%% ----------------------------------------------------
%%           Rules for inference of advice
%% ----------------------------------------------------
%% COUGHING
advice(physician_infection) :-
    cough(more_than_3_weeks).

advice(physician_infection) :-
    cough(yes),
    age(under_3_months).

advice(physician_infection) :-
    cough(more_than_7_days),
    additional_symptoms(yes).

advice(physician_ace) :-
    cough(yes),
    medication(ace_inhibitors).

advice(soothing_syrup) :-
    cough(less_than_3_weeks),
    \+ age(under_3_months),
    age(under_6_years).

advice(soothing_syrup) :-
    cough(yes),
    pregnant(yes).

advice(soothing_syrup) :-
    cough(mild),
    \+ tried(soothing_syrup).

advice(soothing_syrup) :-
    cough(dry),
    medication(sedative).

advice(suppressant_syrup) :-
    cough(dry),
    \+ medication(sedative).

advice(expectorant_syrup) :-
    cough(persistent),
    \+ medication(antibiotic),
    \+ age(under_2_years).

advice(soothing_syrup) :-
    cough(persistent),
    medication(antibiotic).

advice(soothing_syrup) :-
    cough(persistent),
    age(under_2_years).

advice(soothing_syrup) :-
    cough(productive),
    \+ tried(soothing_syrup).

%% BLOCKED NOSE
advice(physician_infection) :-
    blocked_nose(more_than_3_weeks).

advice(bulb_syringe) :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years),
    \+ tried(balloon).

advice(salt_menthol_spray) :-
    blocked_nose(less_than_3_weeks),
    \+ age(under_2_years),
    age(under_6_years),
    \+ tried(salt_spray).

advice(salt_menthol_spray) :-
    blocked_nose(less_than_3_weeks),
    longQT_syndrome(yes).

advice(salt_menthol_spray) :-
    blocked_nose(less_than_3_weeks),
    pregnant(yes),
    \+ tried(salt_spray).

advice(salt_menthol_spray) :-
    blocked_nose(less_than_3_weeks),
    tried(decongestant_spray).
    
advice(decongestant_spray) :-
    blocked_nose(less_than_3_weeks),
    longQT_syndrome(no),
    pregnant(no),
    \+ age(under_2_years),
    \+ tried(decongestant_spray).

advice(decongestant_spray) :-
    blocked_nose(less_than_3_weeks),
    \+ age(under_2_years),
    age(under_6_years),
    tried(salt_spray).

%% THROAT ACHE
advice(physician_infection) :-
    throat_ache(more_than_7_days).

advice(physician_infection) :-
    throat_ache(yes),
    additional_symptoms(yes).

advice(physician_infection) :-
    throat_ache(more_than_3_days),
    age(under_6_years).

advice(paracetamol) :-
    throat_ache(less_than_3_days).

advice(paracetamol) :-
    throat_ache(more_than_3_days),
    age(older_than_6_years).

%% ----------------------------------------------------
%%          Rules for additions to advice
%% ----------------------------------------------------
take_medication(yes) :-                     % fact to make these additions easier
    advice(X),
    \+ X = physician_infection,
    \+ X = physician_ace.

take_decongestant(no) :-
    advice(X),
    \+ X = decongestant_spray.

addition(medical_insert) :-
    take_medication(yes).

addition(breastfed) :-
    breastfed(yes),
    take_medication(yes).

addition(if_tried_already) :-
    take_medication(yes),
    take_decongestant(no),                  % the advice for decongestant already includes "if tried already"    
    \+ breastfed(yes).                      % the advice for breastfed already includes "go to physician"

addition(tips_coughing) :-
    cough(yes),
    take_medication(yes).

addition(tips_blocked_nose) :-
    blocked_nose(yes),
    take_medication(yes).

addition(tips_throat_ache) :-
    throat_ache(yes),
    take_medication(yes).

addition(covid_positive_physician) :-
    covid(positive),
    \+ take_medication(yes).

addition(covid_positive_medication) :-
    covid(positive),
    take_medication(yes).

addition(covid_test_physician) :-
    covid(test),
    \+ take_medication(yes).

addition(covid_test_medication) :-
    covid(test),
    take_medication(yes).

addition(covid_quarantine) :-
    \+ covid(negative).