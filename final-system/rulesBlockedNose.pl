%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added using asserta/1.
:- dynamic longQT_syndrome/1.
:- dynamic advice/1.
:- dynamic age/1.
:- dynamic asked/1.
:- dynamic blocked_nose/1.
:- dynamic tried_decongestant/1.
% TODO: probably needs more still (it returns a permission error static
%       procedure of some sort, put it here).

%% Dummy facts to 'introduce' the predicates to the knowledge base
longQT_syndrome(unknown).
age(none).
asked(none).
blocked_nose(yes).
pregnant(unknown).
tried_decongestant(unknown).

%% Rules that infer which questions to ask

% TODO: is the negation too much hardcoding? Retracting rules doesn't seem
%       like an option either
ask(how_long_blocked_nose) :-
    \+ asked(how_long_blocked_nose),
    blocked_nose(yes).

ask(under_2_years) :-
    \+ asked(under_2_years),
    blocked_nose(less_than_3_weeks).

ask(under_1_year) :-
    \+ asked(under_1_year),
    breastfed(no).

ask(already_balloon) :-
    \+ asked(already_balloon),
    age(under_1_year).

ask(longQT_syndrome) :-
    \+ asked(longQT_syndrome),
    age(over_2_years).

ask(tried_decongestant) :-
    \+ asked(tried_decongestant),
    longQT_syndrome(no).

%% Rules for inference of advice
advice(none).                               % dummy fact to introduce advice/1

advice(physician) :-
    blocked_nose(more_than_3_weeks).

advice(physician) :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years),

advice(physician) :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years),
    age(over_1_year).

advice(physician) :-
    blocked_nose(less_than_3_weeks),
    age(under_2_years),
    medication(balloon).

advice('balloon') :-
    blocked_nose(less_than_3_weeks),
    age(under_1_year),
    medication(none).

advice('a salt/menthol nose spray') :-
    blocked_nose(less_than_3_weeks),
    age(over_2_years),
    longQT_syndrome(yes).

advice('a salt/menthol nose spray') :-
    blocked_nose(less_than_3_weeks),
    age(over_2_years),
    longQT_syndrome(no),
    medication(decongestant).

advice('a decongestant nose spray') :-
    blocked_nose(less_than_3_weeks),
    age(over_2_years),
    longQT_syndrome(no),
    medication(none).