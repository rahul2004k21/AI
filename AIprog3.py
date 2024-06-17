from collections import deque

def is_valid(state, jug1_capacity, jug2_capacity):
    jug1, jug2 = state
    return 0 <= jug1 <= jug1_capacity and 0 <= jug2 <= jug2_capacity

def solve_water_jug(jug1_capacity, jug2_capacity, target_volume):
    queue = deque([(0, 0)]) 
    visited = set()
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        if jug1 == target_volume or jug2 == target_volume:
            return True
        
        visited.add((jug1, jug2))
        
        next_states = [
            (jug1_capacity, jug2),     
            (jug1, jug2_capacity),     
            (0, jug2),                
            (jug1, 0),                 
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   
        ]
        
        for next_state in next_states:
            if next_state not in visited and is_valid(next_state, jug1_capacity, jug2_capacity):
                queue.append(next_state)
    
    return False

jug1_capacity = 4
jug2_capacity = 3
target_volume = 2
if solve_water_jug(jug1_capacity, jug2_capacity, target_volume):
    print(f"Target volume of {target_volume} liters can be measured.")
else:
    print(f"Target volume of {target_volume} liters cannot be measured.")
