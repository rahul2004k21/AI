import heapq

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def next_moves(board):
    moves = []
    i, j = find_blank(board)
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < 3 and 0 <= y < 3:
            new_board = [row[:] for row in board]
            new_board[i][j], new_board[x][y] = new_board[x][y], new_board[i][j]
            moves.append(new_board)
    return moves

def manhattan(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                x, y = divmod(board[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def solve_puzzle(start):
    heap = [(manhattan(start), 0, start)]
    visited = set()
    while heap:
        _, moves, board = heapq.heappop(heap)
        if board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return moves
        if tuple(map(tuple, board)) in visited:
            continue
        visited.add(tuple(map(tuple, board)))
        for next_board in next_moves(board):
            heapq.heappush(heap, (moves + 1 + manhattan(next_board), moves + 1, next_board))

start_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
print("Initial State:")
for row in start_state:
    print(row)
print("Minimum number of moves to solve:", solve_puzzle(start_state))

