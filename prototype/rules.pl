%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added
:- dynamic advice/1.
:- dynamic age/1.
:- dynamic asked/1.
:- dynamic cough/1.
:- dynamic medication/1.
% TODO: probably needs more still (it returns a permission error static 
%       procedure of some sort

medication(unknown).                        % dummy facts to 'introduce' the 
age(none).                                  % predicates to the KB 
cough(yes).
% TODO: change that once we start incorporating other symptoms!
asked(none).
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

ask(already_soothing) :-
    \+ asked(already_soothing),
    cough(less_than_7_days).

%% Rules for inference
advice(none).

advice(physician) :-
    cough(more_than_3_weeks).

advice(physician) :-
    cough(yes),
    age(under_3_months).

advice(physician) :-
    cough(more_than_7_days),
    other_symptoms(more_than_7_days).

advice(physician) :-
    medication(ace_inhibitors).

advice(suppressant) :-
    cough(yes),
    medication(soothing_syrup).

advice(soothing_syrup) :-
    age(under_6_years).

advice(soothing_syrup) :-
    pregnant(yes).

advice(soothing_syrup) :-
    cough(mild).

advice(suppressant) :-
    cough(severe),
    cough(dry),
    sedative(no).

% check this with the expert
advice(soothing_syrup) :-
    cough(severe),
    cough(dry),
    sedative(yes).

advice(expectorant) :-
    cough(severe),
    cough(productive),
    antibiotics(no),
    \+ age(under_2_years).                  % check whether that negation is correct

advice(soothing_syrup) :-
    cough(severe),
    cough(productive),
    antibiotics(yes).

advice(soothing_syrup) :-
    cough(severe),
    cough(productive),
    age(under_2_years).
