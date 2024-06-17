% Edge definitions
edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(c, e).
edge(d, e).

% BFS algorithm to find the shortest path
bfs(Start, Goal, Path) :-
    bfs([[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% Base case: If the path leads to the goal, return this path
bfs([[Goal | Rest] | _], Goal, [Goal | Rest]).

% Expand paths: explore all possible moves
bfs([CurrentPath | OtherPaths], Goal, Path) :-
    CurrentPath = [CurrentNode | _],
    findall([NextNode, CurrentNode | CurrentPath],
            (edge(CurrentNode, NextNode)),
            NewPaths),
    append(OtherPaths, NewPaths, UpdatedPaths),
    bfs(UpdatedPaths, Goal, Path).
