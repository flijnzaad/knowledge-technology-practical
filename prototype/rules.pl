go(physician) :- 
    cough(morethan3weeks).

go(physician) :- 
    cough(yes), 
    age(under3months).

go(physician) :- 
    cough(morethan7days), 
    other_symptoms(morethan7days).

go(physician) :- 
    medication(ace_inhibitors).

take(suppressant) :- 
    cough(yes), 
    medication(soothing_syrup).

take(soothing_syrup) :- 
    age(under6years).

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
    \+ age(under2years).                    % check whether that negation is correct 

take(soothing_syrup) :-
    cough(severe),
    cough(productive),
    antibiotics(yes).

take(soothing_syrup) :-
    cough(severe),
    cough(productive),
    age(under2years).
