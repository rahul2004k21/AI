sum(0, 0).  % Base case: Sum of integers from 1 to 0 is 0.
sum(N, Sum) :-
    N > 0,   % Ensure N is positive.
    N1 is N - 1,
    sum(N1, Sum1),
    Sum is Sum1 + N. % Sum is the sum of integers from 1 to N-1 plus N.
