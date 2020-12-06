medication(none).                           % dummy facts to 'introduce' the 
age(none).                                  % predicate to the KB 

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
    \+ age(under_2_years).                    % check whether that negation is correct

take(soothing_syrup) :-
    cough(severe),
    cough(productive),
    antibiotics(yes).

take(soothing_syrup) :-
    cough(severe),
    cough(productive),
    age(under_2_years).
