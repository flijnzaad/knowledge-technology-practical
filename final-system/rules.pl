%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added using asserta/1.
:- dynamic 
    additional_symptoms/1, 
    advice/1,
    age/1,
    asked/1,
    breastfed/1,
    blocked_nose/1,
    cough/1,
    fever/1,
    longQT_syndrome/1,
    medication/1,
    throat_ache/1.
% TODO: probably needs more still (if it returns a permission error static
%       procedure of some sort, put it here).

%% Dummy facts to 'introduce' the predicates to the knowledge base
additional_symptoms(unknown).
medication(unknown).
pregnant(unknown).
longQT_syndrome(unknown).
temperature(unknown).
only_pain(yes).
fever(unknown).

%% Commonly known facts about age.
age(under_6_years) :-
    age(under_2_years).

age(under_2_years) :-
    age(under_1_year).

age(under_1_year) :-
    age(under_3_months).

%% ----------------------------------------------------
%%       Rules that infer which questions to ask          
%% ----------------------------------------------------

% asked(none).
%% COUGHING

ask(using_ace_inhibitors) :-
    \+ asked(using_ace_inhibitors),
    cough(yes),
    \+ age(under_3_months).

ask(how_long_cough) :-
    \+ asked(how_long_cough),
    cough(yes),
    medication(none).

ask(additional_symptoms) :-
    \+ asked(additional_symptoms),
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

%% BLOCKED NOSE
ask(how_long_blocked_nose) :-
    \+ asked(how_long_blocked_nose),
    blocked_nose(yes).

ask(already_balloon) :-
    \+ asked(already_balloon),
    blocked_nose(less_than_3_weeks),
    age(under_1_year).

ask(longQT_syndrome) :-
    \+ asked(longQT_syndrome),
    \+ age(under_2_years).

ask(already_decongestant) :-
    \+ asked(tried_decongestant),
    longQT_syndrome(no).

%% THROAT ACHE
ask(fever) :-
    \+ asked(fever),
    throat_ache(yes).

ask(how_long_throat_ache) :-
    \+ asked(how_long_throat_ache),
    throat_ache(yes).

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
    medication(soothing_syrup).

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

advice(physician) :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years).

advice('balloon') :-
    blocked_nose(less_than_3_weeks),
    age(under_1_year),
    medication(none).

advice(physician) :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years).

advice(physician) :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years),
    medication(balloon).

advice('a salt/menthol nose spray') :-
    blocked_nose(less_than_3_weeks),
    longQT_syndrome(yes).

advice('a salt/menthol nose spray') :-
    blocked_nose(less_than_3_weeks),
    longQT_syndrome(no),
    medication(decongestant).

advice('a decongestant nose spray') :-
    blocked_nose(less_than_3_weeks),
    longQT_syndrome(no),
    medication(none).

%% THROAT ACHE
advice(physician) :-
    throat_ache(yes),
    fever(yes).

advice(physician) :-
    throat_ache(more_than_7_days).

advice(physician) :-
    throat_ache(more_than_3_days),
    age(under_6_years).

%% Basically "all the other cases": is there a nice way to do that?
advice('throat pastilles and paracetamol') :-
    throat_ache(less_than_3_days).

advice('throat pastilles and paracetamol') :-
    throat_ache(more_than_3_days),
    age(older_than_6_years).


advice(none).