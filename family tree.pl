% family_tree.pl

% Define family members and relationships
parent(john, mary). 
parent(jane, mary). 
parent(jane, tom).
male(john). 
male(tom).
female(jane). 
female(mary).

% Define basic relationships
father(F, C) :- parent(F, C), male(F).
mother(M, C) :- parent(M, C), female(M).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
