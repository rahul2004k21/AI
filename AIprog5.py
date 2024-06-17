from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def __eq__(self, other):
        return self.missionaries == other.missionaries and \
               self.cannibals == other.cannibals and \
               self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __str__(self):
        return f"(M: {self.missionaries}, C: {self.cannibals}, B: {self.boat})"

    def is_valid(self):
        if self.missionaries < 0 or self.missionaries > 3 or \
           self.cannibals < 0 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
            return False
        return True

    def successors(self):
        succ = []
        if self.boat == 1:
            succ.extend([
                State(self.missionaries - 1, self.cannibals, 0),
                State(self.missionaries, self.cannibals - 1, 0),
                State(self.missionaries - 1, self.cannibals - 1, 0),
                State(self.missionaries - 2, self.cannibals, 0),
                State(self.missionaries, self.cannibals - 2, 0)
            ])
        else:
            succ.extend([
                State(self.missionaries + 1, self.cannibals, 1),
                State(self.missionaries, self.cannibals + 1, 1),
                State(self.missionaries + 1, self.cannibals + 1, 1),
                State(self.missionaries + 2, self.cannibals, 1),
                State(self.missionaries, self.cannibals + 2, 1)
            ])
        return [s for s in succ if s.is_valid()]

def breadth_first_search():
    initial_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)
    queue = deque([([], initial_state)])
    visited = set()

    while queue:
        path, current_state = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]
        if current_state not in visited:
            visited.add(current_state)
            for succ in current_state.successors():
                queue.append((path + [current_state], succ))

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Solution found:")
        for i, state in enumerate(solution):
            print(f"Step {i + 1}: {state}")

if __name__ == "__main__":
    solution = breadth_first_search()
    print_solution(solution)
