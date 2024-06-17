import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, cost))
    
    def get_neighbors(self, node):
        return self.graph.get(node, [])

def heuristic(node, goal):
    # Example: Manhattan distance heuristic for grid-like graph
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph.graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.graph}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current_f, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]

        for neighbor, cost in graph.get_neighbors(current_node):
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge((0, 0), (0, 1), 1)
    graph.add_edge((0, 0), (1, 0), 1)
    graph.add_edge((0, 1), (1, 1), 1)
    graph.add_edge((1, 0), (1, 1), 1)
    graph.add_edge((1, 1), (2, 1), 1)
    graph.add_edge((1, 1), (1, 2), 1)
    graph.add_edge((2, 1), (2, 2), 1)
    graph.add_edge((1, 2), (2, 2), 1)

    start = (0, 0)
    goal = (2, 2)
    path = astar(graph, start, goal)
    print("Optimal path:", path)
 
