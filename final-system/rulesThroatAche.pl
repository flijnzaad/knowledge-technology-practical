%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added using asserta/1.
:- dynamic temperature/1.
:- dynamic advice/1.
:- dynamic age/1.
:- dynamic asked/1.
:- dynamic throat_ache/1.
:- dynamic only_pain/1.
% TODO: probably needs more still (it returns a permission error static
%       procedure of some sort, put it here).

%% Dummy facts to 'introduce' the predicates to the knowledge base
temperature(unknown).
only_pain(yes)
age(none).
asked(none).
% TODO: change cough(yes) once we start incorporating other symptoms!
throat_ache(yes).
medication(unknown).
pregnant(unknown).


%% Rules that infer which questions to ask

% TODO: is the negation too much hardcoding? Retracting rules doesn't seem
%       like an option either
ask(temperature_over_38dot5) :-
    \+ asked(temperature_over_38dot5),
    throat_ache(yes).

ask(under_6_years) :-
    \+ asked(under_6_years),
    throat_ache(yes).

ask(throat_ache_over_3_days) :-
    \+ asked(throatache_over_3_days),
    age(under_6_years).

ask(under_3_months) :-
    \+ asked(under_3_months),
    throat_ache(yes).

ask(only_pain) :-
    \+ asked(only_pain),
    throat_ache(yes).


%% Rules for inference of advice
advice(none).                               % dummy fact to introduce advice/1
                             % dummy fact to introduce advice/1

advice(physician) :-
    throat_ache(yes),
    temperature(over_38dot5).

advice(physician) :-
    throat_ache(yes),
    age(under_6_years),
    throat_ache(over_3_days).

advice(physician) :-
    throat_ache(yes),
    age(under_6_years),
    throat_ache(over_3_days),
    temperature(over_38dot5).


advice('prescribed paracetamol') :-
    throat_ache(yes),
    age(under_3_months).

advice('throat pastilles or painkillers(gurgle paracetamol dissolved in water)') :-
    throat_ache(yes),
    only_pain(yes).




