%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added
:- dynamic age/1.
:- dynamic medication/1.
:- dynamic asked/1.
:- dynamic cough/1.
% TODO: probably needs more still (it returns a permission error static 
%       procedure of some sort

medication(unknown).                        % dummy facts to 'introduce' the 
age(none).                                  % predicates to the KB 
cough(none).
asked(none).

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
go(physician) :-
    cough(more_than_3weeks).

go(physician) :-
    cough(yes),
    age(under_3_months).

go(physician) :-
    cough(more_than_7_days),
    other_symptoms(more_than_7_days).

go(physician) :-
    medication(ace_inhibitors).

take(none).

take(suppressant) :-
    cough(yes),
    medication(soothing_syrup).

take(soothing_syrup) :-
    age(under_6_years).

take(soothing_syrup) :-
    pregnant(yes).

take(soothing_syrup) :-
    cough(mild).

take(suppressant) :-
    cough(severe),
    cough(dry),
    sedative(no).

% check this with the expert
take(soothing_syrup) :-
    cough(severe),
    cough(dry),
    sedative(yes).

take(expectorant) :-
    cough(severe),
    cough(productive),
    antibiotics(no),
    \+ age(under_2_years).                  % check whether that negation is correct

take(soothing_syrup) :-
    cough(severe),
    cough(productive),
    antibiotics(yes).

take(soothing_syrup) :-
    cough(severe),
    cough(productive),
    age(under_2_years).
