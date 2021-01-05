%% Declare these predicates as dynamic, i.e. facts with these predicates
%% may be added using asserta/1.
:- dynamic longQT_syndrome/1.
:- dynamic advice/1.
:- dynamic age/1.
:- dynamic asked/1.
:- dynamic blockedNose/1.
:- dynamic breast_fed/1.
:- dynamic triedDecongestant/1.
% TODO: probably needs more still (it returns a permission error static
%       procedure of some sort, put it here).

%% Dummy facts to 'introduce' the predicates to the knowledge base
longQT_syndrome(unknown).
age(none).
asked(none).
% TODO: change cough(yes) once we start incorporating other symptoms!
blockedNose(yes).
breast_fed(unknown).
pregnant(unknown).
triedDecongestant(unknown).

%% Rules that infer which questions to ask

% TODO: is the negation too much hardcoding? Retracting rules doesn't seem
%       like an option either
ask(more_than_3_weeks) :-
    \+ asked(more_than_3_weeks),
    blockedNose(yes).

ask(less_than_3_weeks) :-
    \+ asked(less_than_3_weeks),
    blockedNose(yes).

ask(under_2_years) :-
    \+ asked(under_2_years),
    blockedNose(less_than_3_weeks).

ask(breast_fed) :-
    \+ asked(breast_fed),
    age(under_2_years).

ask(under_1_year) :-
    \+ asked(under_1_year),
    breast_fed(no).

ask(over_1_year) :-
    \+ asked(over_1_year),
    breast_fed(no).


ask(over_2_years) :-
    \+ asked(over_2_years),
    blockedNose(less_than_3_weeks).

ask(longQT_syndrome) :-
    \+ asked(longQT_syndrom),
    blockedNose(over_2_years).

ask(tried_decongestant) :-
    \+ asked(tried_decongestant),
    longQT_syndrome(no).



%% Rules for inference of advice
advice(none).                               % dummy fact to introduce advice/1

advice(physician) :-
    blockedNose(more_than_3_weeks).

advice(physician) :-
    blockedNose(yes),
    blockedNose(less_than_3_weeks),
    age(under_2_years),
    breast_fed(yes).

advice(physician) :-
    blockedNose(yes),
    blockedNose(less_than_3_weeks),
    age(under_2_years),
    breast_fed(no),
    age(over_1_year).

advice('balloon') :-
    blockedNose(yes),
    blockedNose(less_than_3_weeks),
    age(under_2_years),
    breast_fed(no),
    age(under_1_year).

advice('salt/menthol') :-
    blockedNose(yes),
    blockedNose(less_than_3_weeks),
    age(over_2_years),
    longQT_syndrome(yes).

advice('salt/menthol') :-
    blockedNose(yes),
    blockedNose(less_than_3_weeks),
    age(over_2_years),
    longQT_syndrome(yes).

advice('salt/menthol') :-
    blockedNose(yes),
    blockedNose(less_than_3_weeks),
    age(over_2_years),
    longQT_syndrome(no),
    triedDecongestant(yes).

advice('decongestant') :-
    blockedNose(yes),
    blockedNose(less_than_3_weeks),
    age(over_2_years),
    longQT_syndrome(no),
    triedDecongestant(no).



