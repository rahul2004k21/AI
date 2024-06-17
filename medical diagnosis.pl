% Define symptoms for each disease
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, sore_throat).

symptom(cold, runny_nose).
symptom(cold, sneezing).
symptom(cold, sore_throat).

symptom(allergy, sneezing).
symptom(allergy, itchy_eyes).
symptom(allergy, runny_nose).

% Disease prevention methods
prevention(flu, get_vaccinated).
prevention(cold, wash_hands).
prevention(allergy, avoid_allergens).

% Rule to diagnose a disease based on symptoms
diagnose(Disease, Symptoms) :-
    findall(S, member(S, Symptoms), SymptomList),
    match_disease(Disease, SymptomList).

% Match symptoms to a disease
match_disease(Disease, Symptoms) :-
    findall(Symptom, symptom(Disease, Symptom), DiseaseSymptoms),
    subset(DiseaseSymptoms, Symptoms).

% Check if all elements of one list are in another list
subset([], _).
subset([X|Xs], Ys) :-
    member(X, Ys),
    subset(Xs, Ys).

% Example queries
% ?- diagnose(Disease, [fever, cough, sore_throat]).
% Expected output: Disease = flu

% ?- diagnose(Disease, [runny_nose, sneezing, sore_throat]).
% Expected output: Disease = cold

% ?- diagnose(Disease, [sneezing, itchy_eyes, runny_nose]).
% Expected output: Disease = allergy

% Additional queries for prevention
% ?- prevention(flu, Prevention).
% Expected output: Prevention = get_vaccinated
