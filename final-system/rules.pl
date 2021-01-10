%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added using asserta/1.
:- dynamic 
    additional_symptoms/1, 
    advice/1,
    age/1,
    asked/1,
    blocked_nose/1,
    cough/1,
    longQT_syndrome/1,
    medication/1,
    pregnant/1,
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

%% ----------------------------------------------------
%%       Rules that infer which questions to ask          
%% ----------------------------------------------------

%% COUGHING
ask(how_long_cough) :-
    \+ asked(how_long_cough),
    cough(yes).

ask(additional_symptoms_cough) :-
    \+ asked(additional_symptoms_cough),
    cough(more_than_7_days).

ask(cough_severity) :-
    \+ asked(cough_severity),
    cough(yes),
    additional_symptoms(no),
    \+ age(under_6_years),
    pregnant(no).

ask(already_soothing) :-
    \+ asked(already_soothing),
    cough(yes),
    pregnant(yes).

ask(already_soothing) :-
    \+ asked(already_soothing),
    cough(yes),
    age(under_6_years).

ask(already_soothing) :-
    \+ asked(already_soothing),
    cough(mild).

ask(cough_kind) :-
    \+ asked(cough_kind),
    cough(severe).

ask(sedative_medication) :-
    \+ asked(sedative_medication),
    cough(dry).

ask(antibiotic_medication) :-
    \+ asked(antibiotic_medication),
    cough(productive).

%% BLOCKED NOSE
ask(how_long_blocked_nose) :-
    \+ asked(how_long_blocked_nose),
    blocked_nose(yes).

ask(already_balloon) :-
    \+ asked(already_balloon),
    blocked_nose(less_than_3_weeks),
    age(under_2_years).

ask(already_salt_spray) :-
    \+ asked(already_salt_spray),
    blocked_nose(yes),
    \+ age(under_2_years),
    age(under_6_years).

ask(already_salt_spray) :-
    \+ asked(already_salt_spray),
    blocked_nose(yes),
    pregnant(yes).

ask(longQT_syndrome) :-
    \+ asked(longQT_syndrome),
    blocked_nose(yes),
    \+ age(under_6_years),
    pregnant(no).

ask(already_decongestant) :-
    \+ asked(tried_decongestant),
    blocked_nose(yes),
    longQT_syndrome(no).

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
advice(physician) :-
    cough(more_than_3_weeks).

advice(physician) :-
    cough(yes),
    age(under_3_months).

advice(physician) :-
    cough(more_than_7_days),
    additional_symptoms(yes).

advice(physician) :-
    cough(yes),
    medication(ace_inhibitors).

advice('soothing cough syrup') :-
    cough(yes),
    age(under_6_years),
    \+ tried(soothing_syrup).

advice('soothing cough syrup') :-
    cough(yes),
    pregnant(yes),
    \+ tried(soothing_syrup).

advice('wait or physician') :-
    cough(yes),
    age(under_6_years),
    tried(soothing_syrup).

advice('wait or physician') :-
    cough(yes),
    pregnant(yes),
    tried(soothing_syrup).

advice('soothing cough syrup') :-
    cough(mild),
    \+ tried(soothing_syrup).

advice('soothing cough syrup') :-
    cough(severe),
    cough(dry),
    medication(sedative).

advice('cough suppressant') :-
    cough(severe),
    cough(dry),
    \+ medication(sedative).

advice('expectorant cough syrup') :-
    cough(severe),
    cough(persistent),
    \+ medication(antibiotic),
    \+ age(under_2_years).

advice('soothing cough syrup') :-
    cough(severe),
    cough(persistent),
    medication(antibiotic).

advice('soothing cough syrup') :-
    cough(severe),
    cough(persistent),
    age(under_2_years).

advice('soothing cough syrup') :-
    cough(severe),
    cough(productive),
    \+ tried(soothing_syrup).

advice('wait or physician') :-
    cough(severe),
    cough(productive),
    tried(soothing_syrup).

%% BLOCKED NOSE
advice(physician) :-
    blocked_nose(more_than_3_weeks).

advice('a bulb syringe in combination with saline spray') :-
    blocked_nose(yes),
    age(under_2_years),
    \+ tried(balloon).

advice(physician) :-
    blocked_nose(yes),
    age(under_2_years),
    tried(balloon).

advice('salt (with menthol) nose spray') :-
    blocked_nose(yes),
    \+ age(under_2_years),
    age(under_6_years),
    \+ tried(salt_spray).

advice('salt (with menthol) nose spray') :-
    blocked_nose(yes),
    longQT_syndrome(yes).

advice('salt (with menthol) nose spray') :-
    blocked_nose(yes),
    tried(decongestant).

advice('salt (with menthol) nose spray') :-
    blocked_nose(yes),
    pregnant(yes),
    \+ tried(salt_spray).
    
advice('decongestant nose spray') :-
    blocked_nose(yes),
    longQT_syndrome(no),
    pregnant(no),
    \+ age(under_2_years),
    \+ tried(decongestant).

advice('decongestant nose spray') :-
    blocked_nose(yes),
    \+ age(under_2_years),
    age(under_6_years),
    tried(salt_spray).

advice('wait or physician') :-
    blocked_nose(yes),
    pregnant(yes),
    tried(salt_spray).

%% THROAT ACHE
advice(physician) :-
    throat_ache(more_than_7_days).

advice(physician) :-
    throat_ache(yes),
    additional_symptoms(yes).

advice(physician) :-
    throat_ache(more_than_3_days),
    age(under_6_years).

advice(paracetamol) :-
    throat_ache(less_than_3_days).

advice(paracetamol) :-
    throat_ache(more_than_3_days),
    age(older_than_6_years).