import sys
from collections import deque
from reader import read
from board import Board

# BFS solver.
def solveKuboble(board, maxMoves):
    seen, q = set(), deque()
    start = board.get_start()
    seen.add(start)
    q.append((start, []))

    while q:
        state, moves = q.popleft()
        if board.is_win(state):
            return moves
        if len(moves) == maxMoves:
            continue
        neighbors = board.get_neighbors(state)
        for neighbor, move in neighbors:
            if neighbor not in seen:
                seen.add(neighbor)
                q.append((neighbor, moves + [move]))
    return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 solver.py <file>')
        exit()
    contents = open(sys.argv[1]).read()
    maxMoves, board = read(contents)
    solution = solveKuboble(board, maxMoves)
    if solution:
        print('Solution found:')
        for move in solution:
            print(move)
    else:
        print(f'Could not find a solution in {maxMoves} moves.')