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

ask(fever) :-
    \+ asked(fever),
    throat_ache(yes).

ask(how_long_throat_ache) :-
    \+ asked(how_long_throat_ache),
    throat_ache(yes).

%% Rules for inference of advice
advice(none).                               % dummy fact to introduce advice/1

advice(physician) :-
    fever(yes).

advice(physician) :-
    throat_ache(more_than_7_days)

advice(physician) :-
    throat_ache(more_than_3_days),
    age(under_6_years).

%% Basically "all the other cases": is there a nice way to do that?
advice('throat pastilles and paracetamol') :-
    throat_ache(less_than_3_days);
    throat_ache(more_than_3_days),
    age(over_6_years).





