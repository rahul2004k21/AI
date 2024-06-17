% Facts representing individuals and their dates of birth
dob(john, date(1990, 5, 15)).
dob(sarah, date(1985, 10, 25)).
dob(michael, date(1978, 3, 8)).
dob(emily, date(1995, 8, 3)).

% Rules for querying the database

% Predicate to find the age of a person
age(Person, Age) :-
    dob(Person, DateOfBirth),
    current_date(CurrentDate),
    calculate_age(DateOfBirth, CurrentDate, Age).

% Predicate to calculate the age given two dates
calculate_age(date(Year1, Month1, Day1), date(Year2, Month2, Day2), Age) :-
    Age is Year2 - Year1 - ( (Month2, Day2) @< (Month1, Day1) ).

% Current date (You can replace this with your own current date)
current_date(date(2024, 6, 13)).
