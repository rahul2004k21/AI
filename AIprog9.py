from itertools import permutations

def tsp(graph):
    n = len(graph)
    min_cost = float('inf')
    optimal_path = None

    for path in permutations(range(1, n)):
        cost = 0
        current_node = 0
        for next_node in path:
            cost += graph[current_node][next_node]
            current_node = next_node
        cost += graph[current_node][0]

        if cost < min_cost:
            min_cost = cost
            optimal_path = (0,) + path + (0,)

    return min_cost, optimal_path

# Example usage:
if __name__ == "__main__":
    # Example graph - distances between cities
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    min_cost, optimal_path = tsp(graph)
    print(f"Minimum cost: {min_cost}")
    print(f"Optimal path: {optimal_path}")
