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
    not_tried/1,
    tried/1,
    throat_ache/1.
% TODO: probably needs more still (if it returns a permission error static
%       procedure of some sort, put it here).

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
    cough(yes),
    medication(none).

ask(additional_symptoms_cough) :-
    \+ asked(additional_symptoms_cough),
    cough(more_than_7_days).

ask(cough_severity) :-
    \+ asked(cough_severity),
    cough(yes),
    additional_symptoms(no).

ask(cough_severity) :-
    \+ asked(cough_severity),
    cough(less_than_7_days).

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

ask(using_ace_inhibitors) :-
    \+ asked(using_ace_inhibitors),
    cough(yes),
    age(older_than_6_years).

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

ask(longQT_syndrome) :-
    \+ asked(longQT_syndrome),
    blocked_nose(yes),
    \+ age(under_2_years).

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

advice('a cough suppressant') :-
    cough(mild),
    tried(soothing_syrup).

advice('soothing cough syrup') :-
    cough(yes),
    age(under_6_years).

advice('soothing cough syrup') :-
    cough(yes),
    pregnant(yes).

advice('soothing cough syrup') :-
    cough(mild).

advice('a cough suppressant') :-
    cough(severe),
    cough(dry),
    medication(no_sedative).

advice('a soothing cough syrup') :-
    cough(severe),
    cough(dry),
    medication(sedative).

advice('an expectorant cough syrup') :-
    cough(severe),
    cough(productive),
    medication(no_antibiotic),
    \+ age(under_2_years).

advice('a soothing cough syrup') :-
    cough(severe),
    cough(productive),
    medication(antibiotic).

advice('a soothing cough syrup') :-
    cough(severe),
    cough(productive),
    age(under_2_years).

%% BLOCKED NOSE
advice(physician) :-
    blocked_nose(more_than_3_weeks).

advice('a bulb syringe in combination with saline spray') :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years),
    not_tried(balloon).

advice(physician) :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years),
    tried(balloon).

advice('a salt/menthol nose spray') :-
    blocked_nose(less_than_3_weeks),
    longQT_syndrome(yes).

advice('a salt/menthol nose spray') :-
    blocked_nose(less_than_3_weeks),
    longQT_syndrome(no),
    tried(decongestant).

advice('a decongestant nose spray') :-
    blocked_nose(less_than_3_weeks),
    longQT_syndrome(no),
    medication(none).

%% THROAT ACHE
advice(physician) :-
    throat_ache(more_than_7_days).

advice(physician) :-
    additional_symptoms(yes).

advice(physician) :-
    throat_ache(more_than_3_days),
    age(under_6_years).

%% Basically "all the other cases": is there a nice way to do that?
advice('throat pastilles and paracetamol') :-
    throat_ache(less_than_3_days).

advice('throat pastilles and paracetamol') :-
    throat_ache(more_than_3_days),
    age(older_than_6_years).

% advice(none).