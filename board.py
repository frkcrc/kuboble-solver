class Board:
    """Simple board representation.
       
    Internally it stores stone states as dictionaries.
    However, dict isn't hashable, so it outputs states as a tuple
    instead in the format ((stone, (r,c)), ...).
    """

    def __init__(self, board_str):
        n, m = len(board_str), len(board_str[0])

        self._board = [[0] * m for _ in range(n)]
        self._targets = {}
        self._starts = {}
        self._n = n
        self._m = m

        for r in range(n):
            for c in range(m):
                ch = board_str[r][c]
                if ch == '#':
                    self._board[r][c] = 1
                if ch.islower():
                    self._targets[ch.upper()] = (r,c)
                if ch.isupper():
                    self._starts[ch] = (r,c)
    
    def get_start(self):
        return tuple(self._starts.items())
    
    def is_win(self, state):
        return self._targets == dict(state)
    
    def get_neighbors(self, state):
        state = dict(state)
        neighbors = []
        for (stone, (r,c)) in state.items():
            # Try moving the stone in the four directions.
            # UP:
            up = 0
            for i in range(r-1, -1, -1):
                if self._board[i][c] == 1:
                    break
                if (i, c) in state.values():
                    break
                up += 1
            if up > 0:
                neighbor = state.copy()
                neighbor[stone] = (r-up, c)
                neighbors.append((tuple(neighbor.items()), stone + ' UP'))
            # DOWN:
            down = 0
            for i in range(r+1, self._n):
                if self._board[i][c] == 1:
                    break
                if (i, c) in state.values():
                    break
                down += 1
            if down > 0:
                neighbor = state.copy()
                neighbor[stone] = (r+down, c)
                neighbors.append((tuple(neighbor.items()), stone + ' DOWN'))
            # LEFT:
            left = 0
            for i in range(c-1, -1, -1):
                if self._board[r][i] == 1:
                    break
                if (r, i) in state.values():
                    break
                left += 1
            if left > 0:
                neighbor = state.copy()
                neighbor[stone] = (r, c-left)
                neighbors.append((tuple(neighbor.items()), stone + ' LEFT'))
            # RIGHT:
            right = 0
            for i in range(c+1, self._m):
                if self._board[r][i] == 1:
                    break
                if (r, i) in state.values():
                    break
                right += 1
            if right > 0:
                neighbor = state.copy()
                neighbor[stone] = (r, c+right)
                neighbors.append((tuple(neighbor.items()), stone + ' RIGHT'))
            return neighbors