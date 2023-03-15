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