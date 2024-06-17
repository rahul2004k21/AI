from itertools import permutations

def solve_cryptarithmetic(puzzle):
    unique_letters = set(char for char in puzzle if char.isalpha())
    letters = list(unique_letters)
    
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        expression = puzzle.translate(str.maketrans(mapping))
        if eval(expression):
            return mapping
    
    return None

puzzle = "SEND + MORE == MONEY"
solution = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution found:")
    for char, digit in solution.items():
        print(f"{char} = {digit}")
else:
    print("No solution found.")
