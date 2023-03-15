import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def test_parsing(self):
        board_str = '#####\n#...#\n#...#\n#####'.split('\n')
        starts = {'A': (2,1)}
        targets = {'A': (2,3)}
        board = Board(board_str, starts, targets)
        self.assertEqual(board._board, 
          [[1,1,1,1,1], [1,0,0,0,1], [1,0,0,0,1], [1,1,1,1,1]]
        )
        self.assertEqual(board._n, 4)
        self.assertEqual(board._m, 5)
        self.assertIn('A', board._starts)
        self.assertIn('A', board._targets)
        self.assertEqual(board._starts['A'], (2,1))
        self.assertEqual(board._targets['A'], (2,3))
        self.assertEqual(board.get_start(), (('A', (2,1)),))
    
    def test_win(self):
        board_str = '#####\n#...#\n#...#\n#####'.split('\n')
        starts = {'A': (2,1)}
        targets = {'A': (2,3)}
        board = Board(board_str, starts, targets)
        self.assertTrue(board.is_win((('A', (2,3)),)))
        self.assertFalse(board.is_win((('B', (2,3)),)))
        self.assertFalse(board.is_win((('A', (3,1)),)))

        board_str = '#####\n#...#\n#...#\n#...#\n#####'.split('\n')
        starts = {'A': (2,1), 'B': (3,1)}
        targets = {'A': (2,3), 'B': (3,3)}
        board = Board(board_str, starts, targets)
        self.assertFalse(board.is_win((('A', (2,3)),)))
        self.assertTrue(board.is_win((('A', (2,3)), ('B', (3,3)))))
    
    def test_neighbors(self):
        # Check both with walls and without outer walls.
        board_str = '#####\n.....\nA....\n.....\n#####'.split('\n')
        starts = {'A': (2,0)}
        targets = {'A': (2,4)}
        board = Board(board_str, starts, targets)
        neighbors = board.get_neighbors(board.get_start())
        self.assertIn(((('A', (1,0)),), 'A UP'), neighbors)
        self.assertIn(((('A', (3,0)),), 'A DOWN'), neighbors)
        self.assertIn(((('A', (2,4)),), 'A RIGHT'), neighbors)
        self.assertEqual(len(neighbors), 3)