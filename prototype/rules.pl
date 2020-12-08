%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added
:- dynamic additional_symptoms/1.
:- dynamic advice/1.
:- dynamic age/1.
:- dynamic asked/1.
:- dynamic cough/1.
:- dynamic medication/1.
% TODO: probably needs more still (it returns a permission error static 
%       procedure of some sort

%% Dummy facts to 'introduce' the predicates to the knowledge base 
additional_symptoms(unknown).
age(none).
asked(none).
% TODO: change cough(yes) once we start incorporating other symptoms!
cough(yes).                                  
medication(unknown).                        
pregnant(unknown).

%% Rules for which questions to ask
% TODO: is the negation too much hardcoding? Retracting rules doesn't seem
%       like an option either
ask(younger_than_3_months) :-
    \+ asked(younger_than_3_months),
    cough(yes).

ask(using_ace_inhibitors) :-
    \+ asked(using_ace_inhibitors),
    age(over_3_months).
    % TODO: is this the correct rule body? should it include cough(yes)?

ask(how_long_cough) :-
    \+ asked(how_long_cough),
    medication(none).

ask(additional_symptoms) :-
    \+ asked(additional_symptoms),
    cough(more_than_7_days).

ask(cough_severity) :-
    \+ asked(cough_severity),
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

ask(younger_than_2_years) :-
    \+ asked(younger_than_2_years),
    medication(no_antibiotic).

%% Rules for inference
advice(none).

advice(physician) :-
    cough(more_than_3_weeks).

advice(physician) :-
    cough(yes),
    age(under_3_months).

advice(physician) :-
    cough(more_than_7_days),
    additional_symptoms(yes).

advice(physician) :-
    medication(ace_inhibitors).

advice(suppressant) :-
    cough(mild),
    medication('soothing syrup').

advice('soothing syrup') :-
    age(under_6_years).

advice('soothing syrup') :-
    pregnant(yes).

advice('soothing syrup') :-
    cough(mild).

advice(suppressant) :-
    cough(severe),
    cough(dry),
    sedative(no).

% check this with the expert
advice('soothing syrup') :-
    cough(severe),
    cough(dry),
    sedative(yes).

advice(expectorant) :-
    cough(severe),
    cough(productive),
    medication(no_antibiotic),
    age(over_2_years).

advice('soothing syrup') :-
    cough(severe),
    cough(productive),
    medication(antibiotic).

advice('soothing syrup') :-
    cough(severe),
    cough(productive),
    age(under_2_years).
